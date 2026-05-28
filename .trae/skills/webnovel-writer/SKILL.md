---
name: "webnovel-writer"
description: "长篇网文创作技能，支持扫榜分析、拆解学习、大纲规划、章节写作、质量审查、去AI味、封面生成、故事导入等全流程功能。**当用户想要创建新小说项目、规划章节大纲、写作小说章节、审查章节质量、扫榜分析、拆解分析、去AI味、生成封面、导入作品时使用此技能。在用户提到'写小说'、'网文'、'创作'、'章节'、'大纲'、'伏笔'、'审查'、'批量写作'、'风格学习'、'人物成长'、'世界观'、'追读力'、'扫榜'、'拆解'、'去AI味'、'封面'、'导入'等关键词时也应触发此技能。**"
---

# Webnovel Writer - 网文创作系统

## 系统架构

```
┌─────────────────────────────────────────────────────────────────────┐
│                          SOLO Assistant                             │
├─────────────────────────────────────────────────────────────────────┤
│  Skills (13个):                                                     │
│    webnovel-init / webnovel-plan / webnovel-write / webnovel-review │
│    webnovel-query / webnovel-learn / webnovel-dashboard             │
│    batch-write (批量写作)                                           │
│    webnovel-scan (扫榜) / webnovel-analyze (拆解分析)               │
│    webnovel-deslop (去AI味) / webnovel-cover (封面生成)             │
│    webnovel-import (故事导入)                                       │
├─────────────────────────────────────────────────────────────────────┤
│  Agents (19个):                                                      │
│    Context Agent / Data Agent / Reviewer / Deconstruction           │
│    Auto-Validator (提交前校验) / Foreshadow-Manager (伏笔管理)     │
│    Regression-Tester (回归测试) / Emotion-Analyzer (情绪分析)         │
│    Style-Learner (风格学习) / Batch-Writer (批量写作)               │
│    Item-Tracker / Number-Checker / Knowledge-Boundary                │
│    POV-Checker / Relationship-Matrix (势力关系)                      │
│    Memory-Pack (精简记忆包) / Character-Growth (成长追踪)            │
│    Periodic-Health (阶段体检) / Volume-Foreshadow (卷级伏笔)         │
├─────────────────────────────────────────────────────────────────────┤
│  Data Layer:                                                         │
│    .webnovel/state.json / index.db / memory                          │
│    foreshadow_tracker.json / style_dna.json / queue_state.json       │
│    items.json / numbers.json / knowledge.json / relationships.json    │
│    character_growth.json / memory_packs/                            │
│    拆文库/ (扫榜数据、拆解分析)                                      │
├─────────────────────────────────────────────────────────────────────┤
│  References:                                                         │
│    genre-profiles.md / reading-power-taxonomy.md / review-schema.md  │
│    physics-rules.md (物理法则追踪) / style-dna.md (风格基线)         │
│    auto-review-workflow.md (自动审核评分)                            │
│    banned-words.md (AI味检测) / anti-ai-writing.md (去AI方法)        │
│    cover-styles.md (封面风格) / market-trends.md (市场趋势)          │
└─────────────────────────────────────────────────────────────────────┘
```

### 自动化流水线

```
写作请求 → Context Agent → 起草 → Auto-Validator → Regression-Tester
                                              ↓
Foreshadow-Manager ← Data Agent → Emotion-Analyzer → Style-Learner
       ↓                    ↓                    ↓
Item-Tracker      Number-Checker    Knowledge-Boundary
       ↓                    ↓                    ↓
Relationship-Matrix     POV-Checker    Physics-Rules
                                              ↓
                                    自动审核评分 ⚠️
                                              ↓
                                    通过 → 提交/下一章
                                    失败 → 打回优化
```

## 完整创作流水线

```
┌─────────────────────────────────────────────────────────────────────┐
│                          创作流程总览                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. 扫榜分析 → 2. 拆解学习 → 3. 项目初始化 → 4. 大纲规划          │
│         ↓                ↓                ↓                ↓         │
│  webnovel-scan    webnovel-analyze   webnovel-init    webnovel-plan │
│                                                                     │
│  5. 章节写作 → 6. 质量审查 → 7. AI味检测 → 8. 封面设计            │
│         ↓                ↓                ↓                ↓         │
│  webnovel-write  webnovel-review    webnovel-deslop  webnovel-cover │
│                                                                     │
│  9. 作品导入 ←───────────────────────────────────────── 10. 批量写作 │
│  webnovel-import                                            batch-write │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 各功能模块说明

#### 扫榜模块（webnovel-scan）
- 分析起点、番茄、晋江等平台排行榜
- 提炼市场趋势与热门题材
- 提取读者画像
- 输出扫榜报告

#### 拆解模块（webnovel-analyze）
- 深度拆解爆款作品
- 分析黄金三章结构
- 提取人设、爽点、节奏模式
- 生成文风分析报告

#### 去AI味模块（webnovel-deslop）
- 检测文本AI味等级
- 6 Gate 系统性去AI
- 保护创作意图
- 输出润色报告

#### 封面生成模块（webnovel-cover）
- 分析书名题材
- 设计封面视觉风格
- 生成封面设计方案
- 提供各平台尺寸规范

#### 故事导入模块（webnovel-import）
- 逆向解析已有作品
- 生成标准项目结构
- 自动识别角色、伏笔、时间线
- 无缝衔接续写流程

## 什么时候使用这个技能

**此技能专为网文创作场景设计。**

使用此技能的时机：
- 用户想要创建新的小说项目
- 用户想要规划小说大纲（卷大纲、章大纲）
- 用户想要写作小说章节
- 用户想要审查已有章节的质量
- 用户想要查询角色、伏笔、剧情状态
- 用户想要从参考书学习创作模式
- 用户想要查看项目可视化面板
- 用户想要扫榜分析市场趋势
- 用户想要拆解分析爆款作品
- 用户想要去除文章AI味
- 用户想要生成小说封面
- 用户想要导入已有作品续写

## 核心命令

| 命令 | 功能 |
|------|------|
| `/webnovel-init` | 初始化小说项目，创建项目结构 |
| `/webnovel-plan [卷号]` | 规划卷级大纲和章节安排 |
| `/webnovel-write [章号]` | 写作完整章节（带自动审核评分） |
| `/webnovel-review [范围]` | 六维质量审查 |
| `/webnovel-query [关键词]` | 查询角色、伏笔、剧情状态 |
| `/webnovel-learn [内容]` | 从会话中提取写作模式 |
| `/webnovel-dashboard` | 启动可视化面板 |
| `/webnovel-scan` | 扫榜分析市场趋势 |
| `/webnovel-analyze` | 拆解分析爆款作品 |
| `/webnovel-deslop` | 去除文章AI味 |
| `/webnovel-cover` | 生成小说封面 |
| `/webnovel-import` | 导入已有作品续写 |

## Agent 分工

### Context Agent（读）
文件：`agents/context-agent.md`
职责：在写作前构建"创作任务书"，提供本章上下文、约束和追读力策略。

### Data Agent（写）
文件：`agents/data-agent.md`
职责：从正文提取事实，生成 commit artifacts，更新状态和记忆。

### Reviewer Agent（审）
文件：`agents/reviewer.md`
职责：六维质量审查，检查一致性、连贯性、AI味等。

### Deconstruction Agent（拆）
文件：`agents/deconstruction-agent.md`
职责：拆解参考书，提取可迁移的创作模式。

## 防幻觉三定律

| 定律 | 说明 | 执行方式 |
|------|------|----------|
| 大纲即法律 | 遵循大纲，不擅自发挥 | Context Agent 强制加载章节大纲 |
| 设定即物理 | 遵守设定，不自相矛盾 | Reviewer 内置一致性审查 |
| 发明需识别 | 新实体必须入库管理 | Data Agent 自动提取并消歧 |

## Strand 节奏系统

| Strand | 含义 | 理想占比 |
|--------|------|----------|
| Quest | 主线剧情 | 60% |
| Fire | 感情线 | 20% |
| Constellation | 世界观扩展 | 20% |

**节奏红线：**
- Quest 连续不超过 5 章
- Fire 断档不超过 10 章
- Constellation 断档不超过 15 章

## 六维审查 + 逻辑防御

| 维度 | 检查重点 | 防御Agent |
|------|----------|-----------|
| High-point | 爽点密度与质量 | - |
| Consistency | 设定一致性 | Item-Tracker, Physics-Rules |
| Pacing | Strand 比例与断档 | - |
| OOC | 人物行为是否偏离人设 | Relationship-Matrix, Character-Growth |
| Continuity | 场景与叙事连贯性 | Number-Checker |
| Reader-pull | 钩子强度、期待管理 | Foreshadow-Manager |
| Knowledge | 知识边界 | Knowledge-Boundary |
| POV | 视角一致性 | POV-Checker |
| Style | 风格漂移 | Periodic-Health, Style-DNA |

## 记忆中台系统

借鉴 novel-creation 的五层记忆架构，实现长期防漂移：

### 五层记忆结构

| 层级 | 内容 | 存储文件 |
|------|------|----------|
| L1 风格DNA | 写法和语感基线 | `style_dna.json` |
| L2 人物层 | 角色设定、成长轨迹 | `character_growth.json` |
| L3 剧情层 | 主线、因果、时间线 | `state.json` |
| L4 上下文层 | 章节状态、伏笔、未解问题 | `foreshadow_tracker.json` |
| L5 历史层 | 章节摘要、决策记录 | `summaries/` |

### 精简记忆包

| 包类型 | 内容 | 适用场景 |
|--------|------|----------|
| 轻量包 | 章节目标+1个伏笔+角色状态 | 日常续写 |
| 标准包 | +前3章摘要+活跃人物 | 大纲推进 |
| 完整包 | +设定上下文+风格DNA | 重大转折 |

### 阶段性校准

- 每10章触发"阶段体检"
- 检测风格漂移趋势
- 伏笔回收率统计
- 人物弧线进度

## 逻辑防御系统（防止剧情漏洞）

为防止长篇创作中的逻辑漏洞，新增以下防护层：

### 高优先级检查

| Agent | 文件 | 检查内容 |
|-------|------|----------|
| Item-Tracker | `agents/item-tracker.md` | 物品流转：获取→使用→转移→销毁全程追踪 |
| Number-Checker | `agents/number-consistency-checker.md` | 数字一致：年龄/时间/货币/数量校验 |
| Knowledge-Boundary | `agents/knowledge-boundary-checker.md` | 知识边界：角色只知应知之事 |

### 中优先级检查

| Agent | 文件 | 检查内容 |
|-------|------|----------|
| Relationship-Matrix | `agents/relationship-matrix-tracker.md` | 势力关系：态度转变需铺垫 |
| POV-Checker | `agents/pov-leak-checker.md` | 视角检查：限视角不泄漏 |

### 物理法则追踪

文件：`references/physics-rules.md`

| 法则类型 | 检查项 |
|----------|--------|
| 境界法则 | 低境界不能做高境界专属行为 |
| 能量法则 | 灵力消耗有来源，恢复有速率 |
| 空间法则 | 传送/储物有边界限制 |
| 时间法则 | 突破耗时合理，时间线顺序 |
| 因果法则 | 获得必有代价，信息传播有媒介 |

## 项目初始化流程

### `/webnovel-init` 引导信息

创建新小说项目时，引导用户填写：

- **书名**：小说的名称
- **题材**：从以下题材中选择或组合（最多2个）
  - 玄幻修仙、都市异能、末世、系统流、高武、西幻、无限流
  - 古言、宫斗宅斗、青春甜宠、豪门总裁、职场婚恋、种田
  - 悬疑灵异、规则怪谈、克苏鲁、知乎短篇
- **主角信息**：姓名、性格特点、背景
- **金手指/特殊能力**：主角的特殊优势
- **核心冲突**：故事的主要矛盾
- **目标字数**：默认200万字
- **目标章节数**：默认600章

### 初始化产出

```
小说项目/
├── .webnovel/
│   ├── state.json（运行时状态）
│   ├── backups/（备份）
│   ├── archive/（归档）
│   └── summaries/（章节摘要）
├── 设定集/
│   ├── 世界观.md
│   ├── 力量体系.md
│   ├── 主角卡.md
│   ├── 女主卡.md（可选）
│   ├── 主角组.md（可选）
│   └── 反派设计.md
├── 大纲/
│   └── 总纲.md
├── 正文/
└── 审查报告/
```

## 写作流程（带自动审核评分）

### `/webnovel-write` 完整流程

#### Phase 1: 写前准备（Context Agent）
1. 读取 MASTER_SETTING.json、大纲、已有章节
2. 查询角色状态、伏笔、世界规则
3. 生成五段式写作任务书

#### Phase 2: 起草正文
1. 按照任务书写作
2. 遵守防幻觉三定律
3. 应用 Strand 节奏控制

#### Phase 3: 质量审查（Reviewer）
1. 执行六维审查
2. AI味检测
3. 设定一致性检查
4. 输出结构化问题清单

#### Phase 4: 自动审核评分 ⚠️【自动执行】

**自动评分维度：**

| 维度 | 权重 | 通过阈值 |
|------|------|----------|
| High-point | 20% | >= 15/20 |
| Consistency | 20% | >= 15/20 |
| Pacing | 15% | >= 11/15 |
| OOC | 15% | >= 12/15 |
| Continuity | 15% | >= 11/15 |
| Reader-pull | 15% | >= 11/15 |

**评分等级：**
- **优秀（90-100）**：✅ 直接通过
- **良好（75-89）**：✅ 通过
- **合格（60-74）**：⚠️ 通过，需注意问题
- **不合格（<60）**：❌ 打回优化

**通过条件（必须同时满足）：**
1. 总分 >= 75
2. 无 critical 级别问题
3. 高优先级问题 <= 3个
4. AI味检测通过
5. 字数在目标范围内

**审核结果：**

✅ **通过时：**
- 自动保存到正式目录
- 更新 state.json
- 生成评估报告

❌ **打回时：**
- 生成详细问题清单
- 提供修改建议
- 标记为待优化状态
- 等待修复后重新提交

**参考资料：** `references/auto-review-workflow.md`

#### Phase 5: 润色修改
1. 根据审查意见修改
2. 保持角色一致性
3. 优化节奏和爽点
4. 修复审核发现的问题

#### Phase 6: 数据更新（Data Agent）
1. 提取实体和状态变更
2. 生成章节摘要
3. 更新伏笔追踪
4. 保存最终版本

## 题材配置

参考：`references/genre-profiles.md`

### 支持的题材

**玄幻修仙类**：修仙、系统流、高武、西幻、无限流、末世、科幻

**都市现代类**：都市异能、都市日常、都市脑洞、现实题材、电竞、直播文

**言情类**：古言、宫斗宅斗、青春甜宠、豪门总裁、职场婚恋、民国言情、幻想言情、现言脑洞、女频悬疑、种田、年代

**其他题材**：规则怪谈、悬疑脑洞、悬疑灵异、克苏鲁、狗血言情、替身文、知乎短篇

### 题材组合

用 `+` 连接两个题材（主辅比例建议 7:3）：
- 玄幻+系统流
- 都市异能+规则怪谈
- 古言+宫斗宅斗

## 写作风格指南

### 中文网文风格

- **开篇钩子**：前三章必须有强吸引力
- **节奏明快**：避免冗长铺垫
- **情绪张力**：善用爽点、燃点、虐点
- **对话自然**：推进剧情而非堆砌
- **打斗描写**：简洁有力，突出关键动作
- **心理描写**：适度，点到为止

### Anti-AI 对抗

- 删除段末感悟句，留余味
- 删除万能副词（缓缓/淡淡/微微）
- 情绪用生理反应+微动作
- 对话带潜台词和意图冲突
- 制造节奏疏密对比
- 章末禁止安全着陆

## 参考资料

- `references/genre-profiles.md` - 37种题材画像
- `references/reading-power-taxonomy.md` - 追读力学
- `references/review-schema.md` - 审查规范
- `references/auto-review-workflow.md` - 自动审核评分工作流 ⚠️
- `references/grading-standards.md` - 质量评分标准
- `genres/` - 13个详细题材配置目录

## 注意事项

- 始终使用中文回复和写作
- 章节内容要有实质进展
- 保持前后设定一致
- 合理安排爽点分布
- 留有悬念吸引追读
- ⚠️ **所有章节必须通过自动审核评分才能提交**

## 边界条件处理

### 异常场景处理

| 场景 | 触发条件 | 处理动作 |
|------|----------|----------|
| 网络故障 | API调用失败 | 重试3次，失败则暂停并通知用户 |
| 文件损坏 | 章节文件读取失败 | 提示用户检查文件，提供恢复建议 |
| 资源不足 | 内存/存储不足 | 清理缓存，提示用户释放空间 |
| 用户中断 | 用户中途取消 | 保存当前进度，支持恢复 |
| 版本冲突 | Git冲突 | 提示用户手动解决或自动合并 |
| **审核不通过** | 评分 < 75 或存在阻断问题 | 标记为待优化，等待用户修复 |

### 中断恢复机制

1. **自动保存**：每5分钟自动保存写作进度
2. **断点续写**：支持从中断处继续写作
3. **版本回滚**：支持恢复到历史版本
4. **冲突解决**：自动检测并提示版本冲突
5. **审核失败**：保存审核报告，支持从问题点继续优化

## 检查点设计

### 用户确认检查点

| 检查点 | 触发时机 | 确认内容 |
|--------|----------|----------|
| 项目初始化 | 创建新项目前 | 确认书名、题材、主角信息 |
| 大纲规划 | 保存大纲前 | 确认卷章结构、关键节点 |
| 批量写作 | 启动批量任务前 | 确认章节范围、自动处理选项 |
| 质量审查 | 修改章节前 | 确认是否应用审查建议 |
| 风格切换 | 切换写作风格前 | 确认风格变更影响 |
| **审核失败** | 章节未通过审核时 | 确认修复方案 |

### 撤销机制

- **单步撤销**：支持撤销上一步操作
- **历史记录**：保留最近10次修改记录
- **版本对比**：支持查看修改前后对比
- **审核回退**：支持回退到审核前的版本

## 安全边界

- **文件操作**：仅允许修改项目目录内文件
- **权限控制**：不允许访问系统敏感目录
- **数据保护**：自动备份重要文件
- **异常退出**：自动保存状态，防止数据丢失
- **审核机制**：未通过审核的章节不允许提交
