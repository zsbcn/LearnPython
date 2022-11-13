# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 58_最后一个单词的长度.py
# Time       ：2022-11-12 22:51
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        最后一个单词的长度
        :param s: 若干单词和空格组成的字符串
        :return: 最后一个单词的长度
        """
        return len(s.strip().split()[-1])


if __name__ == '__main__':
    test_s = "Hello World"
    ret = Solution().lengthOfLastWord(test_s)
    print(ret)
