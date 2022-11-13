# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 67_二进制求和.py
# Time       ：2022-11-13 21:41
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        二进制求和(v0.0)
        :param a: 第一个二进制数
        :param b: 第一个二进制数
        :return: 二进制结果
        """
        return bin(int(a, 2) + int(b, 2)).split('b')[-1]

    def addBinary_1(self, a: str, b: str) -> str:
        """
        二进制求和(v0.1)
        :param a: 第一个二进制数
        :param b: 第一个二进制数
        :return: 二进制结果
        """
        return str(bin(int(a, 2) + int(b, 2)))[2:]


if __name__ == '__main__':
    test_a = "11"
    test_b = "1"
    ret = Solution().addBinary_1(test_a, test_b)
    print(ret)
