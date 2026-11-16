#!/usr/bin/env python3
"""draw_thule_map.py — 图勒东迁路线示意图(自绘, own rights, 脚本可复现)
输出: pipeline/staging/img/fig-thule-map (PNG)
海岸线与地物高度简化示意, 不按比例; 实线通道=器物分布支持的推定方向, 虚线=气候-鲸模型推断
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fontTools.ttLib import TTCollection
from matplotlib import font_manager
from matplotlib.patches import Polygon as MplPoly, Ellipse, FancyArrowPatch

SC_TTF = '/root/.hermes/cache/scratch/NotoSansCJKsc-Regular.ttf'
if not os.path.exists(SC_TTF):
    tc = TTCollection('/usr/share/fonts/google-noto-cjk/NotoSansCJK-Regular.ttc')
    for f in tc.fonts:
        if 'SC' in (f['name'].getDebugName(1) or ''):
            f.save(SC_TTF); break
font_manager.fontManager.addfont(SC_TTF)
plt.rcParams['font.family'] = font_manager.FontProperties(fname=SC_TTF).get_name()

PAPER, LAND, INK, BLUE, ROUTE = '#f7f4ec', '#e8e2d4', '#33414e', '#4a86b8', '#8a4a1d'
BOX = dict(boxstyle='round,pad=0.3', fc=PAPER, ec='none', alpha=.92)  # 文字纸色底, 防压线

fig, ax = plt.subplots(figsize=(12, 7.2), dpi=150)
ax.set_xlim(0, 100); ax.set_ylim(6, 60); ax.axis('off')
fig.patch.set_facecolor(PAPER); ax.set_facecolor(PAPER)

def blob(pts, label=None, lx=0, ly=0, fs=12):
    ax.add_patch(MplPoly(pts, closed=True, facecolor=LAND, edgecolor='#b9b1a0', lw=1.2))
    if label:
        ax.text(lx, ly, label, ha='center', va='center', fontsize=fs, color=INK, alpha=.85)

# 地物(简化示意)
blob([(2,34),(8,40),(16,44),(22,46),(24,50),(18,56),(8,58),(2,50)], '东西伯利亚\n(楚科奇)', 10, 48)
blob([(27,44),(33,47),(40,48),(47,47),(50,44),(47,38),(40,36),(32,37),(28,40)], '阿拉斯加', 37, 42)
blob([(50,44),(58,44),(66,42),(72,40),(76,38),(74,30),(66,26),(56,26),(50,32)], '加拿大大陆', 62, 32)
for cx, cy in [(52,51.5),(57,50.6),(63,51.8),(68,50.9)]:
    ax.add_patch(Ellipse((cx,cy), 5, 2.2, facecolor=LAND, edgecolor='#b9b1a0', lw=1))
blob([(78,52),(84,54),(90,50),(93,42),(92,32),(88,24),(84,22),(81,28),(79,36),(77,44)], '格陵兰', 87, 40)
ax.add_patch(Ellipse((58,24), 8, 5.4, angle=15, facecolor=LAND, edgecolor='#b9b1a0', lw=1))
ax.text(58, 20.3, '哈德逊湾', ha='center', fontsize=10, color=INK, alpha=.85)

# 多塞特先住民居域(浅色带, 早于图勒上千年)
ax.add_patch(MplPoly([(52,44),(75,44),(91,43),(92,35),(72,33.5),(53,33.5)], closed=True,
             facecolor='#e8c9a0', alpha=.28, edgecolor='none'))
ax.text(64, 37.2, '多塞特先住民居域(早于图勒上千年)', ha='center', fontsize=10.5,
        color='#7a5a34', alpha=.95, zorder=4)

# 前图勒区域传统三支(点位仅示意)
for x, y, t in [(22.5,41.5,'Old Bering Sea(OBS)\n(白令海侧)'), (25.5,47.5,'Punuk\n(海峡岛屿)'), (38,48,'Birnirk\n(阿拉斯加北岸)')]:
    ax.plot(x, y, 'o', ms=8, color=INK, zorder=5)
    ax.text(x, y-3.6, t, ha='center', va='top', fontsize=10.5, color=INK, zorder=5)

def arrow(path, color, ls='-', lw=2.6, label=None, lx=0, ly=0, fs=11):
    for a, b in zip(path[:-1], path[1:]):
        ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=16,
                     color=color, lw=lw, linestyle=ls, zorder=6, shrinkA=0, shrinkB=0))
    if label:
        ax.text(lx, ly, label, ha='center', fontsize=fs, color=color, zorder=7, bbox=BOX)

# 弓头鲸活动范围东扩(虚线, 高位错层)
arrow([(38,55.3),(52,55.6),(66,56),(74,56.2)], BLUE, ls=(0,(5,4)), lw=2.4,
      label='弓头鲸活动范围东扩(模型推断)', lx=48, ly=53.8, fs=10.5)
# 通道① 高纬推定通道
arrow([(40,47.5),(52,48),(64,49),(74,51.2),(80,48.5)], ROUTE, lw=3,
      label='通道①  波弗特海→帕里水道→史密斯海峡\n(器物分布支持的推定方向)', lx=58, ly=44.9, fs=9.5)
# 通道② 哈德逊湾西岸南下(自阿拉斯加南缘引出)
arrow([(44,37.5),(50,31),(56.5,27.2)], ROUTE, lw=3, label='通道② 沿哈德逊湾西岸南下', lx=47.5, ly=29.5, fs=9.5)

# 白令海峡: 来回走廊
ax.annotate('', xy=(23.2,44.2), xytext=(27.8,44.2),
            arrowprops=dict(arrowstyle='<|-|>', color=BLUE, lw=1.6))
ax.text(25.5, 50.8, '白令海峡\n"来回走的走廊"', ha='center', fontsize=9.5, color=INK)

# 诺斯垦区
ax.text(84.5, 29, '诺斯人定居区\n(约985年起)', ha='center', fontsize=9.5, color=INK, alpha=.95)
ax.plot(83.5, 31.5, 's', ms=6, color=INK, alpha=.85)

# 标题与注记
ax.text(1.5, 58.8, '图勒东迁路线示意(约公元1000-1300年间)', fontsize=16.5, color=INK, weight='bold')
ax.text(1.5, 56.9, '海岸线与地物高度简化, 不按比例', fontsize=10, color=INK, alpha=.75)
ax.text(1.5, 9.0, '图例: 实线箭头=器物分布支持的推定通道 | 虚线箭头=模型推断 | 浅橙带=多塞特先住民居域(替换发生于此, 各地年代不一) | 浅色椭圆=北极群岛(简化)',
        fontsize=10, color=INK, alpha=.85)
ax.text(1.5, 7.0, '● 前图勒区域传统(点位仅示意, 三者年代互有重叠, 非单线阶梯) | ■ 诺斯人定居区',
        fontsize=10, color=INK, alpha=.85)

plt.savefig('pipeline/staging/img/fig-thule-map', bbox_inches='tight', facecolor=PAPER)
print('fig-thule-map saved')
