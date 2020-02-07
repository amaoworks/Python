"""
猜数字游戏
计算机出一个 1~100 之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

Version : 0.1
Author  : Brown
"""

import random

answer  = random.randint(1 ,100 )
counter = 0
while True:
    counter += 1
    number  = int(input('Please a number : '))
    if number < answer:
        print('It is Small!')
    elif number > answer:
        print('It is Big!')
    else:
        print('Congratulations, you guessed it!')
        break
print('You have guess %d time(es)' %counter)
if counter > 7:
    print('Obviously, you have insufficient IQ!')