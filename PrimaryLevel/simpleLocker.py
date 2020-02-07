"""
用户身份验证

Version : 0.1
Author  : Brown
"""

username = input('Please input the username : ')
password = input('Please input the password : ')
if username == 'admin' and password == '123456':
    print('Authentication succeeded!')
else:
    print('Authentication failed!')