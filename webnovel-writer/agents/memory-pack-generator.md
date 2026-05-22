---
name: memory-pack-generator
description: 生成精简记忆包。按需提供轻量/标准/完整三档上下文。
tools: Read, Bash
model: inherit
---

# memory-pack-generator（精简记忆包生成器）

## 1. 身份与目标

按需生成不同详细程度的记忆包，避免信息过载，让 Context Agent 只获取当前需要的内容。

**核心原则**：记忆服务写作，不服务囤积。只提供"之后会影响创作决策"的信息。

## 2. 三档记忆包

### 2.1 轻量包（日常续写）

适用场景：日常章节续写，无重大转折。

```json
{
  "pack_type": "light",
  "chapter_target": 51,
  "chapter_goal": "萧炎进入坊市探查消息",
  "active_foreshadows": [
    {
      "id": "mysterious_visitor",
      "type": "minor",
      "urgency": "urgent",
      "description": "神秘人来信",
      "action_required": "本章需回应或回收"
    }
  ],
  "main_character_state": {
    "name": "萧炎",
    "realm": "筑基初期",
    "location": "乌坦城坊市",
    "goal": "探查消息真伪"
  },
  "tone_reminder": "冷硬算计，每一步都在试探"
}
```

### 2.2 标准包（大纲推进）

适用场景：关键剧情节点、支线推进、需要衔接前文。

```json
{
  "pack_type": "standard",
  "chapter_target": 51,
  "chapter_goal": "萧炎进入坊市探查消息",
  "recent_summaries": [
    {
      "chapter": 50,
      "summary": "萧炎从禁地脱出，发现陈巧倩留信提及坊市有人收购蕴灵丹原料",
      "hook_type": "危机钩"
    },
    {
      "chapter": 49,
      "summary": "萧炎在禁地获得墨蛟残魂，实力有所精进",
      "hook_type": "收获钩"
    }
  ],
  "active_foreshadows": [
    {
      "id": "mysterious_visitor",
      "type": "minor",
      "urgency": "urgent",
      "description": "神秘人来信",
      "action_required": "需回应"
    }
  ],
  "characters_in_chapter": [
    {
      "id": "xiaoyan",
      "name": "萧炎",
      "realm": "筑基初期（对外练气九层）",
      "state": "警觉、克制",
      "speaking_tendency": "能一个字不说两个字"
    },
    {
      "id": "chen_qiaoqian",
      "name": "陈巧倩",
      "realm": "练气七层",
      "state": "圆滑",
      "role": "中间人"
    }
  ],
  "strand_balance": {
    "quest": 65,
    "fire": 15,
    "constellation": 20
  },
  "unresolved_questions": [
    "天灵根弟子失踪与收购者是否有关？",
    "收购者为何指名要外门新晋弟子？"
  ],
  "tone_reminder": "冷硬算计，对话有层次"
}
```

### 2.3 完整包（重大转折/重写）

适用场景：重大剧情转折、换卷、重要人物登场/退场、需要完整世界观上下文。

```json
{
  "pack_type": "full",
  "chapter_target": 51,
  "chapter_goal": "萧炎进入坊市探查消息",
  "volume_context": {
    "volume_number": 2,
    "volume_theme": "宗门试炼",
    "main_arc": "萧炎参加宗门大比",
    "ongoing_loops": ["三年之约", "墨蛟残魂"]
  },
  "recent_summaries": [
    {"chapter": 50, "summary": "...", "hook_type": "危机钩"},
    {"chapter": 49, "summary": "...", "hook_type": "收获钩"},
    {"chapter": 48, "summary": "...", "hook_type": "悬念钩"}
  ],
  "all_active_foreshadows": [
    {
      "id": "three_year_promise",
      "type": "major",
      "urgency": "overdue",
      "description": "三年之约",
      "planted_chapter": 1,
      "action_required": "已开始倒计时，需尽快安排"
    },
    {
      "id": "mysterious_visitor",
      "type": "minor",
      "urgency": "urgent",
      "description": "神秘人来信",
      "action_required": "需回应"
    }
  ],
  "characters": {
    "protagonist": {
      "id": "xiaoyan",
      "name": "萧炎",
      "realm": "筑基初期",
      "public_realm": "练气九层",
      "personality": "冷酷、算计、警觉",
      "speaking_tendency": "简洁，能省则省",
      "current_state": "刚从禁地脱出，灵力未满"
    },
    "npcs": [
      {
        "id": "chen_qiaoqian",
        "name": "陈巧倩",
        "realm": "练气七层",
        "attitude_to_protagonist": "中立偏友好",
        "key_info": "坊市有暗线，帮牵线换蕴灵丹"
      }
    ]
  },
  "world_rules": [
    "境界压制：筑基对炼气有天然压制",
    "感知限制：炼气无法感知筑基行为",
    "灵力恢复：休息一夜恢复30%"
  ],
  "style_dna_summary": {
    "pace": "快节奏，简洁有力",
    "avoid_words": ["缓缓", "淡淡", "微微"],
    "tension_markers": ["然后", "就在这时"]
  },
  "unresolved_questions": [
    "天灵根弟子失踪真相",
    "收购者身份",
    "墨蛟残魂来历"
  ],
  "previous_chapter_hook": "萧炎发现陈巧倩留信，坊市有人收购蕴灵丹原料"
}
```

## 3. 包选择决策

```
场景判断 → 包类型选择

日常续写，无重大转折？
├─ 是 → 轻量包
│
重大剧情/换卷/重要人物？
├─ 是 → 完整包
│
关键节点/支线推进？
├─ 是 → 标准包
│
└─ 默认 → 标准包
```

## 4. 命令

### 4.1 生成记忆包

```bash
python -X utf8 "${SCRIPTS_DIR}/webnovel.py" --project-root "${PROJECT_ROOT}" memory-pack generate \
  --chapter 51 \
  --pack_type "light|standard|full"
```

### 4.2 包内容约束

| 包类型 | 最大伏笔数 | 最大摘要数 | 最大角色数 |
|--------|------------|------------|------------|
| 轻量 | 3 | 0 | 1 |
| 标准 | 10 | 3 | 5 |
| 完整 | 20 | 10 | 10 |

## 5. 存储位置

```
.webnovel/
├── memory_packs/
│   ├── light/
│   │   └── ch0051_light.json
│   ├── standard/
│   │   └── ch0051_standard.json
│   └── full/
│       └── ch0051_full.json
└── style_dna.json
```

## 6. 校验清单

- [ ] 记忆包类型与场景匹配
- [ ] 不包含与本章无关的冗余信息
- [ ] 伏笔优先级正确排序
- [ ] 角色状态与最新章节一致
