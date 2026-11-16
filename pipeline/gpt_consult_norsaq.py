#!/usr/bin/env python3
"""gpt_consult_norsaq.py — norsaq复刻工程缺口GPT咨询(尺寸/替材/装填)
输出: ops/gpt_code_review_202611/norsaq_consult.md ; exit 1 = API失败
"""
import json, sys, time, urllib.request

cfg = {}
for line in open('/root/workspace/gpt.md'):
    line = line.strip()
    if line.startswith('http'): cfg['base'] = line
    elif line.startswith('sk-'): cfg['key'] = line
    elif line.lower().startswith('model:'): cfg['model'] = line.split(':', 1)[1].strip()
assert {'base', 'key', 'model'} <= cfg.keys(), f'gpt.md缺字段: {cfg.keys()}'

PROMPT = """你是熟悉因纽特投掷板(norsaq/throwing-board)复建与现代木工的现代制作者顾问。背景：一手工参考（Nansen《Eskimo Life》1893 Ch.III一手记录）已确认的形态事实——格陵兰投掷板传统用红漂流木制；Nansen随身实测14件全长42-52厘米；下宽端约7-8厘米宽、厚约1.5厘米；宽端两侧有拇指/食指抓握凹槽；上平面全长一条沟槽安放镖杆。两种接口形制：①凸钮型（窄端凸钮插镖尾骨板凹槽，配浮囊镖/鸟镖）②双孔型（窄端一孔+近握把一孔，分别扣住鱼镖/长矛杆侧的两个后斜凸榫）。掷法：握把后持、武器水平向后，猛力前甩——板下端先脱开，上端仍扣，甩鞭式加速。现代复建者的镖杆直径计划16-20mm，板材要求能托住圆杆滑出。

我正在写一页"复刻norsaq投掷板"的DIY指南（前作《复建格陵兰投掷镖》已完成），以下工程缺口请给建议。**硬性要求：每条答案末尾自标确定性（高/中/低）；一切尺寸数字明确标注"工程起点（非文献值）"；涉及安全处给出红线。**

1. 尺寸缺口（工程起点）：①上平面沟槽：宽度与深度建议（托16-20mm圆杆、要"搁槽沿滑出而非埋槽"）②双孔型两个孔的孔径与孔位（距窄端/距握把的大致比例位置；孔与镖杆侧凸榫的配合公差）③窄端宽度（渐变到多少）④握把区长度与指凹槽深度 ⑤成品重量参考范围。
2. 现代材料替代：传统红漂流木难得。板材候选（白蜡木/硬枫/桦木/竹集成材/桦木航空层板等）按"刚度/密度/开槽易度"给2-3个推荐与理由；沟槽是否建议衬硬木条；双孔型孔缘是否建议加固（衬套/硬木销孔衬）；明确列2-3种不建议的材料及原因。
3. 装填与掷法细节：双孔型装填的完整动作序列（镖杆放槽、两个后斜凸榫入两孔、锁定检查）；出手时"下端先脱、上端后脱"的时序在复建件上如何自检；常见失败模式（卡滞/提前脱开/镖打转）与修法。
4. 手工工具最小集（无车床前提）与制作顺序（下料→开槽→开孔→握把→砂光的顺序里，哪些工序先后不可换）。
5. 验收标准两条式（托得稳/脱板不夹滞之外还有什么硬指标）。

输出格式：
## 尺寸建议(工程起点)
## 材料替代
## 装填与掷法
## 工具与工序
## 验收标准
每条含确定性自标(高/中/低)。"""

req = urllib.request.Request(
    cfg['base'].rstrip('/') + '/v1/chat/completions',
    data=json.dumps({'model': cfg['model'], 'messages': [{'role': 'user', 'content': PROMPT}],
                     'max_completion_tokens': 12000}).encode(),
    headers={'Authorization': f'Bearer {cfg["key"]}', 'Content-Type': 'application/json'})
t0 = time.time()
try:
    with urllib.request.urlopen(req, timeout=900) as r:
        resp = json.load(r)
except Exception as e:
    print(f'API失败: {e}'); sys.exit(1)

content = resp['choices'][0]['message'].get('content') or ''
usage = resp.get('usage', {})
open('/tmp/gpt_norsaq_raw.txt', 'w', encoding='utf-8').write(
    f'finish={resp["choices"][0].get("finish_reason")} usage={json.dumps(usage, ensure_ascii=False)}\n\n{content}')
if len(content) <= 200:
    print('content过短, 详见/tmp/gpt_norsaq_raw.txt'); sys.exit(1)
import os
os.makedirs('/root/workspace/kayak-wiki/ops/gpt_code_review_202611', exist_ok=True)
out = f'# GPT咨询: norsaq复刻工程缺口(2026-11-16)\n\n- {cfg["model"]} | 用时{time.time()-t0:.0f}s | usage={json.dumps(usage, ensure_ascii=False)}\n\n{content}\n'
open('/root/workspace/kayak-wiki/ops/gpt_code_review_202611/norsaq_consult.md', 'w', encoding='utf-8').write(out)
print(f'OK -> ops/gpt_code_review_202611/norsaq_consult.md  用时{time.time()-t0:.0f}s  tokens={usage.get("total_tokens")}')
