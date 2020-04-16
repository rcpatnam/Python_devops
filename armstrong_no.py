lower = 10
upper = 11

for num in range(lower, upper + 1):

    order = len(str(num))

    summ = 0

    temp = num
    print(f"num: {num}")
    print(f"sum: {summ}")
    print(f"order=len(num): {order}")
    print(f"temp=num: {temp}\n")

    while temp > 0:
        digit = temp % 10
        print(temp, end=':temp  ')
        print(digit, end=':digit(temp%10)  ')

        summ = summ + digit ** order
        print(summ, end=':summ(summ+digit^order)   ')

        temp = temp // 10
        print(temp, end=':temp(temp//10)   ')

        print('\n')

    if num == summ:
        print()  # print(num)