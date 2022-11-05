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
    def romanToInt(self, s: str) -> int:
        """
        罗马数字转整数
        :param s: 输入一个罗马字符串
        :return: 输出对应的数字
        """
        dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40,
                      'XC': 90, 'CD': 400, 'CM': 900}
        sums = 0
        index = 0
        while index < len(s):
            temp = s[index:index + 2]
            if temp in dict_roman:
                index += 2
            else:
                temp = s[index]
                index += 1
            sums += dict_roman[temp]
        return sums


if __name__ == '__main__':
    test_s = 'MCMXCIV'
    ret = Solution().romanToInt(test_s)
    print(ret)
