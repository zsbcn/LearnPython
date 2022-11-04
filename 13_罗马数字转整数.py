# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 13_罗马数字转整数.py
# Time       ：2022-11-5 2:14
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""


class Solution:
    _dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str) -> int:
        ls = list(s)
        print(ls)
        return 0


if __name__ == '__main__':
    test_s = 'III'
    ret = Solution().romanToInt(test_s)
    print(ret)
