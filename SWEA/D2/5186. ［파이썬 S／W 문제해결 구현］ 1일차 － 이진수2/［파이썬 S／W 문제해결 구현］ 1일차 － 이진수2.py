t = int(input())

for i in range(t):
    n = float(input())
    times = 1
    answer = ''

    while n!= 0 and  times <= 13:
        if n >= (1 / 2) ** times:
            n -= (1 / 2) ** times
            answer += '1'
        else:
            answer += '0'

        times += 1

    if n > 0:
        answer = 'overflow'

    print('#' + str(i + 1) + ' ' + answer)