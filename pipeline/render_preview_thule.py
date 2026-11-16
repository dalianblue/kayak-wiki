#!/usr/bin/env python3
"""render_preview_thule.py — thule-origin 页预览渲染(带 Archive 的 Story, 修复技能脚本丢图坑)
坑实锚(1116): md_preview_pdf.py 用 <img src="file://..."> 且 Story 无 archive 参数 → 图片静默丢弃
用法: python3 pipeline/render_preview_thule.py
"""
import importlib.util, os, re, fitz

SKILL = '/root/.hermes/skills/devops/kayak-wiki-ops/scripts/md_preview_pdf.py'
spec = importlib.util.spec_from_file_location('mdp', SKILL)
mdp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mdp)

ROOT = '/root/workspace/kayak-wiki'
MD = f'{ROOT}/pipeline/staging/thule-origin.md'
IMGDIR = f'{ROOT}/pipeline/staging/img'
OUT = f'{ROOT}/pipeline/staging/thule-origin-preview.pdf'

md = open(MD, encoding='utf-8').read()
# fig 行自行处理(img+caption 一起包进居中div; caption 走技能脚本 inline()), 其余行走 mdp.md_to_html
fig_re = re.compile(r'^\{\{fig:([^}]+)\}\}\s*(.*)$')

def _inline(t):
    # 与技能脚本 md_to_html 内嵌 inline() 同款: wikilink→文本, 锚→灰字, **加粗, *斜体
    t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', t)
    t = re.sub(r'\^\[([^\]]+)\]', r'<span style="font-size:11px;color:#888">⟦锚: \1⟧</span>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'\*(.+?)\*', r'<i>\1</i>', t)
    return t

blocks, buf = [], []
for ln in md.split('\n'):
    m = fig_re.match(ln)
    if m:
        if buf:
            blocks.append(('md', '\n'.join(buf))); buf = []
        img, cap = m.group(1), _inline(m.group(2).strip())
        # 竖高图限高防占满版心挤掉caption(实锚: 南格陵兰图873x1359缩放后超版心, caption被静默丢弃)
        from PIL import Image as _Im
        try:
            w, h = _Im.open(os.path.join(IMGDIR, img)).size
            img_tag = f'<img src="{img}" height="620">' if h > 1.15 * w else f'<img src="{img}">'
        except Exception:
            img_tag = f'<img src="{img}">'
        cap_html = f'<div style="font-size:12px;color:#666;text-align:center">{cap}</div>' if cap else ''
        blocks.append(('fig', f'<div style="text-align:center;margin:14px 0">{img_tag}{cap_html}</div>'))
    else:
        buf.append(ln)
if buf:
    blocks.append(('md', '\n'.join(buf)))
def _md_body(md_text):
    """md_to_html 输出完整文档 → 只取 body 内层, 供单文档拼接"""
    s = mdp.md_to_html(md_text, None)
    return s.split('<body>', 1)[1].rsplit('</body>', 1)[0]

html = '<html><head><meta charset="utf-8"></head><body>' + ''.join(
    b if k == 'fig' else _md_body(b) for k, b in blocks) + '</body></html>'
assert '<img src="fig-' in html and 'Sinding' in html, 'fig或caption替换失败'

archive = fitz.Archive(IMGDIR)          # 图片目录入 archive, src 相对名解析
story = fitz.Story(html=html, archive=archive)
doc = fitz.DocumentWriter(OUT)
mediabox = fitz.paper_rect('a4')
where = fitz.Rect(36, 36, mediabox.width - 36, mediabox.height - 36)
more, pages = 1, 0
while more:
    dev = doc.begin_page(mediabox)
    more, _ = story.place(where)
    story.draw(dev)
    doc.end_page()
    pages += 1
    if pages > 40:
        break
doc.close()
print(f'{OUT}: {pages} 页')

d = fitz.open(OUT)
base = os.path.splitext(OUT)[0]
n = 0
for p in range(len(d)):
    d[p].get_pixmap(dpi=100).save(f'{base}_p{p + 1}.png')
    n += 1
print(f'pngs: {n} 张')
print('embedded per page:', [len(pg.get_images(full=True)) for pg in d])
