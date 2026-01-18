"""
配置管理器

LICENSE: This project is licensed under the MIT License.
Copyright (C) 2026 ZhouboLee. All rights reserved.
"""
import toml
from pathlib import Path
from typing import Dict, Any


class ConfigManager:
    def __init__(self, config_file: str = "mnds-config.toml"):
        self.config_file = Path(config_file)
        self.config = self._get_default_config()
        self._load_config()
    
    def _get_default_config(self) -> Dict[str, str]:
        """获取默认配置"""
        return {
            "show_comparison": "off",      # 展示对比
            "show_strategies": "off",      # 展示已选择的策略
            "show_original": "on",         # 打乱后展示原句
            "clear_screen": "on",          # 每次生成前清屏
            "default_text": "你说的对，但是《原神》是由米哈游自主研发的一款全新开放世界冒险游戏。",  # 默认文本
        }
    
    def _load_config(self):
        """加载配置文件"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = toml.load(f)
                    # 合并配置，用户配置覆盖默认配置
                    for key in self.config:
                        if key in loaded_config:
                            value = str(loaded_config[key]).lower()
                            if value in ["on", "off"]:
                                self.config[key] = value
                            else:
                                self.config[key] = value
            except Exception as e:
                print(f"[WARN] 配置文件加载失败，使用默认配置 ({e})")
        else:
            self._create_default_config()
    
    def _create_default_config(self):
        """创建默认配置文件"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                toml.dump(self.config, f)
            print(f"[INFO] 已创建默认配置文件: {self.config_file}")
        except Exception as e:
            print(f"[WARN] 无法创建配置文件 ({e})")
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值"""
        return self.config.get(key, default)
    
    def is_enabled(self, key: str) -> bool:
        """检查功能是否开启"""
        return self.get(key, "off").lower() == "on"
    
    def show_config_status(self):
        """显示当前配置状态"""
        print("当前配置状态:")
        config_names = {
            "show_comparison": "展示对比",
            "show_strategies": "展示策略",
            "show_original": "展示原句",
            "clear_screen": "清屏功能",
        }

        for key, cn_name in config_names.items():
            value = self.get(key)
            status = "[ON] 开启" if self.is_enabled(key) else "[OFF] 关闭"
            print(f"  {cn_name}: {status}")

        default_text = self.get("default_text", "")
        if default_text and len(default_text) > 30:
            default_text = default_text[:30] + "..."
        print(f"  默认文本: {default_text}")
        print()