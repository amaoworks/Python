"""
将华氏温度转化为摄氏温度

Version : 0.1
Author  : Brown
"""

h_Temperature = float(input('Please input HuaShi_Temperature: '))
c_Temperature = ( h_Temperature - 32 ) / 1.8
print('HuaShi_Temperature: %.2f\nSheShi_Temperature: %.2f' % (h_Temperature , c_Temperature))