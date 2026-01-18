"""
各种文本打乱策略的实现

LICENSE: This project is licensed under the MIT License.
Copyright (C) 2026 ZhouboLee. All rights reserved.
"""
import random
import re
from typing import Callable, List


class TextShuffleStrategies:
    """文本打乱策略集合"""
    
    @staticmethod
    def shuffle_middle(text: str) -> str:
        """策略1：词内字序颠倒（保留首尾）"""
        def shuffle_word(match):
            word = match.group()
            if len(word) >= 4:
                middle = list(word[1:-1])
                random.shuffle(middle)
                return word[0] + ''.join(middle) + word[-1]
            elif len(word) == 3:
                return word[0] + word[2] + word[1]
            return word
        
        return re.sub(r'[\u4e00-\u9fff]{2,}', shuffle_word, text)
    
    @staticmethod
    def swap_first_chars(text: str) -> str:
        """策略2：跨词首字交换（相邻词语的第一个字交换）"""
        matches = list(re.finditer(r'[\u4e00-\u9fff]{2,}', text))
        if len(matches) < 2:
            return text
        
        chars = list(text)
        used_indices = set()
        
        for i in range(len(matches) - 1):
            if random.random() > 0.5 and i not in used_indices and (i+1) not in used_indices:
                match1, match2 = matches[i], matches[i+1]
                pos1, pos2 = match1.start(), match2.start()
                chars[pos1], chars[pos2] = chars[pos2], chars[pos1]
                used_indices.update([i, i+1])
        
        return ''.join(chars)
    
    @staticmethod
    def swap_adjacent_words(text: str) -> str:
        """策略3：相邻词语颠倒（模拟口语）"""
        tokens = re.findall(r'[\u4e00-\u9fff]+|[^\u4e00-\u9fff\s]+|\s+', text)
        
        for i in range(len(tokens) - 1):
            if (re.match(r'[\u4e00-\u9fff]{2,}', tokens[i]) and 
                re.match(r'[\u4e00-\u9fff]{2,}', tokens[i+1]) and
                random.random() > 0.7):
                tokens[i], tokens[i+1] = tokens[i+1], tokens[i]
        
        return ''.join(tokens)
    
    @staticmethod
    def insert_noise(text: str) -> str:
        """策略4：随机插入干扰字符"""
        if len(text) < 10:
            return text
        
        chars = list(text)
        insert_pos = random.randint(1, len(chars) - 2)
        noise_chars = ['的', '了', '是', '在', '和', '有']
        chars.insert(insert_pos, random.choice(noise_chars))
        
        return ''.join(chars)
    
    @staticmethod
    def shuffle_punctuation(text: str) -> str:
        """策略5：标点符号移位"""
        punctuation = ['.', ',', '，', '。', '!', '！', '?', '？', ';', '；']
        punct_positions = []
        
        for i, char in enumerate(text):
            if char in punctuation:
                punct_positions.append((i, char))
        
        if len(punct_positions) < 2:
            return text
        
        chars = list(text)
        idx1, idx2 = random.sample(range(len(punct_positions)), 2)
        pos1, char1 = punct_positions[idx1]
        pos2, char2 = punct_positions[idx2]
        
        chars[pos1], chars[pos2] = char2, char1
        
        return ''.join(chars)
    
    @staticmethod
    def get_all_strategies() -> dict:
        """获取所有策略"""
        return {
            1: {"name": "词内字序颠倒", "func": TextShuffleStrategies.shuffle_middle},
            2: {"name": "跨词首字交换", "func": TextShuffleStrategies.swap_first_chars},
            3: {"name": "相邻词语颠倒", "func": TextShuffleStrategies.swap_adjacent_words},
            4: {"name": "随机插入干扰", "func": TextShuffleStrategies.insert_noise},
            5: {"name": "标点移位", "func": TextShuffleStrategies.shuffle_punctuation},
        }