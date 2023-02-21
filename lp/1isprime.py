def isprime(num):
    if num < 2:
        print('illegal')
        return
    for i in range(2, num):
        if num % i == 0:
            print('not prime')
            return
    print('is prime')


try:
    num = eval(input('please input a num:'))
except:
    print('not a num')

isprime(num)