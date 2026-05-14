# NovelForge - 智能小说创作辅助系统

## 项目简介
NovelForge 是一套通过智能 Agent 调用 Skills 的全流程小说创作辅助系统，专注于长篇网文创作。

## 核心功能
- **项目初始化** - 一键创建小说项目结构和设定模板
- **大纲规划** - 卷级和章级大纲智能规划
- **章节写作** - 从上下文准备到数据更新的完整写作流程
- **质量审查** - 六维质量检查系统，确保内容质量
- **风格学习** - 从用户作品中学习写作风格和模式
- **信息查询** - 快速查询角色、伏笔、剧情状态
- **可视化面板** - 项目进度和状态的可视化展示

## 系统架构

### 核心技能 (Skills)
| 命令 | 功能 |
|------|------|
| `/webnovel-init` | 初始化小说项目 |
| `/webnovel-plan [卷号]` | 规划卷级大纲 |
| `/webnovel-write [章号]` | 写作完整章节 |
| `/webnovel-review [范围]` | 质量审查 |
| `/webnovel-query [关键词]` | 查询信息 |
| `/webnovel-learn [内容]` | 学习写作模式 |
| `/webnovel-dashboard` | 可视化面板 |

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
# 1. 初始化项目
/webnovel-init

# 2. 规划大纲
/webnovel-plan 1

# 3. 开始写作
/webnovel-write 1

# 4. 审查章节
/webnovel-review 1-5
```

## 项目结构
```
小说项目/
├── .webnovel/          # 运行时状态和数据
│   ├── state.json
│   ├── backups/
│   └── summaries/
├── 设定集/             # 世界观、角色设定等
│   ├── 世界观.md
│   ├── 力量体系.md
│   └── 主角卡.md
├── 大纲/               # 总纲和卷章大纲
│   └── 总纲.md
├── 正文/               # 章节内容
└── 审查报告/           # 质量审查结果
```

## 更多信息
详细使用说明请查看 [webnovel-writer/README.md](file:///workspace/.trae/skills/webnovel-writer/README.md)
