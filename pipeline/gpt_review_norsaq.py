#!/usr/bin/env python3
"""gpt_review_norsaq.py — norsaq复刻页GPT三视角审稿
输出: ops/gpt_code_review_202611/diy_norsaq_page_review.md ; exit 1 = API失败
"""
import json, sys, time, urllib.request, os

cfg = {}
for line in open('/root/workspace/gpt.md'):
    line = line.strip()
    if line.startswith('http'): cfg['base'] = line
    elif line.startswith('sk-'): cfg['key'] = line
    elif line.lower().startswith('model:'): cfg['model'] = line.split(':', 1)[1].strip()
assert {'base', 'key', 'model'} <= cfg.keys()

ROOT = '/root/workspace/kayak-wiki'
page = open(f'{ROOT}/pipeline/staging/diy-norsaq.md', encoding='utf-8').read()
consult = open(f'{ROOT}/ops/gpt_code_review_202611/norsaq_consult.md', encoding='utf-8').read()
sister = open(f'{ROOT}/pipeline/staging/diy-bird-dart.md', encoding='utf-8').read()
nl = open(f'{ROOT}/raw/books/eskimo-life-nansen-1893/pg46972.txt', encoding='utf-8', errors='ignore').read().replace('\r', '')
import re
idxs = [m.start() for m in re.finditer(r'throwing-stick', nl)]
nansen = '\n'.join(nl.split('\n'))[idxs[0]-200:idxs[0]+4200] if idxs else ''

PROMPT = """你是格陵兰皮划艇装备复建与现代木工安全领域的资深审稿人。下面是知识库新页《复刻一支Norsaq——投掷板的材料、尺寸与装填》(DIY制作指南)，随附其取料底本：①Nansen 1893投掷板一手段落原文 ②GPT制作咨询记录(页内"工程起点"数字的出处) ③姊妹页《复建格陵兰投掷镖》(交叉引用对象)。请按三视角审稿：

**视角一 参数一致性**：页内一切数字与Nansen原文逐条核对(42-52cm/7-8cm/1.5cm/两形制/掷法/三地说)；与咨询记录核对(工程起点数字是否被转写错/确定性自标是否被丢)；与姊妹页交叉引用是否一致(托槽逻辑/槽宽口径/安全框架/7.6m出处)——任何转写错误给出更正与置信度(高/中/低)。
**视角二 可执行性**：一个有基础木工能力的制作者拿着这页能否走完——缺步骤/缺工具/顺序颠倒/两义表述；"先做试配杆再定接口"的主线是否贯穿(孔径孔位条与工序条是否自洽)。
**视角三 安全完整性**：警告是否前置、红线是否齐全(夹持/护目/控尘/展示件禁投/室内禁锐镖/猛甩硬拽停用/倒扣禁止/衬套掩盖禁止)、有无把"可释放挂接"误写成"锁死"之类的不安全表述；安全内容有无缺项(如儿童误用/运输存放)。
输出格式：
## 总评
## 勘误清单
- [视角] 原文片段 → 更正（置信度：高/中/低）
## 可执行性判定
## 安全完整性判定
不审文风。

=====【页面稿】=====
""" + page + """

=====【Nansen投掷板一手段落(1893)】=====
""" + nansen + """

=====【GPT制作咨询记录】=====
""" + consult + """

=====【姊妹页 diy-bird-dart.md】=====
""" + sister

req = urllib.request.Request(
    cfg['base'].rstrip('/') + '/v1/chat/completions',
    data=json.dumps({'model': cfg['model'], 'messages': [{'role': 'user', 'content': PROMPT}],
                     'max_completion_tokens': 16000}).encode(),
    headers={'Authorization': f'Bearer {cfg["key"]}', 'Content-Type': 'application/json'})
t0 = time.time()
try:
    with urllib.request.urlopen(req, timeout=580) as r:
        resp = json.load(r)
except Exception as e:
    print(f'API失败: {e}'); sys.exit(1)
content = resp['choices'][0]['message'].get('content') or ''
usage = resp.get('usage', {})
open('/tmp/gpt_norsaq_review_raw.txt', 'w', encoding='utf-8').write(
    f'finish={resp["choices"][0].get("finish_reason")} usage={json.dumps(usage, ensure_ascii=False)}\n\n{content}')
if len(content) <= 200:
    print('content过短'); sys.exit(1)
out = f'# GPT审稿: diy-norsaq.md《复刻一支Norsaq》(2026-11-16)\n\n- {cfg["model"]} | 三视角(参数一致性/可执行性/安全完整性) | 用时{time.time()-t0:.0f}s | usage={json.dumps(usage, ensure_ascii=False)}\n\n{content}\n'
open(f'{ROOT}/ops/gpt_code_review_202611/diy_norsaq_page_review.md', 'w', encoding='utf-8').write(out)
print(f'OK -> ops/gpt_code_review_202611/diy_norsaq_page_review.md  用时{time.time()-t0:.0f}s  tokens={usage.get("total_tokens")}')
