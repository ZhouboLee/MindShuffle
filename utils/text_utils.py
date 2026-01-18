"""
文本处理工具函数

LICENSE: This project is licensed under the MIT License.
Copyright (C) 2026 ZhouboLee. All rights reserved.
"""
import re


class TextUtils:
    """文本工具类"""
    
    @staticmethod
    def is_chinese_char(char: str) -> bool:
        """判断字符是否为中文"""
        return '\u4e00' <= char <= '\u9fff'
    
    @staticmethod
    def extract_chinese_words(text: str) -> list:
        """提取中文词语"""
        return re.findall(r'[\u4e00-\u9fff]+', text)
    
    @staticmethod
    def split_preserving_punctuation(text: str) -> list:
        """分割文本，保留标点"""
        return re.findall(r'[\u4e00-\u9fff]+|[^\u4e00-\u9fff\s]+|\s+', text)