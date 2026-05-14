---
name: "webnovel-learn"
description: "从当前会话或用户输入中提取可复用写作模式，写入项目记忆。"
---

# `/webnovel-learn` - 写作模式学习

## 功能说明

从当前会话或用户输入中提取可复用的写作模式，写入项目长期记忆。

## 参数

- `[内容]`：要学习的写作内容，如 `"本章的危机钩设计很有效，悬念拉满"`

## 使用场景

- 用户总结本次写作经验时
- 发现有效的写作技巧时
- 需要固化写作模式时

## 学习内容类型

### 1. 钩子设计
```json
{
  "type": "hook_pattern",
  "pattern": "悬念钩",
  "description": "用未解之谜吸引读者",
  "example": "他究竟是谁？"
}
```

### 2. 爽点设计
```json
{
  "type": "cool_point",
  "pattern": "装逼打脸",
  "description": "主角在嘲讽者面前展现实力",
  "conditions": ["被嘲讽", "隐藏实力", "强势反击"]
}
```

### 3. 节奏模式
```json
{
  "type": "pacing_pattern",
  "pattern": "压抑-爆发",
  "description": "先压抑情绪，再一次性释放",
  "example": "主角一直被压制，章末逆袭"
}
```

### 4. 对话技巧
```json
{
  "type": "dialogue_pattern",
  "pattern": "潜台词对话",
  "description": "对话表面一层意思，底下藏另一层",
  "example": "问东答西，欲言又止"
}
```

## 执行流程

1. 解析用户输入
2. 识别写作模式类型
3. 提取关键要素
4. 生成结构化记录
5. 追加到 `.webnovel/project_memory.json`

## project_memory.json 结构

```json
{
  "hook_patterns": [],
  "cool_points": [],
  "pacing_patterns": [],
  "dialogue_patterns": [],
  "other_patterns": [],
  "updated_at": ""
}
```

## 示例

用户：`/webnovel-learn "这章的打斗设计很紧凑，一招一式都有画面感"`

系统提取：
```json
{
  "type": "combat_description",
  "pattern": "简洁战斗描写",
  "description": "用简短的动作描写表现战斗",
  "example": "萧炎抬手，一拳轰出。",
  "source_chapter": 1
}
```
