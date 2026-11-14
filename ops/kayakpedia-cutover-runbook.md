# kayakpedia.cn 切换手册（备案号下来后执行，30分钟级）

> 域名：kayakpedia.cn（施主 2026-11-14 购入，用于皮划艇知识库独立站）
> 硬纪律：备案期间禁解析（cn-icp-beian 技能）——A 记录必须在备案号下发后才加。
> 预备已就位：`/www/server/panel/vhost/nginx/kayakpedia.cn.conf.pending`（未启用，root 指向独立目录 `/www/wwwroot/kayakpedia`）。

## 备案流程（施主操作，agent 可协助填表）
1. 域名实名认证（须与备案主体一致；新域名实名信息入库约 3 天才能提交备案）
2. ECS 控制台申请备案服务码（每台限额 5 个）
3. beian.aliyun.com → 新增网站（已有主体 fxmlab.top，免重新实名核验）→ 填 kayakpedia.cn + 网站名称 → APP 人脸核验
4. 阿里云初审会打电话，务必接听；管局 5~13 天
5. **网站名称口径**：个人备案避免"博客/论坛/社区"等交互词；建议「皮划艇知识笔记」或「皮划艇知识库」类描述性名称，与上线内容大体相符

## 切换清单（备案号短信到达后，agent 执行）
- [ ] DNS：阿里云解析控制台加 A 记录 `@` 与 `www` → 本机公网 IP
- [ ] 内容：`rsync -a --delete site-demo/site/ /www/wwwroot/kayakpedia/`（独立 root，与现有站隔离）
- [ ] vhost：`mv kayakpedia.cn.conf.pending kayakpedia.cn.conf` → `nginx -t` → reload
- [ ] SSL：宝塔为 kayakpedia.cn 签发 Let's Encrypt 证书（自动补 443 段）
- [ ] mkdocs.yml：`site_url` 改 `https://kayakpedia.cn` + `copyright` 挂备案号并链接工信部（法律要求）→ 重建 → rsync 到新 root
- [ ] 核验：curl 逐页 200 + 首页含备案号链接；`fxmlab.top/kayak/` 加 301 跳新域（过渡期保留）
- [ ] 指针更新：RESURRECT.md 域名指针 = kayakpedia.cn（小强架构：仓库=身份/域名=指针）
- [ ] 本 runbook 勾销 + log.md 记录

## 回滚
- 新域异常：mv conf 回 .pending + reload + DNS 暂停解析；fxmlab.top/kayak/ 子路径站不受影响（root 独立）
