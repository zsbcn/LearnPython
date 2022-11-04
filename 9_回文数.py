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
        reverse_x = str(x)[::-1]
        if reverse_x == str(x):
            return True
        else:
            return False


if __name__ == '__main__':
    test_x = -121
    ret = Solution().isPalindrome(test_x)
    print(ret)
