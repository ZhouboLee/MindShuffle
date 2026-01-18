"""
系统工具函数

LICENSE: This project is licensed under the MIT License.
Copyright (C) 2026 ZhouboLee. All rights reserved.
"""
import os
import platform


class SystemUtils:
    """系统工具类"""
    
    @staticmethod
    def clear_screen():
        """跨平台清屏"""
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    @staticmethod
    def pause():
        """等待用户按键"""
        input("按任意键继续...")