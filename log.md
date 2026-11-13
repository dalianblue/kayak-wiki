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

## [2026-11-13] decision | 联邦分发构想入ROADMAP(施主提"让别人也部署")
- 前提链: 分发物=可公开授权内容(公开层自话重写+自绘/CC资产, 书图永不出墙)→内容许可CC BY-SA 4.0(待施主正式确认)
- 双仓制: 私有内核仓+公开仓(白名单单向导出); 分发枢纽=GitHub(本服务器零负担); 论坛遗产节不进联邦包

## [2026-11-13] reframe | 定位重构: 教学图示→历史与经验档案(施主定"动作准确性非重点, 记录历史和经验")
- SCHEMA: Domain改"历史与经验档案"; 词表加经验记录组; 新增trips/划行日志页规范(EXIF归档+自动挂潮汐/水位/天气)
- ROADMAP: 划行日志管线升公开层主力(自有照片+自有文字, 版权几乎自动干净); 书切片退参考层; 联邦包含trips/

## [2026-11-13] design | 版权升为一等元数据(施主定:版权决定公开形式)
- SCHEMA加Rights节: 六态状态机(own/cc/book-licensed/book-orphan/book-uncleared/unknown)→公开形式自动推导, unknown缺字段=按私有处理(fail-closed)
- RIGHTS.yaml机器可读授权台账随管线建立; 卡片schema加rights字段; 构建期许可链校验
- 法理依据: 出版社倒闭不影响作者版权; 书内照片可能独立属于摄影师; 孤儿作品风险趋零非无主

## [2026-11-13] decision | 内容二次定位: 垂直两主线(施主定)
- 主线①皮划艇技术演变路线展示: qajaq→折叠艇→英国海划革命→现代艇→格陵兰复兴→中国支脉
- 主线②格陵兰皮划艇历史与技巧推广: 狩猎文化/构造/滚法体系/当代复兴
- SCHEMA Domain与边界改写; ROADMAP决策记录追加; Eastern Arctic Kayaks升全库中心书
- demo站同步: 新增evolution/+greenland/板块, 移除泛知识库; 演变表标出"英国革命站待补书源"

## [2026-11-13] architecture | 打不死的小强架构定盘(施主定: 网站会死,git+许可不会)
- ROADMAP新增架构原则节: 公开仓=唯一事实源/一键复活/双活镜像/构建即验证(strict)/
  许可即永生(CC BY-SA+MIT)/域名解耦/资产体积纪律/发布=tag/(远期)archive.org三级冗余
- site-demo/RESURRECT.md=复活指南(路径A fork+Pages零服务器/B本地构建任意托管/C镜像接力)
- .github/workflows/deploy.yml=CI(push即构建部署, strict验收)
- 死亡演习通过: mkdocs build --strict抓出roll-list两处断链→修复→全绿
- 演变路线补站⑤b北美西海岸复兴(Harvey Golden/Cape Falcon, 施主点出最精华在加拿大西海岸)
