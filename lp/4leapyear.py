def is_run(year):
    if year % 4 == 0 and year % 100 != 0:  # 普通闰年
        print('yes')
    elif year % 400 == 0:  # 世纪闰年
        print('yes')
    else:
        print('no')


year = eval(input('please input a year!'))
is_run(year)
