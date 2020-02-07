"""
使用 input() 函数获取键盘输入(字符串)
使用 int() 函数将输入的字符串转换整数
使用 print() 函数输出带占位符的字符串

Version : 0.1
Author  : Brown
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d + %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))