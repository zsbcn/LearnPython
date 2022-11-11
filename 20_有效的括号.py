# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 20_有效的括号.py
# Time       ：2022-11-5 23:29
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        有效的括号(v0.0)
        :param s: 仅包含括号的字符串
        :return: 字符串是否有效
        """
        dict_ = {')': '(', ']': '[', '}': '{'}
        stack_ls = []
        for i in s:
            if i in ('(', '[', '{') or i in (')', ']', '}') and dict_[i] != stack_ls[-1]:
                stack_ls.append(i)
            elif i in (')', ']', '}') and dict_[i] == stack_ls[-1]:
                stack_ls.pop()
            elif i in (')', ']', '}') and not stack_ls:
                return False
        if stack_ls:
            return False
        else:
            return True

    def isValid_01(self, s: str) -> bool:
        """
        有效的括号(v0.1)
        :param s: 仅包含括号的字符串
        :return: 字符串是否有效
        """
        dict_ = {')': '(', ']': '[', '}': '{'}
        stack_ls = []
        for i in s:
            if i in ('(', '[', '{') or i in (')', ']', '}') and dict_[i] != stack_ls[-1]:
                stack_ls.append(i)
            elif dict_[i] == stack_ls[-1]:
                stack_ls.pop()
            elif not stack_ls:
                return False
        if stack_ls:
            return False
        else:
            return True


if __name__ == '__main__':
    test_s = "(])"
    ret = Solution().isValid_01(test_s)
    print(ret)
