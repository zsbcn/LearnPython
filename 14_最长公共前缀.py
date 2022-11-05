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


if __name__ == '__main__':
    test_strs = ["flower", "flawer", "flvwer", "flower"]
    ret = Solution().longestCommonPrefix(test_strs)
    print(ret)
