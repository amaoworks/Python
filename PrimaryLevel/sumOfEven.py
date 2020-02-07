"""
用 for 循环实现 1~100 之间的偶数求和

Version : 0.1
Author  : Brown
"""

sum = 0
for x in range(0 ,101 ,2 ):
    sum += x
print('The sum is %d' %sum)