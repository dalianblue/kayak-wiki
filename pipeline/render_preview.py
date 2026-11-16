#!/usr/bin/env python3
"""render_preview.py — 通用staging页PDF预览(带Archive的Story, 修复技能脚本丢图坑)
坑实锚(1116): 技能md_preview_pdf.py ①Story无archive→file://图静默丢弃 ②archive按文件名精确匹配(fig id勿带扩展名)
③竖高图超版心→caption被静默挤丢(img height=620限高) ④md_to_html整段拼接产生多<html>头致内容丢失→剥壳单文档拼接
用法: python3 pipeline/render_preview.py --md <页路径> [--imgdir <图目录>] [--pngs]
"""
import argparse, importlib.util, os, re, fitz

SKILL = '/root/.hermes/skills/devops/kayak-wiki-ops/scripts/md_preview_pdf.py'
spec = importlib.util.spec_from_file_location('mdp', SKILL)
mdp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mdp)

ap = argparse.ArgumentParser()
ap.add_argument('--md', required=True)
ap.add_argument('--imgdir', default=None)
ap.add_argument('--out', default=None)
ap.add_argument('--pngs', action='store_true')
a = ap.parse_args()
out = a.out or os.path.splitext(a.md)[0] + '-preview.pdf'

md = open(a.md, encoding='utf-8').read()
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
        img_tag = f'<img src="{img}">'
        if a.imgdir:
            from PIL import Image as _Im
            p = os.path.join(a.imgdir, img)
            if os.path.exists(p):
                try:
                    w, h = _Im.open(p).size
                    if h > 1.15 * w:
                        img_tag = f'<img src="{img}" height="620">'
                except Exception:
                    pass
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

story = fitz.Story(html=html, archive=(fitz.Archive(a.imgdir) if a.imgdir else None))
doc = fitz.DocumentWriter(out)
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
print(f'{out}: {pages} 页')

d = fitz.open(out)
n_img = [len(p.get_images(full=True)) for p in d]
print('embedded per page:', n_img, '| total imgs:', sum(n_img))
if a.pngs:
    base = os.path.splitext(out)[0]
    for p in range(len(d)):
        d[p].get_pixmap(dpi=100).save(f'{base}_p{p + 1}.png')
    print(f'pngs: {len(d)} 张')
