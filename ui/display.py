"""
显示功能模块

LICENSE: This project is licensed under the MIT License.
Copyright (C) 2026 ZhouboLee. All rights reserved.
"""
from typing import Tuple, List


class DisplayUtils:
    """显示工具类"""
    
    @staticmethod
    def compare_texts(original: str, shuffled: str) -> List[Tuple[int, str, str]]:
        """对比两个文本的差异"""
        differences = []
        max_len = max(len(original), len(shuffled))
        
        for i in range(max_len):
            orig_char = original[i] if i < len(original) else ' '
            shuff_char = shuffled[i] if i < len(shuffled) else ' '
            
            if orig_char != shuff_char:
                differences.append((i + 1, orig_char, shuff_char))
        
        return differences
    
    @staticmethod
    def show_differences(differences: List[Tuple[int, str, str]]):
        """显示差异"""
        if not differences:
            print("  （无变化）")
            return
        
        print("对比（不同之处）：")
        for pos, orig, shuff in differences:
            print(f"  位置{pos}: '{orig}' → '{shuff}'")
    
    @staticmethod
    def show_strategies(shuffler, strategy_ids: List[int]):
        """显示选择的策略"""
        if not strategy_ids:
            return
        
        print("选择的策略：", end="")
        for sid in strategy_ids:
            print(f"[{sid}] {shuffler.get_strategy_name(sid)} ", end="")
        print()