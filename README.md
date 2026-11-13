# kayak-wiki — 皮划艇知识沉淀库

> 背景：皮划艇论坛基本消失，长内容知识无家可归。本项目把藏书（多本皮划艇书籍）与幸存论坛遗产
> 沉淀为**自有的、永久的、可交叉对照的**知识库。技术栈 = Karpathy LLM-wiki 内核（llm-wiki 技能规范）
> + mkdocs 公开壳（规划中）。

## 两层架构与版权口径（1113 施主拍板）

```
私有层（本仓库，不公开）              公开层（规划：fxmlab.top/kayak/）
├─ raw/books/   书切片卡片+出处页码    └─ concepts/ comparisons/ 导出
├─ raw/assets/  书图 WebP（不进git）     只导自写正文 + 自绘示意/公开资产
└─ 内部检索/查询                    书图一律不出墙；知识用自话重写+标注出处
```

**版权口径**：版权保护表达、不保护知识。书图与原文表达只存私有层；公开层一律自话重写
+ 标注参考出处（书名/页码）。公开与否、何时公开，由施主拍板。

## 目录结构（llm-wiki 三层规范）

| 目录 | 用途 | 进git |
|---|---|---|
| `SCHEMA.md` | 域约定+词表(taxonomy)+页面阈值 | ✅ |
| `raw/books/` | 书的切片卡片（文本md，含图路径引用） | ✅ |
| `raw/assets/` | 书图 WebP/PDF原件 | ❌ .gitignore（大文件不进git铁律） |
| `concepts/` | 技术条目（公开层候选） | ✅ |
| `comparisons/` | 多书交叉对照（本项目增量价值核心） | ✅ |
| `entities/` | 装备/船型/河流/组织 | ✅ |
| `queries/` | 值得留档的查询结果 | ✅ |
| `pipeline/` | 切图/入库/蒸馏脚本（后续建设） | ✅ |

## 运转模式

- 施主：管源（给书/指方向）+ 验收条目质量 + 拍板公开节奏
- agent：切图入库、按 SCHEMA 蒸馏建页、交叉引用、矛盾标记（contested）、lint 健康检查
- 每会话开工先读 SCHEMA.md + index.md + log.md 近段（llm-wiki 规范），防重复建页

## 关联

- 展示层（规划）：fxmlab.top/kayak/（mkdocs-material，只出公开层）
- 服务器容量结论：5Mbps PayByTraffic 实测口径下 10000 查询/日无压力（1113 API实查，见 ops/README）
