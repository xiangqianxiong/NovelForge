# 风格DNA - 网文风格基线

## 定位

风格DNA是网文写作的"基因图谱"，定义了一本书区别于其他书的独特风格特征。

## 结构

```json
{
  "version": "1.0",
  "book_title": "凡人修仙传",
  "extracted_chapters": [1, 2, 3],
  "style_features": {
    "vocabulary": {
      "high_freq_words": ["修士", "灵气", "筑基", "丹药", "功法"],
      "genre_specific": ["灵根", "丹田", "元婴", "飞升"],
      "action_verbs": ["冷哼", "目光一凝", "身形一晃"]
    },
    "sentence_patterns": {
      "short_cuts": ["他没说话。", "只是看着。", "走了。"],
      "four_char_clusters": ["目光如炬", "灵光一闪", "浑身一颤"],
      "dialogue_tags": ["沉声道", "冷笑道", "淡淡道"]
    },
    "tension_markers": {
      "chapter_hooks": ["就在这时", "突然", "然而"],
      "cliffhangers": ["就在这时", "但他不知道的是", "危险正在逼近"]
    },
    "emotional_expressions": {
      "physiological": ["瞳孔微缩", "手指轻颤", "后背发凉"],
      "micro_expressions": ["嘴角微扬", "眉头一皱", "眼神闪烁"]
    }
  },
  "anti_patterns": {
    "avoid_words": ["缓缓", "淡淡", "微微", "轻轻"],
    "avoid_phrases": ["他感到", "他明白", "此时此刻"],
    "avoid_structures": ["四段闭环（起因经过结果感悟）", "连续同构句"]
  },
  "pace_metrics": {
    "avg_sentence_length": 18,
    "avg_paragraph_length": 45,
    "dialogue_ratio": 0.35,
    "action_ratio": 0.40,
    "description_ratio": 0.25
  },
  "character_voices": {
    "xiaoyan": {
      "speaking_style": "简洁冷硬，能一个字不说两个字",
      "internal_thought": "算计型，每步都有后手",
      "example": ""嗯。"", ""走。"", ""你确定？""
    },
    "yaolao": {
      "speaking_style": "老练沉稳，偶尔带调侃",
      "internal_thought": "看透世事，随性而为",
      "example": ""小子，胆子不小。"", ""有意思。""
    }
  },
  "genre_conventions": {
    "tropes_used": ["退婚流", "升级流", "宗门流"],
    "subverted_tropes": [],
    "signature_moments": ["突破时的异象", "打脸时的简洁", "危机时的冷静"]
  }
}
```

## 提取流程

### 初始化时（项目创建后）

1. 收集前3-5章已确认风格正确的正文
2. 调用 `style_dna_extractor` 分析
3. 生成初始风格DNA
4. 保存到 `.webnovel/style_dna.json`

### 提取内容

| 维度 | 分析内容 |
|------|----------|
| 词汇 | 高频词、题材特有词、动作词 |
| 句式 | 短句切割、四字格、对话标签 |
| 节奏 | 平均句长、段落长度、对话占比 |
| 情绪 | 生理反应、微表情、情感标记词 |
| 角色声线 | 各角色说话风格、内心独白模式 |
| 反模式 | 需避免的词/句式/结构 |

## 校准检测

### 检测时机

- 每章写作完成后
- 阶段校准时（每10章）

### 检测维度

| 检测项 | 说明 | 阈值 |
|--------|------|------|
| 词汇偏离度 | 新文本高频词与DNA差异 | >30% 偏离 |
| 句式偏离度 | 短句比例变化 | >20% 变化 |
| 节奏偏离度 | 对话/动作比例变化 | >25% 变化 |
| 反模式命中 | 出现avoid_words | 任意命中 |

### 偏离报告

```json
{
  "chapter": 51,
  "calibration_result": {
    "word_drift": {
      "status": "warning",
      "drift_ratio": 0.35,
      "new_words": ["突然地", "慢慢地"],
      "missing_words": ["冷哼", "目光一凝"]
    },
    "pace_drift": {
      "status": "ok",
      "drift_ratio": 0.12
    },
    "anti_pattern_hits": {
      "status": "critical",
      "hits": [
        {"pattern": "缓缓", "count": 3, "locations": ["第2段", "第5段"]},
        {"pattern": "他感到", "count": 2, "locations": ["第8段"]}
      ]
    }
  },
  "overall_status": "需要修正",
  "suggestions": [
    "减少'缓缓'使用，改用具体动作",
    "第8段'他感到愤怒'改为生理反应描写"
  ]
}
```

## 与写作流程集成

### Context Agent

- 读取风格DNA
- 在任务书中体现角色声线
- 提醒当前章节的风格要求

### Data Agent

- 提取本章风格样本
- 触发风格校准检测

### Reviewer

- 对比本章与风格DNA
- 输出偏离警告

## 维护规则

- 每10章重新校准一次
- 风格样本库持续积累
- 角色声线随剧情发展可微调
- 题材特有词可随世界观扩展更新
