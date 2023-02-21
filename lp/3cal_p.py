import numpy as np


def cal_p(num_total):
    num_circle = 0
    x_list = []
    y_list = []
    for _ in range(num_total):
        rand_x = np.random.uniform(0, 1, size=1)
        rand_y = np.random.uniform(0, 1, size=1)
        x_list.append(rand_x)
        y_list.append(rand_y)
        if np.add(rand_x ** 2, rand_y ** 2) <= 1:
            num_circle += 1
    p = 4 * float(num_circle) / float(num_total)
    return p


num = eval(input('input a num:'))
p = cal_p(num)
print(p)
