# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : 69_x的平方根.py
# Time       ：2022-11-18 20:44
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        x的平方根(v0.0), 此版本使用暴力计算
        :param x: 待求平方根的数x
        :return: x的平方根的整数部分
        """
        for i in range(x + 1):
            temp = i * i
            if temp > x:
                return i - 1
            elif temp == x:
                return i

    def mySqrt_1(self, x: int) -> int:
        """
        x的平方根(v0.1), 此版本使用了二分查找
        :param x: 待求平方根的数x
        :return: x的平方根的整数部分
        """
        head = 0
        tail = x
        temp = -1
        while head <= tail:
            mid = head + (tail - head) // 2
            if mid ** 2 <= x:
                temp = mid
                head = mid + 1
            else:
                tail = mid - 1
        return temp

    def mySqrt_2(self, x: int) -> int:
        """
        x的平方根(v0.2), 此版本使用了数学方法计算平方根,要注意浮点数的计算精度,还需要导入math库
        :param x: 待求平方根的数x
        :return: x的平方根的整数部分
        """
        if x == 0:
            return 0
        result = int(math.e ** (0.5 * math.log(x)))
        return result + 1 if (result + 1) ** 2 <= x else result


if __name__ == '__main__':
    test_x = 4
    ret = Solution().mySqrt_2(test_x)
    print(ret)
