# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 9_回文数.py
# Time       ：2022-11-5 0:02
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        判断回文数一句话版
        :param x: 输入的数字
        :return: 返回TRUE是回文数；False不是回文数
        """
        return True if str(x)[::-1] == str(x) else False

    def isPalindrome_2(self, x: int) -> bool:
        """
        判断回文数正常版
        :param x: 输入的数字
        :return: 返回TRUE是回文数；False不是回文数
        """
        reverse_x = str(x)[::-1]    # 输入x转字符串后倒序
        if reverse_x == str(x):     # 判断倒序的字符串和正序字符串是否相等？相等：是回文数，否则不是
            return True
        else:
            return False


if __name__ == '__main__':
    test_x = -121
    ret = Solution().isPalindrome(test_x)
    print(ret)
