# 皮划艇知识库 Log

> 全部动作按时间追加。格式：`## [YYYY-MM-DD] 动作 | 对象`。超500条轮转 log-YYYY.md。

## [2026-11-13] create | 仓库初始化
- 立项：皮划艇知识沉淀（背景=论坛消失，藏书多本可交叉对照）
- 技术栈拍板：LLM-wiki 内核 + mkdocs 公开壳（规划）
- 版权口径拍板：书图与原文只存私有层；公开层自话重写+出处
- 建立 SCHEMA/index/log 三层骨架 + ROADMAP.md（Phase 0~5）
- 待办：书形态确认（电子版/扫描）→ Phase 1 切图管线

## [2026-11-13] external-review | 方案GPT评审(10题)+裁决并入ROADMAP
- 输入: docs/tech-plan.md + 10题编号清单(gpt-6.1-sol, finish=stop, 3406tok)
- 结果: 4同意(Q2/Q3/Q6/Q8) + 6部分同意(Q1/Q4/Q5/Q7/Q9/Q10), 0反对
- 已并入ROADMAP: 切割双轨对测/图组有序子图列表/VLM100组冒烟/数据契约(重跑不覆盖人工)/白名单发布模式/tags主索引(trigram两字盲点)/单书重要页豁免阈值/原PDF异地备份/救援类人工复核
- 报告: ops/gpt_code_review_202611/kayak_plan_review.md
