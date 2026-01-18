#!/usr/bin/env python3
"""
MindShuffle 主程序入口
中文文本轻度打乱生成器

LICENSE: This project is licensed under the MIT License.
Copyright (C) 2026 ZhouboLee. All rights reserved.
"""
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.terminal_ui import TerminalUI


def main():
    """主函数"""
    # 检查依赖
    try:
        import toml
    except ImportError:
        print("错误：未安装toml库，请先安装：")
        print("  pip install toml")
        sys.exit(1)

    # 启动程序
    ui = TerminalUI()
    ui.run()


if __name__ == "__main__":
    main()
