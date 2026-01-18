"""
终端用户界面

LICENSE: This project is licensed under the MIT License.
Copyright (C) 2026 ZhouboLee. All rights reserved.
"""
from typing import List
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config_manager import ConfigManager
from core.shuffler import ChineseTextShuffler
from ui.display import DisplayUtils
from utils.system_utils import SystemUtils


class TerminalUI:
    """终端用户界面管理器"""

    def __init__(self):
        self.config = ConfigManager()
        self.shuffler = ChineseTextShuffler()
        self.display = DisplayUtils()
        self.system = SystemUtils()
    
    def show_title(self):
        """显示标题"""
        print("="*50)
        print("中文文本轻度打乱生成器")
        print("="*50)
    
    def show_strategy_menu(self):
        """显示策略菜单"""
        print("\n" + "="*50)
        print("可选的打乱策略：")
        for idx, info in self.shuffler.strategies.items():
            print(f"  [{idx}] {info['name']}")
        print("="*50)
        print("提示：输入多个编号（用空格分隔）可组合使用")
        print("示例：1 3 表示先使用策略1，再使用策略3")
        print("="*50)
    
    def get_user_input(self) -> str:
        """获取用户输入的文本"""
        prompt = "输入需要打乱的句子 > "
        text = input(prompt).strip()

        # 检查是否为命令
        if text.startswith('/'):
            should_pause = self.handle_command(text)
            # 如果命令需要暂停（如帮助或配置命令），则暂停一下让用户阅读
            if should_pause:
                input("\n按 Enter 键继续...")
            return None  # 返回None表示这是一个命令，不是普通输入

        if not text and self.config.get("default_text"):
            text = self.config.get("default_text")
            print(f"使用默认句子：{text[:50]}{'...' if len(text) > 50 else ''}")

        return text

    def handle_command(self, command: str):
        """处理命令，返回是否需要暂停"""
        if command == '/help':
            self.show_help()
            return True  # 需要暂停
        elif command == '/quit':
            self.quit_program()
        elif command == '/config':
            self.show_config_info()
            return True  # 需要暂停
        elif command == '/change-default-text':
            self.change_default_text()
            return True  # 需要暂停
        elif command == '/reset':
            self.reset_default_text()
            return True  # 需要暂停
        else:
            print(f"未知命令: {command}，输入 /help 查看可用命令")
        return False  # 不需要暂停

    def show_help(self):
        """显示帮助信息"""
        print("\n" + "="*50)
        print("可用命令:")
        print("  /help               - 显示此帮助信息")
        print("  /quit               - 退出程序")
        print("  /config             - 显示当前配置信息")
        print("  /change-default-text - 更改默认文本")
        print("  /reset              - 重置默认文本为初始值")
        print("  输入文本            - 对输入的文本进行打乱处理")
        print("="*50)

    def quit_program(self):
        """退出程序"""
        print("\n程序已退出，再见！")
        exit(0)

    def show_config_info(self):
        """显示配置信息"""
        print("\n" + "="*50)
        print("当前配置信息:")
        config_names = {
            "show_comparison": "展示对比",
            "show_strategies": "展示策略",
            "show_original": "展示原句",
            "clear_screen": "清屏功能",
        }

        for key, cn_name in config_names.items():
            value = self.config.get(key)
            status = "[ON] 开启" if self.config.is_enabled(key) else "[OFF] 关闭"
            print(f"  {cn_name}: {status}")

        default_text = self.config.get("default_text", "")
        if default_text and len(default_text) > 30:
            default_text = default_text[:30] + "..."
        print(f"  默认文本: {default_text}")
        print(f"\n配置文件路径: {self.config.config_file}")
        print("="*50)

    def change_default_text(self):
        """更改默认文本"""
        print("\n" + "="*50)
        print("更改默认文本")
        print("当前默认文本:")
        current_text = self.config.get("default_text", "")
        if len(current_text) > 50:
            print(f"  {current_text[:50]}...")
        else:
            print(f"  {current_text}")

        print("\n请选择操作:")
        print("  1. 使用更长的句子")
        print("  2. 使用自定义句子")
        print("  3. 取消")

        choice = input("\n请输入选项编号 (1-3): ").strip()

        if choice == "1":
            # 使用更长的句子
            long_text = "你说的对，但是《原神》是由米哈游自主研发的一款全新开放世界冒险游戏。游戏发生在一个被称作「提瓦特」的幻想世界，在这里，被神选中的人将被授予「神之眼」，导引元素之力。你将扮演一位名为「旅行者」的神秘角色在自由的旅行中邂逅性格各异、能力独特的同伴们，和他们一起击败强敌，找回失散的亲人——同时，逐步发掘「原神」的真相。因为你的素养很差，我现在每天玩原神都能赚150原石，每个月差不多5000原石的收入， 也就是现实生活中每个月5000美元的收入水平，换算过来最少也30000人民币，虽然我 只有14岁，但是已经超越了中国绝大多数人(包括你)的水平，这便是原神给我的骄傲的资本。毫不夸张地说，《原神》是miHoYo迄今为止规模最为宏大，也是最具野心的一部作品。即便在经历了8700个小时的艰苦战斗后，游戏还有许多尚未发现的秘密，错过的武器与装备，以及从未使用过的法术和技能。尽管游戏中的战斗体验和我们之前在烧机系列游戏所见到的没有多大差别，但游戏中各类精心设计的敌人以及Boss战已然将战斗抬高到了一个全新的水平。就和几年前的《 塞尔达传说 》一样，《原神》也是一款能够推动同类游戏向前发展的优秀作品。"
            self._update_default_text(long_text, "长句子")
        elif choice == "2":
            # 使用自定义句子
            print("\n请输入新的默认文本:")
            custom_text = input().strip()
            if custom_text:
                self._update_default_text(custom_text, "自定义句子")
            else:
                print("未输入任何内容，未做更改。")
        elif choice == "3":
            # 取消
            print("操作已取消。")
        else:
            print("无效选项，操作已取消。")

        print("="*50)

    def _update_default_text(self, new_text, text_type):
        """更新默认文本的辅助方法"""
        # 更新配置
        self.config.config["default_text"] = new_text

        # 保存到配置文件
        import toml
        from pathlib import Path
        config_file_path = Path(self.config.config_file)
        try:
            with open(config_file_path, 'w', encoding='utf-8') as f:
                toml.dump(self.config.config, f)
            print(f"\n✓ {text_type}已设置为默认文本！")
        except Exception as e:
            print(f"\n✗ 保存配置失败: {e}")

    def reset_default_text(self):
        """重置默认文本为初始值"""
        print("\n" + "="*50)
        print("重置默认文本")
        print("确认要将默认文本重置为初始值吗？")
        confirm = input("输入 'yes' 确认，其他任意键取消: ")

        if confirm.lower() == 'yes':
            # 从默认配置中获取原始默认文本
            from config.config_manager import ConfigManager
            default_config = ConfigManager()._get_default_config()
            original_default_text = default_config["default_text"]

            # 更新配置
            self.config.config["default_text"] = original_default_text

            # 保存到配置文件
            import toml
            from pathlib import Path
            config_file_path = Path(self.config.config_file)
            try:
                with open(config_file_path, 'w', encoding='utf-8') as f:
                    toml.dump(self.config.config, f)
                print(f"\n✓ 默认文本已重置为初始值！")
            except Exception as e:
                print(f"\n✗ 保存配置失败: {e}")
        else:
            print("操作已取消。")
        print("="*50)
    
    def get_strategy_choice(self) -> List[int]:
        """获取用户选择的策略"""
        while True:
            try:
                choice = input("\n打乱方式 > ").strip()
                if not choice:
                    return [1]  # 默认使用策略1
                
                strategy_ids = [int(x) for x in choice.split()]
                if all(1 <= sid <= len(self.shuffler.strategies) for sid in strategy_ids):
                    return strategy_ids
                else:
                    print(f"请输入1-{len(self.shuffler.strategies)}之间的数字")
            except ValueError:
                print("输入无效，请用空格分隔数字，如：1 2 3")
    
    def process_text(self, text: str, strategy_ids: List[int]):
        """处理文本并显示结果"""
        # 显示原句
        if self.config.is_enabled("show_original"):
            print("\n" + "-"*50)
            print("原句：")
            print(f"  {text}")
            print()
        
        # 显示策略信息
        if self.config.is_enabled("show_strategies"):
            self.display.show_strategies(self.shuffler, strategy_ids)
        
        # 应用策略并显示结果
        print("打乱后：")
        shuffled_text = self.shuffler.apply_strategies(text, strategy_ids)
        print(f"  {shuffled_text}")
        
        # 显示对比
        if self.config.is_enabled("show_comparison"):
            print("\n" + "-"*50)
            differences = self.display.compare_texts(text, shuffled_text)
            self.display.show_differences(differences)
    
    def run(self):
        """运行主循环"""
        try:
            while True:
                # 清屏
                if self.config.is_enabled("clear_screen"):
                    self.system.clear_screen()

                # 显示标题
                self.show_title()

                # 获取输入
                text = self.get_user_input()

                # 如果是命令，则跳过后续处理
                if text is None:
                    continue

                # 显示菜单
                self.show_strategy_menu()

                # 获取策略选择
                strategy_ids = self.get_strategy_choice()

                # 处理文本
                self.process_text(text, strategy_ids)

                # 显示结束信息
                print("\n" + "="*50)
                print("输入 /help 查看可用命令")

                # 等待继续
                input("\n按 Enter 键继续生成新句子，或按 Ctrl+C 退出...")

        except KeyboardInterrupt:
            print("\n\n程序结束（用户终止）")