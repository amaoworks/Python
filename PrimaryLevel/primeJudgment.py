"""
输入一个正整数判断是否为素数

Version : 0.1
Author  : Brown
"""

inputNumber = int(input('Please input a Positive integer : '))
counter     = 0
for x in range(1 , inputNumber + 1, 1):
    if (inputNumber % x) == 0:
        counter+=1
if counter == 2:
    print('It is a prime!')
else:
    print('It is not a prime!')