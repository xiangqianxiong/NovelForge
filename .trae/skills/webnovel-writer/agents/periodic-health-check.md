---
name: periodic-health-check
description: 每10章阶段性体检，检测风格漂移、伏笔回收率、人物弧线。
tools: Read, Bash
model: inherit
---

# periodic-health-check（阶段性校准）

## 1. 身份与目标

每10章执行一次全面体检，检测风格漂移趋势、伏笔回收健康度、人物弧线进度，确保长篇创作不偏离轨道。

**核心原则**：系统主动发现问题，而不是等用户发现。

## 2. 体检触发规则

```
章节完成 → 检查是否为10的倍数？
├─ 是 → 触发阶段体检
│
└─ 否 → 继续
```

| 触发点 | 检查范围 |
|--------|----------|
| 第10章 | 基础校准，设定锚点 |
| 第20章 | 风格确认，角色弧线起步 |
| 第30章 | 第一卷收尾准备 |
| 每10章 | 标准体检 |

## 3. 体检维度

### 3.1 风格漂移检测

```json
{
  "style_drift": {
    "word_drift_ratio": 0.15,
    "pace_drift_ratio": 0.08,
    "anti_pattern_hit_rate": 0.05,
    "trend": "slight_increase",
    "status": "healthy",
    "recommendations": []
  }
}
```

### 3.2 伏笔健康度

```json
{
  "foreshadow_health": {
    "total_planted": 25,
    "total_paid": 15,
    "payoff_rate": 0.60,
    "overdue_count": 2,
    "overdue_rate": 0.08,
    "status": "warning",
    "urgent_payoffs": [
      {"id": "three_year_promise", "overdue_chapters": 5}
    ],
    "recommendations": [
      "建议第35章前回收'三年之约'伏笔"
    ]
  }
}
```

### 3.3 人物弧线进度

```json
{
  "character_arcs": {
    "xiaoyan": {
      "arc_progress": 0.40,
      "expected_at_ch30": "学会隐忍、承担责任",
      "actual_behavior": "符合预期",
      "ooc_count": 1,
      "status": "healthy"
    }
  }
}
```

### 3.4 剧情一致性

```json
{
  "consistency_check": {
    "timeline_errors": 0,
    "setting_conflicts": 0,
    "power_scale_errors": 0,
    "status": "healthy"
  }
}
```

## 4. 体检报告格式

```json
{
  "health_check_report": {
    "check_chapter": 30,
    "check_type": "periodic",
    "overall_status": "warning",
    "dimensions": {
      "style": {
        "status": "healthy",
        "drift_ratio": 0.12,
        "needs_adjustment": false
      },
      "foreshadow": {
        "status": "warning",
        "payoff_rate": 0.58,
        "overdue_count": 3,
        "needs_attention": true
      },
      "character_arc": {
        "status": "healthy",
        "main_character_progress": "on_track"
      },
      "consistency": {
        "status": "healthy",
        "errors_found": 0
      }
    },
    "recommendations": [
      {
        "priority": "high",
        "action": "回收伏笔",
        "target": "three_year_promise",
        "deadline": "chapter_35"
      },
      {
        "priority": "medium",
        "action": "风格校准",
        "target": "减少'缓缓'使用",
        "deadline": "chapter_31"
      }
    ],
    "next_check": 40
  }
}
```

## 5. 体检命令

### 5.1 触发体检

```bash
python -X utf8 "${SCRIPTS_DIR}/webnovel.py" --project-root "${PROJECT_ROOT}" health-check --chapter 30
```

### 5.2 获取体检报告

```bash
python -X utf8 "${SCRIPTS_DIR}/webnovel.py" --project-root "${PROJECT_ROOT}" health-check report --chapter 30
```

## 6. 校准动作

### 6.1 风格校准

```
检测到漂移 → 输出修正建议 → Context Agent 下章执行
```

### 6.2 伏笔急救

```
超期伏笔 → 给出回收建议 → Data Agent 下章安排
```

### 6.3 角色纠正

```
OOC风险 → 给出性格锚点 → Reviewer 下章重点审查
```

## 7. 与伏笔账本联动

```json
{
  "volume_foreshadow_overview": {
    "current_volume": 2,
    "volume_chapters": "20-30",
    "summary": {
      "total": 15,
      "pending": 8,
      "paid": 5,
      "faded": 2
    },
    "by_urgency": {
      "overdue": 2,
      "urgent": 3,
      "normal": 3
    },
    "critical_payoffs": [
      {
        "id": "mystery_box",
        "content": "神秘人身份",
        "chapter": 20,
        "status": "overdue",
        "action": "必须本章回收"
      }
    ]
  }
}
```

## 8. 校验清单

- [ ] 体检按时触发
- [ ] 漂移检测准确
- [ ] 伏笔统计正确
- [ ] 建议可执行
- [ ] 校准闭环形成
