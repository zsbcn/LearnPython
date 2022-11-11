# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 27_移除元素.py
# Time       ：2022-11-11 21:58
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        移除元素(v0.0)
        :param nums: 输入数组
        :param val: 待删除的数字
        :return: 剩余数组长度
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == '__main__':
    test_nums = [0, 1, 2, 2, 3, 0, 4, 2]
    test_val = 2
    ret = Solution().removeElement(test_nums, test_val)
    print(ret)
