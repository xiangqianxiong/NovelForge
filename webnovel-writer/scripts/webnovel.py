#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Webnovel Writing Assistant - CLI Tool
网文创作助手 - 命令行工具

提供项目管理、队列管理、风格提取等功能
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Any

# 配置路径
PROJECT_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = Path(__file__).parent


class Colors:
    """终端颜色输出"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def color(text: str, color_code: str) -> str:
    """给文本添加颜色"""
    return f"{color_code}{text}{Colors.ENDC}"


def load_state(project_root: Path) -> Dict[str, Any]:
    """加载项目状态"""
    state_file = project_root / ".webnovel" / "state.json"
    if state_file.exists():
        with open(state_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_state(project_root: Path, state: Dict[str, Any]):
    """保存项目状态"""
    state_file = project_root / ".webnovel" / "state.json"
    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def cmd_init(args):
    """初始化项目命令"""
    project_root = Path(args.project_root or os.getcwd())

    # 创建目录结构
    directories = [
        ".webnovel",
        ".webnovel/backups",
        ".webnovel/archive",
        ".webnovel/summaries",
        "设定集",
        "大纲",
        "正文",
        "审查报告"
    ]

    for directory in directories:
        dir_path = project_root / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"创建目录: {directory}")

    # 创建初始状态文件
    state = {
        "project_info": {
            "title": args.title or "未命名小说",
            "genre": args.genre or "玄幻修仙",
            "created_at": datetime.now().isoformat(),
            "target_words": args.target_words or 2000000,
            "target_chapters": args.target_chapters or 600,
            "style_references": args.style.split(',') if args.style else []
        },
        "progress": {
            "current_chapter": 0,
            "total_words": 0,
            "current_volume": 1
        },
        "protagonist_state": {
            "name": args.protagonist or "主角",
            "power": {"realm": "凡人", "layer": 1}
        },
        "strand_tracker": {
            "last_quest_chapter": 0,
            "last_fire_chapter": 0,
            "last_constellation_chapter": 0
        },
        "style_settings": {
            "current_style": args.style.split(',')[0] if args.style else "网文",
            "mix_ratio": {},
            "custom_rules": []
        }
    }

    save_state(project_root, state)

    # 创建模板文件
    templates = {
        "设定集/世界观.md": "# 世界观设定\n\n## 世界背景\n\n## 社会结构\n\n## 主要势力\n",
        "设定集/力量体系.md": "# 力量体系\n\n## 境界划分\n\n## 能力类型\n",
        "设定集/主角卡.md": f"# 主角：{args.protagonist or '主角'}\n\n## 基本信息\n\n## 性格特点\n\n## 成长轨迹\n",
        "大纲/总纲.md": "# 总纲\n\n## 第一卷\n\n### 主线\n\n### 支线\n",
    }

    for file_path, content in templates.items():
        full_path = project_root / file_path
        if not full_path.exists():
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"创建文件: {file_path}")

    print(color("\n✅ 项目初始化完成！", Colors.GREEN))
    print(f"项目路径: {project_root}")


def cmd_status(args):
    """查看项目状态"""
    project_root = Path(args.project_root or os.getcwd())
    state = load_state(project_root)

    if not state:
        print(color("❌ 未找到项目状态文件，请先初始化项目", Colors.RED))
        return

    print(color("\n📖 项目状态报告", Colors.HEADER))
    print("=" * 60)

    # 项目信息
    info = state.get('project_info', {})
    print(f"\n{color('项目信息', Colors.BOLD)}")
    print(f"  书名: {info.get('title', '未命名')}")
    print(f"  题材: {info.get('genre', '未知')}")
    print(f"  创建时间: {info.get('created_at', '未知')}")
    print(f"  目标字数: {info.get('target_words', 0):,} 字")
    print(f"  目标章节: {info.get('target_chapters', 0)} 章")

    # 进度信息
    progress = state.get('progress', {})
    print(f"\n{color('写作进度', Colors.BOLD)}")
    print(f"  当前章节: 第 {progress.get('current_chapter', 0)} 章")
    print(f"  总字数: {progress.get('total_words', 0):,} 字")
    print(f"  当前卷: 第 {progress.get('current_volume', 1)} 卷")

    # 主角状态
    protagonist = state.get('protagonist_state', {})
    print(f"\n{color('主角状态', Colors.BOLD)}")
    print(f"  姓名: {protagonist.get('name', '未知')}")
    power = protagonist.get('power', {})
    print(f"  境界: {power.get('realm', '凡人')} (第 {power.get('layer', 1)} 层)")

    # 风格设置
    style = state.get('style_settings', {})
    print(f"\n{color('风格设置', Colors.BOLD)}")
    print(f"  当前风格: {style.get('current_style', '默认')}")
    refs = info.get('style_references', [])
    if refs:
        print(f"  参考风格: {', '.join(refs)}")


def cmd_queue_create(args):
    """创建批量写作队列"""
    project_root = Path(args.project_root or os.getcwd())
    queue_file = project_root / ".webnovel" / "queue_state.json"

    queue = {
        "version": "1.0",
        "queue_id": f"queue-{datetime.now().strftime('%Y%m%d%H%M')}",
        "created_at": datetime.now().isoformat(),
        "config": {
            "start_chapter": args.start,
            "end_chapter": args.end,
            "auto_continue": args.auto,
            "stop_on_blocking": args.stop,
            "auto_validate": True,
            "auto_regression": True,
            "auto_emotion": False
        },
        "progress": {
            "current_chapter": args.start,
            "completed": 0,
            "total": args.end - args.start + 1,
            "failed": 0,
            "skipped": 0
        },
        "chapters": [
            {
                "chapter": i,
                "status": "pending"
            }
            for i in range(args.start, args.end + 1)
        ],
        "stats": {
            "avg_duration_seconds": 0,
            "success_rate": 1.0,
            "total_words": 0
        }
    }

    with open(queue_file, 'w', encoding='utf-8') as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)

    print(color(f"\n✅ 队列创建成功！", Colors.GREEN))
    print(f"队列ID: {queue['queue_id']}")
    print(f"章节范围: 第 {args.start} - {args.end} 章")
    print(f"总章节数: {queue['progress']['total']} 章")


def cmd_queue_status(args):
    """查看队列状态"""
    project_root = Path(args.project_root or os.getcwd())
    queue_file = project_root / ".webnovel" / "queue_state.json"

    if not queue_file.exists():
        print(color("❌ 没有活跃的队列", Colors.RED))
        return

    with open(queue_file, 'r', encoding='utf-8') as f:
        queue = json.load(f)

    config = queue.get('config', {})
    progress = queue.get('progress', {})
    chapters = queue.get('chapters', [])

    print(color(f"\n📋 批量写作队列 [第{config['start_chapter']}-{config['end_chapter']}章]", Colors.HEADER))
    print("=" * 60)

    # 进度条
    completed = progress.get('completed', 0)
    total = progress.get('total', 1)
    percentage = completed / total
    bar_length = 40
    filled = int(bar_length * percentage)
    bar = '█' * filled + '░' * (bar_length - filled)

    print(f"\n进度: {completed}/{total} 章节 [{bar}] {percentage*100:.1f}%")

    # 章节详细状态
    print(f"\n{color('章节状态:', Colors.BOLD)}")
    status_symbols = {
        'committed': color('✓', Colors.GREEN),
        'writing': color('▶', Colors.YELLOW),
        'failed': color('✗', Colors.RED),
        'pending': color('○', Colors.CYAN)
    }

    for ch in chapters:
        chapter = ch['chapter']
        status = ch['status']
        symbol = status_symbols.get(status, '?')

        if status == 'committed':
            completed_at = ch.get('completed_at', '')
            duration = ch.get('duration_seconds', 0)
            print(f"  {symbol} 第{chapter:03d}章 - 已完成 ({completed_at[:16]} - {duration}s)")
        elif status == 'writing':
            print(f"  {symbol} 第{chapter:03d}章 - 写作中...")
        elif status == 'failed':
            reason = ch.get('error', '未知错误')
            print(f"  {symbol} 第{chapter:03d}章 - 失败 ({reason})")
        else:
            print(f"  {symbol} 第{chapter:03d}章 - 等待中")

    # 统计信息
    stats = queue.get('stats', {})
    print(f"\n{color('统计:', Colors.BOLD)}")
    print(f"  平均耗时: {stats.get('avg_duration_seconds', 0):.0f}s/章")
    print(f"  成功率: {stats.get('success_rate', 0)*100:.1f}%")
    print(f"  总字数: {stats.get('total_words', 0):,}")


def cmd_queue_pause(args):
    """暂停队列"""
    project_root = Path(args.project_root or os.getcwd())
    queue_file = project_root / ".webnovel" / "queue_state.json"

    if not queue_file.exists():
        print(color("❌ 没有活跃的队列", Colors.RED))
        return

    with open(queue_file, 'r', encoding='utf-8') as f:
        queue = json.load(f)

    queue['status'] = 'paused'
    queue['paused_at'] = datetime.now().isoformat()

    with open(queue_file, 'w', encoding='utf-8') as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)

    print(color("⏸ 队列已暂停", Colors.YELLOW))


def cmd_queue_resume(args):
    """继续队列"""
    project_root = Path(args.project_root or os.getcwd())
    queue_file = project_root / ".webnovel" / "queue_state.json"

    if not queue_file.exists():
        print(color("❌ 没有活跃的队列", Colors.RED))
        return

    with open(queue_file, 'r', encoding='utf-8') as f:
        queue = json.load(f)

    if queue.get('status') != 'paused':
        print(color("❌ 队列不在暂停状态", Colors.RED))
        return

    queue['status'] = 'running'
    queue['resumed_at'] = datetime.now().isoformat()

    with open(queue_file, 'w', encoding='utf-8') as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)

    print(color("▶ 队列已继续", Colors.GREEN))


def cmd_queue_stop(args):
    """停止队列"""
    project_root = Path(args.project_root or os.getcwd())
    queue_file = project_root / ".webnovel" / "queue_state.json"

    if not queue_file.exists():
        print(color("❌ 没有活跃的队列", Colors.RED))
        return

    queue_file.unlink()
    print(color("■ 队列已停止", Colors.RED))


def cmd_style_get_history(args):
    """获取章节修改历史"""
    project_root = Path(args.project_root or os.getcwd())
    chapter = args.chapter

    # 查找章节文件
    chapter_files = list(project_root.glob(f"正文/第{chapter:04d}章-*.md"))

    if not chapter_files:
        print(color(f"❌ 未找到第 {chapter} 章", Colors.RED))
        return

    chapter_file = chapter_files[0]

    # 提取修改模式（示例）
    result = {
        "chapter": chapter,
        "file": str(chapter_file),
        "revisions": [
            {
                "timestamp": datetime.now().isoformat(),
                "before": "示例：缓缓地站起身来",
                "after": "站起身",
                "pattern": "删除了'缓缓地'"
            }
        ],
        "user_preferences": {
            "no_emotion_labels": True,
            "no_adverbs": ["缓缓地", "淡淡地", "微微地"],
            "prefer_physiological_reactions": True
        }
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='网文创作助手 - 命令行工具',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--project-root',
        help='项目根目录 (默认: 当前目录)'
    )

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # init 命令
    init_parser = subparsers.add_parser('init', help='初始化项目')
    init_parser.add_argument('--title', help='书名')
    init_parser.add_argument('--genre', help='题材')
    init_parser.add_argument('--protagonist', help='主角名')
    init_parser.add_argument('--target-words', type=int, help='目标字数')
    init_parser.add_argument('--target-chapters', type=int, help='目标章节数')
    init_parser.add_argument('--style', help='参考风格 (逗号分隔)')
    init_parser.set_defaults(func=cmd_init)

    # status 命令
    status_parser = subparsers.add_parser('status', help='查看项目状态')
    status_parser.set_defaults(func=cmd_status)

    # queue 子命令
    queue_parser = subparsers.add_parser('queue', help='队列管理')
    queue_subparsers = queue_parser.add_subparsers(dest='queue_command')

    # queue create
    queue_create = queue_subparsers.add_parser('create', help='创建队列')
    queue_create.add_argument('--start', type=int, required=True, help='起始章节')
    queue_create.add_argument('--end', type=int, required=True, help='结束章节')
    queue_create.add_argument('--auto', action='store_true', help='自动模式')
    queue_create.add_argument('--stop', action='store_true', help='遇错即停')
    queue_create.set_defaults(func=cmd_queue_create)

    # queue status
    queue_status = queue_subparsers.add_parser('status', help='查看队列状态')
    queue_status.set_defaults(func=cmd_queue_status)

    # queue pause
    queue_pause = queue_subparsers.add_parser('pause', help='暂停队列')
    queue_pause.set_defaults(func=cmd_queue_pause)

    # queue resume
    queue_resume = queue_subparsers.add_parser('resume', help='继续队列')
    queue_resume.set_defaults(func=cmd_queue_resume)

    # queue stop
    queue_stop = queue_subparsers.add_parser('stop', help='停止队列')
    queue_stop.set_defaults(func=cmd_queue_stop)

    # style 子命令
    style_parser = subparsers.add_parser('style', help='风格管理')
    style_subparsers = style_parser.add_subparsers(dest='style_command')

    # style get-history
    style_history = style_subparsers.add_parser('get-history', help='获取修改历史')
    style_history.add_argument('--chapter', type=int, required=True, help='章节号')
    style_history.set_defaults(func=cmd_style_get_history)

    # 解析参数
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    # 执行命令
    args.func(args)


if __name__ == '__main__':
    main()
