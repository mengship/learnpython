"""
同一个缩进为一个整体代码块
4个空格为一个缩进

身份验证小case
Version 0.1
Author 王昱棋
"""

username = input('请输入用户名： ')
password = input('请输入口令： ')
# 用户名是admin且密码是123456则身份验证成功否则身份验证失败
if username == 'admin' and password == '123456':
    print('身份验证成功！')
else:
    print('身份验证失败！')

