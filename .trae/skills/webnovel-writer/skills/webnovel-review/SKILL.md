---
name: "webnovel-review"
description: "审查章节质量。执行六维质量审查，输出结构化问题清单。"
---

# `/webnovel-review` - 章节审查

## 功能说明

对已有章节执行六维质量审查，输出结构化问题清单。

## 参数

- `[范围]`：要审查的章节范围，如 `1-5`、`45`

## 六维审查

| 维度 | 检查重点 | severity 级别 |
|------|----------|---------------|
| High-point | 爽点密度与质量 | - |
| Consistency | 设定一致性（战力/地点/时间线） | critical/high |
| Pacing | Strand 比例与断档 | - |
| OOC | 人物行为是否偏离人设 | high |
| Continuity | 场景与叙事连贯性 | high |
| Reader-pull | 钩子强度、期待管理 | - |

## AI 味检查

### 词汇层
- 高频 AI 词汇密度
- "缓缓/淡淡/微微"+动词 出现频率
- "眸中闪过""瞳孔微缩"等神态模板

### 句式层
- "起因→经过→结果→感悟"四段闭环
- 连续同构句（≥3句）
- 总结句收尾模式

### 叙事层
- 节奏匀速
- "他不知道的是……"反讽提示
- 章末"安全着陆"

### 情感层
- 情绪标签化（"他感到愤怒"）
- 情绪即时切换

### 对话层
- 信息宣讲式对话
- 全员书面语

## 输出格式

```json
{
  "issues": [
    {
      "severity": "critical | high | medium | low",
      "category": "continuity | setting | character | timeline | ai_flavor | logic",
      "location": "第N段 或 具体引用",
      "description": "问题描述",
      "evidence": "原文引用 vs 数据记录",
      "fix_hint": "修复方向",
      "blocking": true
    }
  ],
  "summary": "N个问题：X个阻断，Y个高优"
}
```

## 执行流程

1. 读取待审查章节正文
2. 读取设定集（世界规则、角色设定）
3. 读取上章摘要
4. 执行六维审查
5. 输出问题清单

## 边界

- **不评分**——不输出 overall_score
- **不评价文笔质量**
- **不建议情节改动**
- **只报可验证的问题**
