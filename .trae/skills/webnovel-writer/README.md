# 网文写作技能安装指南

## 技能简介

本技能参考 [webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) 项目设计，专为长篇网文创作场景优化。

## 功能概览

| 功能 | 说明 |
|------|------|
| `/webnovel-init` | 初始化小说项目，创建项目结构 |
| `/webnovel-plan` | 规划卷级大纲和章节安排 |
| `/webnovel-write` | 写作完整章节，包含质量审查 |
| `/webnovel-review` | 六维质量审查 |
| `/webnovel-query` | 查询角色、伏笔、剧情状态 |

## 安装步骤

### 方式一：复制到项目配置（推荐）

1. 将 `webnovel-writer` 文件夹复制到您的 SOLO 项目配置目录：
   ```
   .trae/skills/
   ```

2. 重启 SOLO 或刷新配置

### 方式二：复制到全局配置

1. 找到 SOLO 的全局技能配置目录
2. 将 `webnovel-writer` 文件夹放入

## 快速开始

### 1. 初始化项目

在 SOLO 中输入：
```
/webnovel-init
```

按提示填写：
- 书名
- 题材（可组合，最多2个）
- 主角信息
- 金手指设定
- 核心冲突

### 2. 规划大纲

```
/webnovel-plan 1
```

生成第一卷的大纲和章节安排。

### 3. 开始写作

```
/webnovel-write 1
```

系统会自动：
1. 读取上下文和大纲
2. 生成写作任务书
3. 完成正文写作
4. 执行质量审查
5. 保存章节

### 4. 审查章节

```
/webnovel-review 1-10
```

对第1-10章进行六维质量审查。

### 5. 查询信息

```
/webnovel-query 萧炎
/webnovel-query 伏笔
/webnovel-query 节奏
```

## 核心概念

### 防幻觉三定律

1. **大纲即法律** - 遵循大纲，不擅自发挥
2. **设定即物理** - 遵守设定，不自相矛盾
3. **发明需识别** - 新实体必须入库管理

### Strand 节奏系统

| Strand | 含义 | 理想占比 |
|--------|------|----------|
| Quest | 主线剧情 | 60% |
| Fire | 感情线 | 20% |
| Constellation | 世界观扩展 | 20% |

### 六维审查

| 维度 | 检查重点 |
|------|----------|
| High-point | 爽点密度与质量 |
| Consistency | 设定一致性 |
| Pacing | Strand 比例与断档 |
| OOC | 人物行为是否偏离人设 |
| Continuity | 场景与叙事连贯性 |
| Reader-pull | 钩子强度与期待管理 |

## 文件结构

```
webnovel-writer/
├── SKILL.md           # 主技能文件
├── writing-guide.md   # 写作风格指南
├── genre-templates.md # 题材模板
└── README.md          # 本文件
```

## 参考项目

本技能设计参考了 [webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) 项目，这是一个基于 Claude Code 的长篇网文创作系统，提供了丰富的创作理念和实践方法。

## 写作建议

1. **保持更新节奏**：日更或稳定更新
2. **注重开篇**：黄金三章决定读者去留
3. **控制节奏**：合理分布爽点
4. **保持一致**：遵守世界观和人物设定
5. **留下悬念**：每章结尾要有钩子

祝创作愉快！
