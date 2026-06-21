# Webnovel Writer - 网文创作技能

## 核心规则：一本书 = 一个项目目录

- 每本小说对应一个独立项目目录，目录名 = 书名（如 `逆天改命/`、`斗破苍穹/`）
- 所有创作活动都在该书的项目目录内进行
- 工作目录下可同时存在多本书的项目目录，互不干扰
- 所有创作类命令必须先找到项目目录才能执行，找不到时提示先 init

## 快速开始

### 1. 初始化项目
输入书名和题材，**用户确认后**创建项目目录
```
/webnovel-init
```
→ 生成 `{书名}/` 目录及标准结构

### 2. 规划大纲
在 `{书名}/大纲/` 内保存
```
/webnovel-plan 1
```

### 3. 开始写作
在 `{书名}/正文/` 内保存章节
```
/webnovel-write 1
```

### 4. 审查章节
报告保存在 `{书名}/审查报告/`
```
/webnovel-review 1-5
```

### 5. 批量写作多章
```
/batch-write 1-20
```

### 6. 去AI味润色
L1-L4 四层自检
```
/webnovel-deslop
```

## 完整命令列表

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
| `/webnovel-analyze` | 拆解分析爆款作品 | 有目录则从 `{书名}/正文/` 读 |
| `/webnovel-deslop` | 去除文章AI味（L1-L4 四层自检） | 有目录则在 `{书名}/` 内 |
| `/webnovel-cover` | 生成小说封面 | 有目录则复用书名题材 |
| `/webnovel-import` | 导入已有作品续写 | 新建 `{书名}/` 目录 |

## 项目结构（目录名 = 书名）

```
{书名}/                    # 项目根目录，目录名 = 小说书名
├── .webnovel/            # 运行时状态和数据
│   ├── state.json        # 书名、题材、进度、风格设置
│   ├── backups/          # 备份
│   ├── summaries/        # 章节摘要
│   └── archive/          # 归档
├── 设定集/               # 世界观、角色设定等
│   ├── 世界观.md
│   ├── 力量体系.md
│   └── 主角卡.md
├── 大纲/                 # 总纲和卷章大纲
│   └── 总纲.md
├── 正文/                 # 章节内容（第1章-xxx.md）
└── 审查报告/             # 质量审查结果
```

## 参考资料

- `references/genre-profiles.md` - 37种题材配置
- `references/reading-power-taxonomy.md` - 追读力学
- `references/review-schema.md` - 审查规范
- `references/anti-ai-writing.md` - 去AI味方法
- `references/banned-words.md` - AI禁用词清单
- `references/structures.md` - 结构性问题清单
- `references/examples.md` - 改写示例库
- `references/auto-review-workflow.md` - 自动审核流程
- `references/physics-rules.md` - 物理法则追踪
- `genres/` - 详细题材目录

## 设计原则

### 防幻觉三定律
1. 大纲即法律
2. 设定即物理
3. 发明需识别（新实体由 data-agent 提取）

### Strand 节奏系统
- **Quest** 主线剧情 60%
- **Fire** 感情线 20%
- **Constellation** 世界观扩展 20%
- Quest 连续不超过 5 章
- Fire 断档不超过 10 章
- Constellation 断档不超过 15 章

### 质量审查体系
- **六维审查**：High-point / Consistency / Pacing / OOC / Continuity / Reader-pull
- **去AI味**：L1（硬性规则）→ L2（风格一致性）→ L3（内容质量）→ L4（活人感终审）
- **物理法则追踪**：境界法则、能量法则、空间法则、时间法则、因果法则

### 19 个智能代理协同工作
- **Context Agent** - 写前构建创作任务书
- **Data Agent** - 从正文提取事实，更新状态和记忆
- **Reviewer Agent** - 六维质量审查
- **Auto-Validator** - 提交前自动校验
- **Foreshadow-Manager** - 伏笔生命周期追踪
- **Emotion-Analyzer** - 情绪曲线分析
- **Style-Learner** - 风格学习和模式提取
- **Item-Tracker** - 物品流转一致性
- **Number-Checker** - 数字/时间线一致性
- **Knowledge-Boundary** - 角色知识边界检查
- **POV-Checker** - 视角泄漏检查
- **Relationship-Matrix** - 势力关系矩阵
- **Character-Growth** - 角色成长追踪
- **Periodic-Health** - 每10章阶段体检
- **Volume-Foreshadow** - 卷级伏笔全景视图
- **Regression-Tester** - 回归测试
- **Deconstruction Agent** - 参考书拆解
- **Batch-Writer** - 状态机批量写作
- **Memory-Pack Generator** - 三档上下文按需生成
