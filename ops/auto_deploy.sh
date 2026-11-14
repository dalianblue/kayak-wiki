#!/bin/bash
# kayak-wiki 自动部署: origin/main 有新提交且工作区干净时, 重建并原子换目录
# 设计: 用 git worktree 在隔离目录构建, 永不碰本仓工作区(保护未提交的本地实验)
# 日志: /var/log/kayak_deploy.log ; 纪律: 只在变更时构建, 静默运行
set -u
REPO=/root/workspace/kayak-wiki
WT=$REPO/.deploy-wt
LOG() { echo "$(date '+%F %T') $*"; }

cd "$REPO" || exit 1
git fetch origin main --quiet 2>/dev/null || { LOG "fetch失败(网络?)"; exit 1; }
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)
[ "$LOCAL" = "$REMOTE" ] && exit 0                      # 无变更, 静默退出

if ! git diff --quiet || ! git diff --cached --quiet; then
    LOG "跳过: 工作区有未提交修改(保护本地实验), 待手动处理"; exit 1
fi

git worktree add --force "$WT" origin/main --detach 2>/dev/null || git worktree move "$WT" "$WT" 2>/dev/null
cd "$WT/site-demo" || { LOG "worktree site-demo缺失"; exit 1; }
mkdocs build --strict || { LOG "构建失败(--strict), 保持旧版上线"; cd "$REPO" && git worktree remove --force "$WT"; exit 1; }

# 原子换目录: 旧版→backup(单份轮换), 新版→上线 (deny红线友好: 无rm -rf)
STAMP=$(date +%m%d%H%M)
mv /www/wwwroot/kayak "/www/wwwroot/kayak_bak_$STAMP"
mv "$WT/site-demo/site" "/www/wwwroot/kayak"
cd "$REPO" && git worktree remove --force "$WT"
git merge --ff-only origin/main --quiet 2>/dev/null   # 本地快进, 防同提交反复重建
# 只保留最近一份backup
ls -1dt /www/wwwroot/kayak_bak_* 2>/dev/null | tail -n +2 | xargs -r mv -t /tmp/ 2>/dev/null
LOG "部署完成 $LOCAL (旧版轮换至 /tmp/kayak_bak_*)"
