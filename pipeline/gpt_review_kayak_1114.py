#!/usr/bin/env python3
"""gpt_review_kayak_1114.py — 演变三页送GPT事实审阅(施主1114令: GPT知道的比一休多)
输出: pipeline/reviews/kayak-gpt-1114.md ; exit 1 = API失败(不静默)"""
import json, sys, time, urllib.request

cfg = {}
for line in open('/root/workspace/gpt.md'):
    line = line.strip()
    if line.startswith('http'): cfg['base'] = line
    elif line.startswith('sk-'): cfg['key'] = line
    elif line.lower().startswith('model:'): cfg['model'] = line.split(':', 1)[1].strip()
assert {'base', 'key', 'model'} <= cfg.keys(), f'gpt.md缺字段: {cfg.keys()}'

PAGES = {'greenland-qajaq': 'site-demo/docs/evolution/greenland-qajaq.md',
         'aleut-baidarka': 'pipeline/staging/aleut-baidarka.md',
         'british-sea-kayak': 'site-demo/docs/evolution/british-sea-kayak.md'}
pages = {}
for name, rel in PAGES.items():
    pages[name] = open(f'/root/workspace/kayak-wiki/{rel}', encoding='utf-8').read()

PROMPT = '''你是皮划艇史与海事民族志领域的资深审稿人（熟悉Inuit/Aleut皮艇研究、海划艇设计史、极地探险史）。下面是中文皮划艇知识库"技术演变路线"的三页新稿（格陵兰qajaq / 阿留申baidarka / 英式海划革命）。请做严格的事实审阅：

1. 逐条核对史实：年代、人名、地名、船名、尺寸数字、事件细节——任何错误给出更正与置信度(高/中/低)。
2. 标记"wiki常见但学界存疑"的说法（如4000年起源、最老1577年艇等），说明学界现口径。
3. 英式革命页中 Anas Acuta 与 Nordkapp 段落：核对设计者全名、年代、建造厂、设计背景（Ken Turner? Ken Taylor? 年代1970-71还是更晚? Nordkapp 1975还是1976?），给出你掌握的最准确事实。
4. 指出任何中文表述造成的史实歧义。
5. 不审文风，只审事实。输出格式：
## 总评
## 逐页勘误
### <页名>
- [错误/存疑/确认] 原文片段 → 更正内容（置信度：高/中/低）
## 需要补充的关键事实（如有）

---

''' + '\n\n=====\n\n'.join(f'【{k}】\n{v}' for k, v in pages.items())

req = urllib.request.Request(
    cfg['base'].rstrip('/') + '/v1/chat/completions',
    data=json.dumps({
        'model': cfg['model'],
        'messages': [{'role': 'user', 'content': PROMPT}],
        'max_completion_tokens': 16000,
    }).encode(),
    headers={'Authorization': f'Bearer {cfg["key"]}', 'Content-Type': 'application/json'})
t0 = time.time()
try:
    with urllib.request.urlopen(req, timeout=600) as r:
        resp = json.load(r)
except Exception as e:
    print(f'API失败: {e}'); sys.exit(1)

content = resp['choices'][0]['message'].get('content') or ''
reasoning = resp['choices'][0]['message'].get('reasoning_content') or ''
usage = resp.get('usage', {})
# 响应先无条件落盘(防后续任何一步摔了丢响应)
open('/tmp/gpt_review_last_raw.txt', 'w', encoding='utf-8').write(
    f'finish={resp["choices"][0].get("finish_reason")} usage={json.dumps(usage, ensure_ascii=False)}\n\n{content}\n\n==REASONING==\n{reasoning}')
if len(content) <= 200:
    print(f'诊断: finish_reason={resp["choices"][0].get("finish_reason")} usage={json.dumps(usage)} '
          f'message_keys={list(resp["choices"][0]["message"].keys())} reasoning_len={len(reasoning)}')
assert len(content) > 200, f'响应过短({len(content)}字), 疑似截断: {content[:200]}'

out = f'''# GPT审稿 — 演变三页（{time.strftime('%Y-%m-%d %H:%M')}）
模型: {cfg['model']} | 用时: {time.time()-t0:.0f}s | usage: {json.dumps(usage, ensure_ascii=False)}

{content}

---
## reasoning_content（思考过程存档）
{reasoning[:3000]}
'''
path = '/root/workspace/kayak-wiki/pipeline/reviews/kayak-gpt-1114.md'
import os
os.makedirs(os.path.dirname(path), exist_ok=True)
open(path, 'w', encoding='utf-8').write(out)
print(f'审稿完成 → {path} ({len(out)}字)')
