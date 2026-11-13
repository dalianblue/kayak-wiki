# 皮划艇知识库 Schema（llm-wiki 规范定制版 v1）

## Domain

皮划艇（海洋舟/激流艇/旅行舟）技术、安全、装备与航线知识。来源=多本藏书（切片卡片）+
幸存论坛遗产（待抢救）+施主实践验证。核心增量=**多书交叉对照**（单本书与论坛帖都不具备）。

## Conventions

- 文件名：小写连字符（`sweep-stroke.md`、` Eskimo-roll.md`→`eskimo-roll.md`）
- 每页 YAML frontmatter 必填：title/created/updated/type/tags/sources
- 每页 ≥2 条出站 `[[wikilinks]]`（孤儿页是缺陷）
- 更新必 bump `updated`；新页必进 index.md；每个动作必追加 log.md
- 出处标注：综合 3+ 源的段落尾挂 `^[raw/books/<书slug>.md#p<页码>]`；多书分歧段落
  必须并列并写明"书A pX vs 书B pY"
- 公开候选页（concepts/comparisons）**禁止内嵌书图**，图位用`{{fig:图组id}}`占位符——
  公开构建时替换为自绘示意或公开资产，私有构建时替换为真实图
- 施主实践验证回填：条目加 `**实测**:` 段，标注日期与水域（桐洲岛/富春江为准）

## Frontmatter 模板

```yaml
---
title: 爱斯基摩翻滚（Eskimo Roll）
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept            # concept | comparison | entity | query
tags: [翻滚, 安全救援]    # 只能取自下方词表
sources: [raw/books/<书slug>.md]
confidence: high|medium|low
contested: false         # 多书分歧=true，并在 contradictions 互指
contradictions: []
---
```

## Tag 词表（新 tag 先进这里再用）

- 划法：基础划法, 前进, 后退, 侧移, 摆渡, 横渡, 修正划
- 进阶：翻滚, 支撑, 复位, 滚水舟
- 安全救援：T救援, 自救, 伙伴救援, 信号, 风浪判断, 装备脱困
- 读水：河流读水, 潮汐, 流速, 障碍物, 主流线
- 装备：船型, 桨, PFD救生衣, 裙, 尾舵, 服装, 维护
- 环境：桐洲岛, 富春江, 海划, 激流
- 元：对照, 争议, 实测, 论坛遗产

## 页面阈值

- 一个技术出现在 **2+ 本书** → 建 concept 页 +（如有分歧）comparison 页
- 单书孤例且非核心 → 留在 raw 卡片，不建页
- 页超 ~200 行 → 拆子主题页 + 交叉链接
- 装备/船型/河流 → entities 页

## Comparison 页规范（本项目核心增量）

```markdown
# <技术> —— 多书对照
| 维度 | 《书A》p12 | 《书B》p45 | 实测 |
|---|---|---|---|
| 桨叶角度 | 45° | 掠水角 | 待验证 |
| 常见错误 | ... | ... | ... |
**综合**：两书一致的部分写共识；分歧写各自适用条件（船型/水况）
**实测**：施主下水验证后回填
```

## 公开层边界（版权口径，1113 施主拍板）

- raw/ 与书图 = 私有，**永不**出现在公开构建
- concepts/comparisons = 公开候选：正文必须自话重写；`{{fig:}}` 占位符在公开构建时替换
- 公开与否、何时公开，由施主拍板；构建脚本（Phase 4）强制执行边界，不靠自觉
