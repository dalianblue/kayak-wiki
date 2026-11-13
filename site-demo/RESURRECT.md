# RESURRECT.md — 本站复活指南（打不死的小强架构）

> 如果 fxmlab.top 打不开、原维护者失联——这个仓库就是全部真相。按下面任一路径，10 分钟内复活本站。

## 你需要什么

- 一个 GitHub 账号（免费），或任何能跑 Python 的机器
- 不需要联系任何人、不需要授权（内容 CC BY-SA 4.0，代码 MIT——fork 合法）

## 路径 A：GitHub Pages 一键复活（推荐，零服务器）

1. Fork 本仓库
2. 在你 fork 的仓库里：Settings → Pages → Source 选 **GitHub Actions**
3. Actions 标签页确认 `deploy.yml` 工作流已启用（fork 后默认启用）
4. 等 2-3 分钟，站点出现在 `https://<你的用户名>.github.io/<仓库名>/`
5. （可选）绑自定义域名：Settings → Pages → Custom domain

## 路径 B：本地构建，部署到任意静态托管

```bash
git clone https://github.com/<owner>/<repo>.git
cd <repo>
pip install -r requirements.txt   # mkdocs-material 已锁定版本
mkdocs build --strict             # 产物在 site/，也是本仓 CI 的验收标准
# 把 site/ 扔到任何静态托管: nginx / Netlify / Vercel / 对象存储+CDN ...
```

## 路径 C：镜像站接力

本站常驻镜像：<仓库 Pages URL>——主站失效时镜像继续服务；
镜像也失效时，回到路径 A/B，任何读者都能成为新的宿主。

## 内容许可与出处

- 正文内容：CC BY-SA 4.0——保留署名+回链，即可自由复制/修改/再分发（含商业）
- 管线代码：MIT
- 每页技术条目标注来源（书名/页码或组织名）；书内原图永不出现在本站
- 第三方 CC 资产逐条带许可链标注于 `RIGHTS.yaml`

## 维护者交接（给未来的续命人)

- 内容源=本仓 `docs/`（mkdocs）；构建配置=`mkdocs.yml`；CI=`.github/workflows/deploy.yml`
- 私有研究库（书籍切片、RIGHTS 台账全量）不在本仓——联系维护者获取，或按公开层内容继续独立运营
- 改完内容 push 即自动构建部署；`mkdocs build --strict` 本地先跑一遍防断链
- 新增资产纪律：SVG/WebP，单文件 ≤500KB，必须进 git

## 本架构的原则（为什么它打不死）

公开仓=唯一事实源；网站只是构建产物。产物可丢，源不可丢。
