"""
输入两个正整数，计算他们的最大公约数和最小公倍数

Version : 0.1
Author  : Brown
"""

x = int(input('Please input a positive integer : '))
y= int(input('Please input anther positive integer : '))

if x > y:
    x, y = y, x

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('The Greatest common divisor is : %d' %factor)
        print('The Least common multiple is : %d' %(x * y // factor))
        break