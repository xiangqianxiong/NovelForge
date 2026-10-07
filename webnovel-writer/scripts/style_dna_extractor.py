#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Style DNA Extractor - 风格 DNA 提取器

从章节文本中提取风格特征，构建风格 DNA
"""

import argparse
import json
import re
import os
from pathlib import Path
from collections import Counter
from typing import Dict, List, Any, Tuple
import sys

# 常见网文词汇分类
VOCABULARY_CATEGORIES = {
    '武侠仙侠': ['剑', '刀', '功法', '灵气', '筑基', '金丹', '元婴', '飞升', '丹田', '经脉'],
    '玄幻奇幻': ['魔法', '斗气', '异能', '血脉', '天赋', '法则', '神力', '元素'],
    '都市言情': ['总裁', '豪门', '少爷', '小姐', '都市', '职场', '甜蜜', '霸道'],
    '动作词': ['冷笑', '冷哼', '目光一凝', '身形一晃', '纵身', '拔剑', '挥掌'],
    '情绪词': ['愤怒', '悲伤', '喜悦', '恐惧', '惊讶', '无奈', '惆怅'],
    '副词': ['缓缓', '淡淡', '微微', '轻轻', '慢慢', '渐渐'],
    '四字格': ['目光如炬', '灵光一闪', '浑身一颤', '侠肝义胆', '情深义重']
}

# Anti-patterns (需要避免的)
ANTI_PATTERNS = {
    'emotion_labels': ['他感到', '他觉得', '他明白', '此时此刻', '不由得'],
    'overused_adverbs': ['缓缓地', '淡淡地', '微微地', '轻轻地', '慢慢地'],
    'ai_phrases': ['突然', '然而', '就在这时', '就在这时间', '不由得']
}


class StyleDNAExtractor:
    """风格 DNA 提取器"""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.chapters_dir = project_root / "正文"
        self.output_file = project_root / ".webnovel" / "style_dna.json"

    def extract_chapters(self, chapter_numbers: List[int]) -> List[str]:
        """提取指定章节的内容"""
        chapters = []

        for num in chapter_numbers:
            chapter_files = list(self.chapters_dir.glob(f"第{num:04d}章-*.md"))
            if chapter_files:
                with open(chapter_files[0], 'r', encoding='utf-8') as f:
                    chapters.append(f.read())

        return chapters

    def extract_vocabulary(self, text: str) -> Dict[str, List[str]]:
        """提取词汇特征"""
        vocabulary = {
            'high_freq_words': [],
            'genre_specific': [],
            'action_verbs': [],
            'emotion_words': []
        }

        # 统计高频词
        words = re.findall(r'[\u4e00-\u9fa5]+', text)
        word_freq = Counter(words)

        # 获取前20高频词
        vocabulary['high_freq_words'] = [w for w, c in word_freq.most_common(20)]

        # 提取题材特有词
        for category, words in VOCABULARY_CATEGORIES.items():
            for word in words:
                if word in text:
                    if category == '动作词':
                        vocabulary['action_verbs'].append(word)
                    elif category == '情绪词':
                        vocabulary['emotion_words'].append(word)
                    else:
                        vocabulary['genre_specific'].append(word)

        return vocabulary

    def extract_sentence_patterns(self, text: str) -> Dict[str, Any]:
        """提取句式特征"""
        patterns = {
            'short_cuts': [],
            'four_char_clusters': [],
            'dialogue_tags': []
        }

        # 短句切割 (少于10字的独立句子)
        sentences = re.split(r'[。！？]', text)
        for sent in sentences:
            sent = sent.strip()
            if 2 <= len(sent) <= 10:
                patterns['short_cuts'].append(sent)

        # 四字格
        four_char = re.findall(r'[\u4e00-\u9fa5]{4}', text)
        four_char_freq = Counter(four_char)
        patterns['four_char_clusters'] = [fc for fc, c in four_char_freq.most_common(30)]

        # 对话标签
        dialogue_tags = re.findall(r'["""\']([^"""\'。！？]+)["""\']', text)
        tag_patterns = [
            r'[\u4e00-\u9fa5]{1,3}(?:道|说|问|答|喊|笑|怒|叹|冷笑道|沉声道|朗声道)',
        ]
        for pattern in tag_patterns:
            matches = re.findall(pattern, text)
            patterns['dialogue_tags'].extend(matches)

        return patterns

    def extract_tension_markers(self, text: str) -> Dict[str, List[str]]:
        """提取张力标记"""
        markers = {
            'chapter_hooks': [],  # 章节钩子
            'cliffhangers': []    # 悬念结尾
        }

        # 章节钩子词
        hooks = ['就在这时', '突然', '然而', '但是', '就在此时', '就在这一刻']
        for hook in hooks:
            if hook in text:
                markers['chapter_hooks'].append(hook)

        # 悬念结尾模式
        cliffhanger_patterns = [
            r'就在这时',
            r'但他不知道的是',
            r'危险正在逼近',
            r'没有人知道',
            r'答案即将揭晓'
        ]
        for pattern in cliffhanger_patterns:
            if re.search(pattern, text):
                markers['cliffhangers'].append(pattern)

        return markers

    def extract_emotional_expressions(self, text: str) -> Dict[str, List[str]]:
        """提取情绪表达"""
        expressions = {
            'physiological': [],  # 生理反应
            'micro_expressions': []  # 微表情
        }

        # 生理反应
        physio_patterns = [
            '瞳孔微缩', '手指轻颤', '后背发凉', '心跳加速',
            '脸色苍白', '拳头紧握', '指节发白', '浑身一颤'
        ]
        for pattern in physio_patterns:
            if pattern in text:
                expressions['physiological'].append(pattern)

        # 微表情
        micro_patterns = [
            '嘴角微扬', '眉头一皱', '眼神闪烁', '嘴角上扬',
            '眉头紧锁', '眼神一凝', '嘴角一抽'
        ]
        for pattern in micro_patterns:
            if pattern in text:
                expressions['micro_expressions'].append(pattern)

        return expressions

    def extract_pace_metrics(self, text: str) -> Dict[str, float]:
        """提取节奏指标"""
        # 计算平均句子长度
        sentences = re.split(r'[。！？]', text)
        sentences = [s.strip() for s in sentences if s.strip()]

        if sentences:
            avg_sentence_length = sum(len(s) for s in sentences) / len(sentences)
        else:
            avg_sentence_length = 0

        # 计算平均段落长度
        paragraphs = text.split('\n\n')
        paragraphs = [p.strip() for p in paragraphs if p.strip()]
        if paragraphs:
            avg_paragraph_length = sum(len(p) for p in paragraphs) / len(paragraphs)
        else:
            avg_paragraph_length = 0

        # 统计对话、动作、描写比例
        dialogue_count = len(re.findall(r'["""\']', text))
        action_count = len(re.findall(r'(纵身|拔剑|挥掌|出招|后退|闪避)', text))
        desc_count = len(re.findall(r'(只见|只见得|看起来)', text))

        total = dialogue_count + action_count + desc_count
        if total > 0:
            dialogue_ratio = dialogue_count / total
            action_ratio = action_count / total
            description_ratio = desc_count / total
        else:
            dialogue_ratio = 0.3
            action_ratio = 0.4
            description_ratio = 0.3

        return {
            'avg_sentence_length': round(avg_sentence_length, 2),
            'avg_paragraph_length': round(avg_paragraph_length, 2),
            'dialogue_ratio': round(dialogue_ratio, 3),
            'action_ratio': round(action_ratio, 3),
            'description_ratio': round(description_ratio, 3)
        }

    def check_anti_patterns(self, text: str) -> Dict[str, List[Dict]]:
        """检查反模式"""
        anti_pattern_hits = {
            'emotion_labels': [],
            'overused_adverbs': [],
            'ai_phrases': []
        }

        # 检查情感标签
        for pattern in ANTI_PATTERNS['emotion_labels']:
            matches = list(re.finditer(pattern, text))
            if matches:
                for match in matches:
                    line_num = text[:match.start()].count('\n') + 1
                    anti_pattern_hits['emotion_labels'].append({
                        'pattern': pattern,
                        'line': line_num,
                        'context': text[max(0, match.start()-10):match.end()+10]
                    })

        # 检查过度使用的副词
        for pattern in ANTI_PATTERNS['overused_adverbs']:
            matches = list(re.finditer(pattern, text))
            if matches:
                for match in matches:
                    line_num = text[:match.start()].count('\n') + 1
                    anti_pattern_hits['overused_adverbs'].append({
                        'pattern': pattern,
                        'line': line_num,
                        'count': len(matches)
                    })

        # 检查AI痕迹
        for pattern in ANTI_PATTERNS['ai_phrases']:
            count = len(re.findall(pattern, text))
            if count > 5:  # 超过5次认为是问题
                anti_pattern_hits['ai_phrases'].append({
                    'pattern': pattern,
                    'count': count
                })

        return anti_pattern_hits

    def extract_style_dna(self, chapters: List[int]) -> Dict[str, Any]:
        """提取完整风格 DNA"""
        print(f"正在分析第 {chapters} 章...")

        # 读取章节内容
        texts = self.extract_chapters(chapters)
        if not texts:
            print("未找到指定章节")
            return {}

        full_text = '\n\n'.join(texts)

        # 提取各项特征
        print("提取词汇特征...")
        vocabulary = self.extract_vocabulary(full_text)

        print("提取句式特征...")
        sentence_patterns = self.extract_sentence_patterns(full_text)

        print("提取张力标记...")
        tension_markers = self.extract_tension_markers(full_text)

        print("提取情绪表达...")
        emotional_expressions = self.extract_emotional_expressions(full_text)

        print("提取节奏指标...")
        pace_metrics = self.extract_pace_metrics(full_text)

        print("检查反模式...")
        anti_patterns = self.check_anti_patterns(full_text)

        # 构建风格 DNA
        style_dna = {
            'version': '1.0',
            'book_title': self.project_root.name,
            'extracted_chapters': chapters,
            'extracted_at': self.get_current_time(),
            'style_features': {
                'vocabulary': vocabulary,
                'sentence_patterns': sentence_patterns,
                'tension_markers': tension_markers,
                'emotional_expressions': emotional_expressions
            },
            'pace_metrics': pace_metrics,
            'anti_patterns': {
                'avoid_words': ANTI_PATTERNS['overused_adverbs'],
                'avoid_phrases': ANTI_PATTERNS['emotion_labels'],
                'detected': anti_patterns
            }
        }

        return style_dna

    def get_current_time(self) -> str:
        """获取当前时间"""
        from datetime import datetime
        return datetime.now().isoformat()

    def save_style_dna(self, style_dna: Dict[str, Any]):
        """保存风格 DNA"""
        # 确保目录存在
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(self.output_file, 'w', encoding='utf-8') as f:
            json.dump(style_dna, f, ensure_ascii=False, indent=2)

        print(f"\n✅ 风格 DNA 已保存到: {self.output_file}")

    def generate_report(self, style_dna: Dict[str, Any]) -> str:
        """生成分析报告"""
        report = []
        report.append("\n" + "=" * 60)
        report.append("风格 DNA 分析报告")
        report.append("=" * 60)

        # 基本信息
        report.append(f"\n📊 基本信息")
        report.append(f"  提取章节: {style_dna.get('extracted_chapters', [])}")
        report.append(f"  提取时间: {style_dna.get('extracted_at', '')}")

        # 节奏指标
        metrics = style_dna.get('pace_metrics', {})
        report.append(f"\n⚡ 节奏指标")
        report.append(f"  平均句长: {metrics.get('avg_sentence_length', 0):.1f} 字")
        report.append(f"  平均段长: {metrics.get('avg_paragraph_length', 0):.1f} 字")
        report.append(f"  对话占比: {metrics.get('dialogue_ratio', 0)*100:.1f}%")
        report.append(f"  动作占比: {metrics.get('action_ratio', 0)*100:.1f}%")
        report.append(f"  描写占比: {metrics.get('description_ratio', 0)*100:.1f}%")

        # 高频词
        vocab = style_dna.get('style_features', {}).get('vocabulary', {})
        report.append(f"\n📝 高频词 Top 10")
        for i, word in enumerate(vocab.get('high_freq_words', [])[:10], 1):
            report.append(f"  {i}. {word}")

        # 反模式检测
        anti = style_dna.get('anti_patterns', {}).get('detected', {})
        emotion_hits = anti.get('emotion_labels', [])
        adverb_hits = anti.get('overused_adverbs', [])

        if emotion_hits or adverb_hits:
            report.append(f"\n⚠️ 反模式检测")
            if emotion_hits:
                report.append(f"  情感标签: 发现 {len(emotion_hits)} 处")
                for hit in emotion_hits[:3]:
                    report.append(f"    - 第{hit['line']}行: {hit['pattern']}")
            if adverb_hits:
                report.append(f"  过度副词: 发现 {len(adverb_hits)} 处")
                for hit in adverb_hits[:3]:
                    report.append(f"    - {hit['pattern']}: {hit.get('count', 1)}次")

        report.append("\n" + "=" * 60)

        return '\n'.join(report)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='风格 DNA 提取器')

    parser.add_argument(
        '--project-root',
        type=str,
        default=os.getcwd(),
        help='项目根目录'
    )
    parser.add_argument(
        '--chapters',
        type=str,
        default='1,2,3',
        help='要分析的章节号 (逗号分隔)'
    )
    parser.add_argument(
        '--report',
        action='store_true',
        help='生成详细报告'
    )

    args = parser.parse_args()

    # 解析章节号
    chapters = [int(c.strip()) for c in args.chapters.split(',')]

    # 创建提取器
    project_root = Path(args.project_root)
    extractor = StyleDNAExtractor(project_root)

    # 提取风格 DNA
    style_dna = extractor.extract_style_dna(chapters)

    if style_dna:
        # 保存
        extractor.save_style_dna(style_dna)

        # 生成报告
        if args.report:
            print(extractor.generate_report(style_dna))
    else:
        print("❌ 风格 DNA 提取失败")
        sys.exit(1)


if __name__ == '__main__':
    main()
