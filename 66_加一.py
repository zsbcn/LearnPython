# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 66_加一.py
# Time       ：2022-11-13 21:04
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        加一(v0.0)
        :param digits: 0-9数字组成的列表
        :return: 列表代表的数字加一后对应的列表
        """
        digits.insert(0, 0)
        digits[-1] += 1
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] >= 10:
                digits[i - 1] = digits[i - 1] + (digits[i] // 10)
                digits[i] %= 10
            else:
                break
        if digits[0] == 0:
            digits.pop(0)
        return digits

    def plusOne_1(self, digits: List[int]) -> List[int]:
        """
        加一(v0.1)
        :param digits: 0-9数字组成的列表
        :return: 列表代表的数字加一后对应的列表
        """
        num = 0
        length = len(digits)
        for i in range(length):
            num += digits[length - i - 1] * 10 ** i
        num += 1
        digits = [int(i) for i in str(num)]
        return digits

    def plusOne_2(self, digits: List[int]) -> List[int]:
        """
        加一(v0.2)
        :param digits: 0-9数字组成的列表
        :return: 列表代表的数字加一后对应的列表
        """
        num = int(''.join(map(str, digits)))
        num += 1
        digits = [int(i) for i in str(num)]
        return digits


if __name__ == '__main__':
    test_digits = [8, 9, 9, 9]
    ret = Solution().plusOne_2(test_digits)
    print(ret)
