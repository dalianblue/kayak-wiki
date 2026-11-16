#!/usr/bin/env python3
"""gpt_review_thule_1116.py — 图勒起源页送GPT事实审阅(施主1114令: GPT知道的比一休多)
输出: ops/gpt_code_review_202611/thule_origin_review.md ; exit 1 = API失败(不静默)"""
import json, sys, time, urllib.request

cfg = {}
for line in open('/root/workspace/gpt.md'):
    line = line.strip()
    if line.startswith('http'): cfg['base'] = line
    elif line.startswith('sk-'): cfg['key'] = line
    elif line.lower().startswith('model:'): cfg['model'] = line.split(':', 1)[1].strip()
assert {'base', 'key', 'model'} <= cfg.keys(), f'gpt.md缺字段: {cfg.keys()}'

ROOT = '/root/workspace/kayak-wiki'
page = open(f'{ROOT}/pipeline/staging/thule-origin.md', encoding='utf-8').read()
wikis = {}
for t in ('thule-people', 'dorset-culture', 'paleo-eskimo'):
    wikis[t] = open(f'{ROOT}/raw/sources/wikipedia-prehistory/{t}.txt', encoding='utf-8').read()
nl = open(f'{ROOT}/raw/books/eskimo-life-nansen-1893/pg46972.txt', encoding='utf-8', errors='ignore').read().replace('\r', '')
nansen = '\n'.join(nl.split('\n')[419:645])  # Ch.I 起源段(Gutenberg行420-645)

PROMPT = """你是极地考古学与因纽特史前史领域的资深审稿人（熟悉Thule文化研究、Paleo-Eskimo序列、古DNA文献: 2010 Nature Inuk基因组 / 2014 Science Raghavan等 / 2019 Nature Flegontov等, 以及McGhee的文化生态模型）。下面是中文皮划艇知识库的一页新稿《格陵兰人的起源》（图勒人起源, 综合页）, 随附其全部取料底本（维基百科三篇快照 + Nansen《Eskimo Life》Ch.I节选）。请做严格的事实审阅：

1. 逐条核对史实：年代、人名、地名、文化序列(OBS/Punuk/Birnirk)、单倍群数字、事件细节——任何错误给出更正与置信度(高/中/低)。
2. 本页三大论点——①根在亚洲②图勒文化在阿拉斯加孕育成型后才东进③东迁动力是技术外溢+追随资源而非吃苦耐劳——核对页内表述与考古学证据是否匹配, 有无过度声称(overclaim)。
3. 标记"维基口径但学界存疑或有更新"的说法（如抵达格陵兰的确切年代、多塞特消失年代、图勒-多塞特关系细节、McGhee模型之外的新解释）。
4. Nansen 1893年文字的转述是否忠实（含对Rink观点的转述、Skræling文献解读、路线争论的概括）。
5. 指出任何中文表述造成的史实歧义或因果夸大。
6. 不审文风, 只审事实。输出格式：
## 总评
## 勘误清单
- [错误/存疑/确认] 原文片段 → 更正内容（置信度：高/中/低）
## 论点匹配度判定
## 需要补充的关键事实（如有）

=====【页面稿】=====
""" + page + """

=====【维基: thule-people】=====
""" + wikis['thule-people'] + """

=====【维基: dorset-culture】=====
""" + wikis['dorset-culture'] + """

=====【维基: paleo-eskimo】=====
""" + wikis['paleo-eskimo'] + """

=====【Nansen Eskimo Life Ch.I 节选(1893)】=====
""" + nansen

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
    with urllib.request.urlopen(req, timeout=900) as r:
        resp = json.load(r)
except Exception as e:
    print(f'API失败: {e}'); sys.exit(1)

content = resp['choices'][0]['message'].get('content') or ''
reasoning = resp['choices'][0]['message'].get('reasoning_content') or ''
usage = resp.get('usage', {})
open('/tmp/gpt_thule_raw.txt', 'w', encoding='utf-8').write(
    f'finish={resp["choices"][0].get("finish_reason")} usage={json.dumps(usage, ensure_ascii=False)}\n\n{content}\n\n==REASONING==\n{reasoning}')
if len(content) <= 200:
    print(f'诊断: finish={resp["choices"][0].get("finish_reason")} usage={json.dumps(usage)}')
    print('content过短, 详见/tmp/gpt_thule_raw.txt'); sys.exit(1)

out = f'# GPT审稿: thule-origin.md《格陵兰人的起源》(2026-11-16)\n\n- 模型: {cfg["model"]} | prompt含页面稿+维基快照x3+Nansen Ch.I节选 | 用时{time.time()-t0:.0f}s | usage={json.dumps(usage, ensure_ascii=False)}\n\n{content}\n'
open(f'{ROOT}/ops/gpt_code_review_202611/thule_origin_review.md', 'w', encoding='utf-8').write(out)
print(f'OK -> ops/gpt_code_review_202611/thule_origin_review.md  用时{time.time()-t0:.0f}s  usage={json.dumps(usage, ensure_ascii=False)}')
