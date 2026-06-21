# NovelForge - 智能小说创作辅助系统

## 项目简介
NovelForge 是一套通过智能 Agent 调用 Skills 的全流程小说创作辅助系统，专注于长篇网文创作。

## 核心功能
- **项目目录管理** - 一本书 = 一个项目目录，目录名 = 书名（如 `逆天改命/`）
- **项目初始化** - 一键创建小说项目结构和设定模板（用户确认后创建）
- **大纲规划** - 卷级和章级大纲智能规划，在项目目录内保存
- **章节写作** - 从上下文准备到数据更新的完整写作流程
- **批量写作** - 多章节连续写作，自动管理队列状态
- **质量审查** - 六维质量检查系统 + 去AI味，确保内容质量
- **去AI味** - L1-L4 四层自检，Phase 1-5 全流程润色
- **风格学习** - 从用户作品中学习写作风格和模式
- **信息查询** - 快速查询角色、伏笔、剧情状态
- **扫榜分析** - 分析平台榜单数据和市场趋势
- **作品拆解** - 深度拆解爆款作品的结构与技巧
- **封面生成** - 根据书名题材自动生成封面设计方案
- **作品导入** - 逆向解析已有作品，生成标准项目目录
- **可视化面板** - 项目进度和状态的可视化展示

## 系统架构

### 核心技能 (Skills)
| 命令 | 功能 | 工作目录 |
|------|------|---------|
| `/webnovel-init` | 初始化小说项目（用户确认后创建） | `{书名}/` |
| `/webnovel-plan [卷号]` | 规划卷级大纲和章节安排 | `{书名}/大纲/` |
| `/webnovel-write [章号]` | 写作完整章节 | `{书名}/正文/` |
| `/webnovel-review [范围]` | 六维质量审查 + 去AI味 | `{书名}/审查报告/` |
| `/webnovel-query [关键词]` | 查询角色、伏笔、剧情状态 | `{书名}/.webnovel/` |
| `/webnovel-learn [内容]` | 学习写作模式 | `{书名}/设定集/` |
| `/webnovel-dashboard` | 启动可视化面板 | `{书名}/` |
| `/batch-write [范围]` | 批量写作多章节 | `{书名}/正文/` |
| `/webnovel-scan` | 扫榜分析市场趋势 | 不依赖项目目录 |
| `/webnovel-analyze` | 拆解分析爆款作品 | 有项目目录则从 `{书名}/正文/` 读取 |
| `/webnovel-deslop` | 去除文章AI味（L1-L4 四层自检） | 有项目目录则在 `{书名}/` 内 |
| `/webnovel-cover` | 生成小说封面 | 有项目目录则复用信息 |
| `/webnovel-import` | 导入已有作品续写 | 新建 `{书名}/` 目录 |

### 智能代理 (Agents)
系统包含 19 个专门代理，各司其职：
- **Context Agent** - 构建创作任务书
- **Data Agent** - 提取事实更新状态
- **Reviewer Agent** - 六维质量审查
- **Auto-Validator** - 提交前校验
- **Foreshadow-Manager** - 伏笔管理
- **Emotion-Analyzer** - 情绪分析
- **Style-Learner** - 风格学习
- **Item-Tracker** - 物品追踪
- **Number-Checker** - 数字一致性
- **Knowledge-Boundary** - 知识边界
- **POV-Checker** - 视角检查
- **Relationship-Matrix** - 关系矩阵
- **Character-Growth** - 角色成长
- **Periodic-Health** - 阶段体检
- 等更多代理...

## 支持的题材
系统支持 37 种小说题材，包括：
- 玄幻修仙、都市异能、末世、系统流、高武、西幻、无限流
- 古言、宫斗宅斗、青春甜宠、豪门总裁、职场婚恋、种田
- 悬疑灵异、规则怪谈、克苏鲁、知乎短篇
- 支持最多 2 种题材组合

## 设计理念
### 防幻觉三定律
1. **大纲即法律** - 遵循大纲，不擅自发挥
2. **设定即物理** - 遵守设定，不自相矛盾
3. **发明需识别** - 新实体必须入库管理

### Strand 节奏系统
- **Quest** 主线剧情 60%
- **Fire** 感情线 20%
- **Constellation** 世界观扩展 20%

### 六维质量审查
- High-point / Consistency / Pacing
- OOC / Continuity / Reader-pull

## 快速开始
```bash
# 1. 初始化项目（按书名创建目录，需用户确认后创建）
/webnovel-init

# 2. 规划大纲（在 {书名}/大纲/ 内保存）
/webnovel-plan 1

# 3. 开始写作（在 {书名}/正文/ 内保存章节）
/webnovel-write 1

# 4. 审查章节（报告保存在 {书名}/审查报告/）
/webnovel-review 1-5

# 5. 批量写作（在 {书名}/正文/ 内连续写作多章）
/batch-write 1-20

# 6. 去AI味润色
/webnovel-deslop
```

## 核心规则：一本书 = 一个项目目录

- 每本小说对应一个独立项目目录，目录名 = 小说书名（如 `逆天改命/`、`斗破苍穹/`）
- 所有创作活动（正文、设定、大纲、审查报告）都在该书的项目目录内进行
- 工作目录下可同时存在多本书的项目目录，互不干扰
- 所有创作类命令必须先找到项目目录才能执行，找不到时提示先 init

## 创作项目结构

使用系统创建的小说项目结构如下（目录名 = 书名）：

```
{书名}/                    # 项目根目录，目录名 = 小说书名
├── .webnovel/            # 运行时状态和数据
│   ├── state.json        # 书名、题材、进度、风格设置
│   ├── backups/          # 备份
│   ├── archive/          # 归档
│   └── summaries/        # 章节摘要
├── 设定集/               # 世界观、角色设定等
│   ├── 世界观.md
│   ├── 力量体系.md
│   └── 主角卡.md
├── 大纲/                 # 总纲和卷章大纲
│   └── 总纲.md
├── 正文/                 # 章节内容（第1章-xxx.md）
└── 审查报告/             # 质量审查结果
```

## 技能模块结构

webnovel-writer 核心技能模块的结构如下：

```
NovelForge/
├── README.md              # 项目说明文档
└── webnovel-writer/       # 核心技能模块
    ├── agents/            # 19个智能代理
    │   ├── context-agent.md
    │   ├── data-agent.md
    │   ├── reviewer.md
    │   └── ...
    ├── genres/            # 小说题材配置
    │   ├── xuanhuan/
    │   ├── period-drama/
    │   └── ...
    ├── references/        # 参考文档
    │   ├── review-schema.md
    │   ├── style-dna.md
    │   └── ...
    ├── skills/            # 7个核心技能
    │   ├── webnovel-init/
    │   ├── webnovel-plan/
    │   ├── webnovel-write/
    │   └── ...
    ├── templates/         # 模板文件
    ├── README.md
    └── SKILL.md
```

## 核心组件

### 智能代理 (Agents)
系统包含 19 个专门代理，各司其职：
- **Context Agent** - 构建创作任务书
- **Data Agent** - 提取事实更新状态
- **Reviewer Agent** - 六维质量审查
- **Foreshadow-Manager** - 伏笔管理
- **Emotion-Analyzer** - 情绪分析
- **Style-Learner** - 风格学习
- **Relationship-Matrix** - 关系矩阵
- **Character-Growth** - 角色成长追踪

### 支持题材
- 玄幻修仙、都市异能、末世、系统流、高武、西幻
- 古言、宫斗宅斗、青春甜宠、豪门总裁
- 悬疑灵异、规则怪谈、克苏鲁、知乎短篇

## 更多信息
详细使用说明请查看 [webnovel-writer/README.md](file:///workspace/.trae/skills/webnovel-writer/README.md)