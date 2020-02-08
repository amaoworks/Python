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
    number  = int(input('请输入一个数字 : '))
    if number < answer:
        print('这个数太小了！')
    elif number > answer:
        print('这个数太大了！')
    else:
        print('恭喜你，终于猜中了')
        break
print('你已经猜了 %d 次' %counter)
if counter > 7:
    print('你猜了7次都没有猜中，你真是一只猪！')