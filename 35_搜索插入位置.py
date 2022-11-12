# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 35_搜索插入位置.py
# Time       ：2022-11-11 22:21
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        搜索插入位置(v0.0)
        :param nums: 有序类别
        :param target: 搜索目标值
        :return: 目标值应该插入的下标
        """
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (tail - head) // 2 + head
            if target < nums[mid]:
                tail = mid - 1
            elif nums[mid] < target:
                head = mid + 1
            else:
                return mid
        return tail + 1


if __name__ == '__main__':
    test_nums = [1, 3, 5]
    test_target = 4
    ret = Solution().searchInsert(test_nums, test_target)
    print(ret)
