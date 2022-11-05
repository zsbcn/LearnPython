# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 14_最长公共前缀.py
# Time       ：2022-11-5 21:47
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        最长公共前缀(v0.0)
        :param strs: 字符串列表
        :return: 最长的公共前缀，若无返回空字符串
        """
        strs = list(set(strs))
        out_str = strs[-1]
        for i in strs:
            if len(i) < len(out_str):
                out_str = i
        length = len(out_str)
        flag = True
        while flag:
            for i in strs:
                if i[:length] != out_str:
                    out_str = out_str[:-1]
                    length = len(out_str)
                    break
                elif i == strs[-1] or out_str == '':
                    flag = False
        return out_str

    def longestCommonPrefix_v01(self, strs: List[str]) -> str:
        """
        最长公共前缀(v0.1)
        :param strs: 字符串列表
        :return: 最长的公共前缀，若无返回空字符串
        """
        strs = set(strs)
        out_str = ''
        for i in zip(*strs):
            if len(set(i)) != 1:
                break
            else:
                out_str = f'{out_str}{i[0]}'
        return out_str

    def longestCommonPrefix_v02(self, strs: List[str]) -> str:
        """
        最长公共前缀(v0.2)
        :param strs: 字符串列表
        :return: 最长的公共前缀，若无返回空字符串
        """
        strs = set(strs)
        index = 0
        for index, value in enumerate(zip(*strs)):
            if len(set(value)) != 1:
                break
            else:
                index += 1
        return strs.pop()[:index]


if __name__ == '__main__':
    test_strs = ["a"]
    ret = Solution().longestCommonPrefix_v02(test_strs)
    print(ret)
