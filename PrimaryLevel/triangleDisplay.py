"""
打印如下所示的三角形图案
->
*
**
***
****
*****

->
    *
   **
  ***
 ****
*****

->
    *
   ***
  *****
 *******
*********

Version : 0.1
Author  : Brown
"""

row = int(input('Please input the row: '))

for x in range(row):
    for y in range(x+1):
        print('*', end = '')
    print()

for x in range(row):
    for y in range(row - x - 1):
        print(' ', end = '')
    for z in range(x + 1):
        print('*', end = '')
    print()

for x in range(row):
    for y in range(row - x - 1):
        print(' ', end='')
    for z in range(2*x + 1):
        print('*', end='')
    print()