import random
import string

count = eval(input('please input num:'))
src = string.ascii_letters + string.digits
list_passwd = []
for i in range(count):
    passwd = random.sample(src, 5)
    passwd.extend(random.sample(string.digits, 1))
    passwd.extend(random.sample(string.ascii_lowercase, 1))
    passwd.extend(random.sample(string.ascii_uppercase, 1))
    random.shuffle(passwd)  # 打乱字符顺序
    if passwd not in list_passwd:
        list_passwd.append(passwd)
print(list_passwd)
