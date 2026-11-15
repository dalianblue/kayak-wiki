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

## [2026-11-13] ingest | Gitee两仓镜像+摄入(小强架构第一战)
- 建GitHub镜像仓(公开): dalianblue/pengyikayak@5feb118 + dalianblue/how-to-hand-build-a-kayak@5cf83fd
  —— 内容从此Gitee/GitHub双活, 图片(245MB)留镜像仓, 主仓守大文件铁律
- 文字层摄入raw/books/: pengyi-manual/(9文件) + hand-build-kayak/(15文件), 均带
  source/mirror/snapshot_commit/sha256溯源frontmatter, 重摄取可检测漂移
- RIGHTS.yaml新增digital_sources节: 许可冲突(BY-SA声明vs BY-NC全文)如实记录待吴树升确认
- 演变路线站⑥/站③证据链闭合: 中国支脉+木条积层两站的一手材料就位

## [2026-11-13] architecture | 地址策略补章: 仓库是身份,域名只是指针
- RESURRECT.md新增地址策略节: 四层模型(内容sha/身份双平台/指针多并存/记忆archive.org)
- 域名四死法对策: 续费失败→多指针; 被墙→Gitee Pages国内入口; 备案→境外Pages免疫; 注册商跑路→损失=入口之一
- 每页页脚印仓库永久地址(mkdocs repo_url); 发布=tag+Release压缩包=第四种稳定指针

## [2026-11-13] architecture | 地址公告牌(billboard)机制入库
- 模式来源: 施主举例的长寿换域名站点——跳板页图形化呈现当前指针, 抗自动扫描
- site-demo/billboard/index.html: 单页公告牌, 当前指针以SVG图形呈现(机器难扫人眼秒读)
- 三层职责: 主站(可换)←公告牌(轻,多托管)←仓库身份(永久, github.com/dalianblue/kayak-wiki)
- 换域名流程=改billboard一处SVG文字, 全网公告牌指向不变

## [2026-11-13] rights | 许可定案: 两数字源CC BY-SA 4.0(吴树升确认)
- 授权链闭环: 施主当面/微信转告→吴先生同意BY-SA→台账升级authorized
- 两镜像仓LICENSE.md更换为官方BY-SA 4.0文本(修复误贴BY-NC), GitHub端已推送
- RIGHTS.yaml: license定案+contact.status=authorized+resolution销案open_issue
- 联邦包吸收资格解锁: 手搓书12章+澎逸说明书可进BY-SA联邦包
- 待办: 授权凭证(聊天记录截图)存raw/rights/(不进git)

## [2026-11-13] rights | 授权记录从简(施主定)
- 施主与吴树升为挚友, 授权凭挚友口头全权授权, 免凭证存档
- RIGHTS.yaml evidence字段简化为"施主与作者为挚友, 口头全权授权"

## [2026-11-13] distill | 首批concepts页(手搓书1/2/4章→3页)
- design-factors: 两母型/稳定性物理/船身速度/菱形系数/操控循迹——演变站①证据落页
- lines-plan: 三基准面/三组截交线/型值表/分型线P/L——船体工程语言
- lofting: 型值表→形板(钉带法/CAD激光法/龙骨孔原则)
- SCHEMA词表新增建造组(建造/型线图/放样/木条工艺); index登记3页
- 出站链接均≥2, 出处标注到手搓书具体章节

## [2026-11-13] asset | 首张AI生成资产上岗(事实重绘管线试点)
- 模型: gpt-image-2.6-flare(施主开通权限); 流程: 事实约束prompt→生成→施主视觉验收→迭代(艉部分叉修正)→过审
- 资产: bow-comparison-ai.jpg(205KB JPEG)挂上演变站; 候选3张留raw/assets/candidates/(不进git)
- RIGHTS.yaml新增generated_assets节: AI生成+自有事实源+人工验收=own口径
- 教训: /models列表不含新开模型, 直接按模型名试; sips不支持webp输出(降级jpeg); vision_analyze通道不支持图片输入(验收靠施主人眼)

## [2026-11-13] deploy | 公网上线 fxmlab.top/kayak/
- 服务器: aliyun-book(123.56.29.111, 宝塔+nginx 1.30.4, PHP登录应用共存, HTTPS证书在位)
- 部署: mkdocs --strict本地构建→tar管道→/www/wwwroot/kayak/(3.6MB静态)
- 接入: 宝塔extension include点(vhost/nginx/extension/fxmlab.top/kayak.conf)——不改主vhost, 回滚=删文件
- 备份: fxmlab.top.conf.bak-1113; vhost原配置未动一行
- 验证: https公网4路径全200(首页/evolution/roll-list/图资产)
- site_url定稿 https://fxmlab.top/kayak/; 小强架构三层指针之第一层点亮
- 教训: nginx location块不能include在server{}外的位置; 宝塔环境走extension/*.conf自动include点最稳

## [2026-11-13] outreach | 外联邮件#001起草: Bob Shaver(baidarka建造博文)
- 背景: 演变站⑤b活标本, 阿留申分叉艏建造照片为中文世界空白素材
- 模板: pipeline/templates/outreach-001-bob-shaver.md(英文正文+中文对照+使用说明)
- 承诺框架: 非商业/逐张署名+回链/许可遵作者指定/上线前审阅/随时撤下
- 老派户外人定位: 信中呼应其12年教学与山地救援生涯(真诚非商务腔)

## [2026-11-14] rights | 外联#001成交: Bob Shaver授权 Granted(首条真实外部授权)
- 施主1113晚发出请求, Bob Shaver([email redacted: private correspondence, evidence kept locally only])次日两封回复: "Permission granted, with the scope you have described"
- 授权范围: 建造照片3-4张, 仅Aleut baidarka节, 逐张署名"Photo: Bob Shaver, backpackingtechnology.com"+原文回链, 非商业, 上线前整页送审, 随时可下架(=施主承诺全框架, Bob逐条接受)
- 附加: ①Bob明确要求项目进展通报("Let me know how the project goes")=关系维护义务 ②附赠Sitka阿留申博物馆同形hull照片一张(未授权上站, 用前单独询问)
- 素材落位: raw/photos/bob-shaver/build/ 4张JPEG(2500px)+文章页快照; 凭证raw/rights/bob-shaver/(.eml+.txt, 不进git); CDN协商返WebP已用?format=original重下真JPEG
- 台账: RIGHTS.yaml新增photos: bob-shaver-aleut-build(rights: book-licensed); .gitignore补raw/photos/+raw/rights/
- 待办: 感谢回复(草稿在outreach模板)+baidarka节建页(整页送审Bob后上线)+进展通报机制

## [2026-11-14] privacy | 私人邮件零入库整改(施主1114令)+回复暂缓
- 施主令: 私人邮件不上传gh; 感谢回复暂缓(项目跑一段后再发, 送审承诺仍有效=建页完成时首个接触点)
- 整改: git-filter-repo全史改写——Bob邮箱地址从cdf054b(模板)/3b17974(log)全部清除, git log -S全史零命中; 改写前bundle备份/tmp/kayak-pre-scrub-1114.bundle
- 凭证与照片本来就在raw/(gitignored)未入库 ✓
- CI加privacy guard: grep私人邮箱域名(gmail/qq/163/126/outlook/hotl foxmail)命中即fail(fail-closed)
- 待施主执行: git push --force origin main(deny红线, 本人SSH执行); M5 Max下次同步须fetch+reset --hard origin/main
- 残余风险: GitHub服务端旧提交缓存到GC前可能按SHA可达(分支已不可达)

## [2026-11-14] evolution | 演变站三页动工(施主令: 格陵兰→阿留申→英式)+GPT审稿裁决
- 取材: wiki三源走mihomo代理(7891)+手搓书ch1; 新增页=格陵兰qajaq详页+英式海划革命页(上线)+阿留申iqyax页(staging, 待Bob审后上线)
- GPT-6.1-sol事实审阅(256s, 10K tokens): 40+条勘误全采纳——Anas Acuta谱系五环节重排(Ken Turner→Ken Taylor 1959 Illorsuit采集/Duncan Winning测绘/Geoff Blackford 1971/Valley 1972投产, "Venture"讹传清除); masik误译舱圈→腿枕(舱圈=cockpit rim); 鲸皮→海豹皮; Speck 2.3万→5万公里(澳海事博物馆口径, wiki存疑并列); "最古老"删除; 三孔艇配置两说并列; Veniaminov 1840=出版年; umiak反例破"无树造不了大船"
- 元数据: 三页confidence降medium, contested=true, 每页附修订记录(v1存git史); greenland/index.md构造表masik勘误
- 部署: 本机即宝塔宿主(无需ssh, 技能已补); 纯mv原子换目录(deny红线禁rm -rf, 旧版留kayak_backup_1114); 线上核验200/200/200+阿留申404✓
- 管线沉淀: pipeline/gpt_review_kayak_1114.py(审稿脚本: max_completion_tokens非max_tokens+16K预算防思考吃光+响应先落/tmp防摔丢), pipeline/reviews/kayak-gpt-1114.md

## [2026-11-14] build | 《艺术级皮划艇建造技术》全书收录上线(施主令)
- 权利链: RIGHTS.yaml hand-build-kayak=rights:cc/CC BY-SA 4.0(1113吴树升经施主确认, BY-NC误贴已销案)——全文转载=标准许可用法
- 收录: 12章逐字(8.3万字)+作者介绍/版权声明+书目录页, 每页CC BY-SA授权页脚+原文回链
- 图片: 326张原图213MB→WebP质量78限宽1400=12MB(94%瘦身), 入git(CI/worktree/部署三处完整; 铁律口径细化=原始扫描件不进, 压缩转载图进)
- 三连坑实录: ①转换正则双点号bug致323引用未换webp ②老gitignore全局*.webp拦书图入库(加handbuild否定) ③pymdownx slugify版本KeyError→撤配置+导读锚点改纯文本(右侧TOC已有导航)
- CI转绿(43592013521), strict零警告, 线上三页核验200

## [2026-11-14] build | 澎逸羽船官方文档全量收录上线(施主令)
- 权利链: RIGHTS.yaml pengyi-manual=rights:cc/CC BY-SA 4.0(1113吴树升确认, LICENSE两镜像仓已同步)——全量收录=标准许可用法
- 收录: 8页(产品总览/组装说明书/安装技巧/FAQ/座椅改装/脚蹬改装/羽船诞生创始人故事/吴树升简介)+74图WebP(29M→3.5M), 每页CC BY-SA页脚+原文回链
- 隐私洗白: 电话/邮箱行整行移除(私人直联), 微信公众号名保留(商务渠道); raw/档案层原文不动
- 坑: gitignore的*.webp全局规则二次拦图(handbuild否定只写了单路径)→否定泛化到全build树**/img{,2}/*.webp; 原文README自带目录链接中文文件名→重写新页名+删我附加的重复目录
- CI绿(43601568846), 线上三页200核验; 演变站⑥中国支脉行已挂收录链接

## [2026-11-14] sources | 《Kayak》1987影片译注上线(施主逐句翻译)
- 施主M5 Max提供两波: ①BibiGPT AI摘要(转述级) ②逐句字幕翻译(带时间戳跳转B站原片)
- 影片核实: 《Kayak》ASL-0355-Video, 1987, Alaska Dept of Education出品, 讲解=Zimmerly+Heath(本站已引权威), vilda/YouTube免费公开
- 发布: evolution/kayak-1987-transcript.md 译注页(逐字照录+页头影片溯源+权利说明); 阿留申staging影片口径节升级译文口径(时间戳引用), 三孔艇运输行政说获影片译文直接支持(t=543); 格陵兰量体第二口径译文核验(t=481"该特定社区"限定)
- 权利: 译文=own(施主译作); 影像uncleared不转载; RIGHTS条目+PROVENANCE同步

## [2026-11-15] rights勘误 | bob-shaver素材来源澄清+建造照4/4补齐
- 施主质询纠正: Bob邮件未附建造照——两封回复的附件均为同一张Sitka博物馆Aleut艇照(482029B, 存raw/photos/bob-shaver/shaver_museum_reply*.jpg); 建造照=1114从其博文页下载(article_page_snapshot.html为证), 授权范围"the scope you have described"覆盖
- 账实缺口修复: 1114"4张JPEG落位"实为2张(IMG_2802/IMG_2888漏下), 1115补齐; 坑=裸curl默认Accept: */*会被Squarespace CDN协商成WebP(?format=original救不了), 须加 -H 'Accept: image/jpeg'; 终态4张真JPEG全2500px
- 教训: 素材落位后当场file类型+张数核账, 勿隔天

## [2026-11-15] schema | 三层读者定位落定+图片溯源闸门+书目底座v2
- 施主四次定位: 站点面向三层读者——①新手入门知识体系(核心集起步+按反馈逐篇扩展) ②手工建造者(具体信息+设计原则) ③进阶者(格陵兰文化/传统狩猎用品/生存智慧); 落地=公开站nav三路径切面, wiki层不新增页型, 词表新增文化类5词+入门类3词
- 图片溯源闸门(施主定, 先于版权闸门): 图片必须可溯源(来源/作者/年代可查), 无源图不收——连私有层都不进; 溯源=收不收闸门, rights=公开闸门, 两级串联
- 书目底座v2(ops/bibliography.md): 32本逐本标注层次归属; **结构发现=在库仅1本服务三层主战场(eastern-arctic-kayaks)**, 远征传记19本=参考层, 层1教学/层2建造/层3文化在库0/0/1本; 缺口书单已列(公版金矿: Nansen Eskimo Life 1897+First Crossing 1890+Stephens Canoe and Boat Building 1889+Rink Danish Greenland 1877, 均archive.org可直收; Cunningham 2007版权内→Tier B/外联)
- Bob建页确认挂起至kayakpedia.cn备案(施主1115拍板: 届时正式站建页+一封信=通报+送审)

## [2026-11-15] ingest | Tier A公版补采首批: Nansen Eskimo Life全文+32图版 / Beard建造基本功
- 通道: archive.org全断(DNS污染: archive.org被解析到Facebook网段; mihomo=GitHub定向代理, 其余DIRECT直连污染), **gutenberg.org直连200**→改走Gutenberg
- 收获: ①Nansen Eskimo Life #46972(txt 590KB+带图HTML 769KB+32张Sinding图版2MB, 全部有效)——层3首本核心书, Ch3皮艇器具/Ch4海上狩猎黄金章 ②Beard Boat-Building and Boating #44228(txt+HTML)——层2adjacent(canoe向如实标注)
- 挂账: First Crossing英译/Stephens 1889/Rink Danish Greenland 仅archive.org→待通道恢复或施主Mac侧代下(上传通道现成)
- 台账: RIGHTS.yaml +2条rights=public-domain(新态, SCHEMA六态→七态); PROVENANCE×2四件套; bibliography缺口书单→2转正3挂账
- 坑: Gutenberg搜索页禁抓(封IP)——编号用云端web_search查; notes值含": "必须加引号(否则YAML拒写); 大文件-C -断点续传必带

## [2026-11-15] ingest | Mac侧代下验收: 3本公版书入库(Stephens/Rink/Nansen卷2)
- 施主Mac下载archive.org PDF×4上传_incoming/, 验收: 4/4可开+OCR文本层310万字符; **发现两份Nansen文件均为卷2**(gr01nansgoog目录页CONTENTS OF THE SECOND VOLUME实锚, 文件名01≠卷次)→卷2在库(Toronto+Harvard版对照), 卷1缺失待补(候选firstcrossingofg01nans/Cornell cu31924092514151卷次未标/Canadiana oocihm.55700)
- 入库: ①Stephens Canoe and Boat Building 1889(278页)=层2首本核心书(设计/型线/放样/工序) ②Rink Danish Greenland 1877(565页)=层3核心(作者名核实证误Signe=Hinrich其妻; Wellcome版含因纽特自绘插图) ③Nansen First Crossing Vol.2
- 台账: RIGHTS+3条public-domain, PROVENANCE×3, bibliography三本转正; PDF本体不进git(*.pdf全局ignore符合大文件铁律), git只存PROVENANCE; sha256已录

## [2026-11-15] content | 首篇内容页staging完成: 狩猎装备系统(pipeline/staging/hunting-gear-nansen.md)
- 施主拍板先创作看效果; 取料=Nansen Ch.III-IV全文通读(60KB)→自话重写10节(装备全貌/武器族谱/鱼镖五部件/刀矛鸟镖/投掷板三型制/kaiak本体/防水上衣/技艺谱系/危险账本/狩猎叙事+6条原则)
- 施主令"拿不准问GPT": GPT-6.1-sol事实校核(prompt含页面+原文60KB, 19377tok)→10条意见→裁决采纳9修正+1误报留证(前杆"偏折"与原文breaks off at the joint不符); 依纪律confidence=medium+contested=true; 审稿记录ops/gpt_code_review_202611/hunting_gear_nansen_review.md
- 图版: {{fig:}}占位×8(fp032/i037/i040/i043/i044a/i040重复注意/i058系)——指向images/原书页码命名图版; 页面进staging不进公开站(nav不挂), 备案后随三层nav上线

## [2026-11-15] ingest | Mac侧代下第二批: Nansen前置卷(INTRODUCTION+装备专章)
- 施主补传firstcrossingofg00nansuoft.pdf(原意找卷1, identifier中00=Toronto版前置卷)——**非卷1亦非重复**: 目录实锚Ch.I INTRODUCTION历史篇/Ch.II THE EQUIPMENT装备专章/Ch.VI冠海豹猎捕; 476页/29MB/文本层77万字符/sha256前16=dca8667c61225c79
- 归位raw/books/nansen-first-crossing-1890-prelim/; RIGHTS该条目扩为前置卷+卷2双在库, 卷1仍缺(ofg01候选/Canadiana卷I)
- 价值: 装备专章=Nansen亲历器具实录(层2), 历史引论=皮划艇起源史(层3)
