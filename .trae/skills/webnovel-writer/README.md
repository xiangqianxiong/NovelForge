# Webnovel Writer - 网文创作技能

## 快速开始

### 1. 初始化项目
```
/webnovel-init
```

### 2. 规划大纲
```
/webnovel-plan 1
```

### 3. 开始写作
```
/webnovel-write 1
```

### 4. 审查章节
```
/webnovel-review 1-5
```

## 核心功能

| 命令 | 功能 |
|------|------|
| `/webnovel-init` | 初始化小说项目 |
| `/webnovel-plan` | 规划卷级大纲 |
| `/webnovel-write` | 写作章节 |
| `/webnovel-review` | 审查质量 |
| `/webnovel-query` | 查询信息 |
| `/webnovel-learn` | 学习写作模式 |
| `/webnovel-dashboard` | 可视化面板 |

## 项目结构

```
小说项目/
├── .webnovel/
│   ├── state.json
│   ├── backups/
│   ├── summaries/
│   └── archive/
├── 设定集/
│   ├── 世界观.md
│   ├── 力量体系.md
│   └── 主角卡.md
├── 大纲/
│   └── 总纲.md
└── 正文/
```

## 参考资料

- `references/genre-profiles.md` - 37种题材配置
- `references/reading-power-taxonomy.md` - 追读力学
- `references/review-schema.md` - 审查规范
- `genres/` - 详细题材目录

## 设计原则

### 防幻觉三定律
1. 大纲即法律
2. 设定即物理
3. 发明需识别

### Strand 节奏
- Quest 60% / Fire 20% / Constellation 20%

### 六维审查
- High-point / Consistency / Pacing
- OOC / Continuity / Reader-pull
