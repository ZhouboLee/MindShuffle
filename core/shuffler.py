"""
文本打乱器核心类

LICENSE: This project is licensed under the MIT License.
Copyright (C) 2026 ZhouboLee. All rights reserved.
"""
from typing import List
from .strategies import TextShuffleStrategies


class ChineseTextShuffler:
    """中文文本打乱器"""
    
    def __init__(self):
        self.strategies = TextShuffleStrategies.get_all_strategies()
    
    def apply_strategies(self, text: str, strategy_ids: List[int]) -> str:
        """按顺序应用选定的策略"""
        result = text
        for strategy_id in strategy_ids:
            if 1 <= strategy_id <= len(self.strategies):
                result = self.strategies[strategy_id]["func"](result)
        return result
    
    def get_strategy_name(self, strategy_id: int) -> str:
        """获取策略名称"""
        if 1 <= strategy_id <= len(self.strategies):
            return self.strategies[strategy_id]["name"]
        return f"未知策略[{strategy_id}]"