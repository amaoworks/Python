"""
生成斐波那契数列的前20个数

Version : 0.1
Author  : Brown
"""

for x in range(0, 20, 1):
    if x < 2:
        back = 1
        now  = 1
        print(now)
    else:
        mid  = now
        now += back
        back = mid
        print(now)
