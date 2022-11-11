# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 26_删除有序数组中的重复项.py
# Time       ：2022-11-11 20:24
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 0
        for i in range(len(nums)):
            if nums[length] != nums[i]:
                nums[length + 1] = nums[i]
                length += 1
        return length+1


if __name__ == '__main__':
    test_nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ret = Solution().removeDuplicates(test_nums)
    print(ret)
