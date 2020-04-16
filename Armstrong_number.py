num = 153  # 407, 1634, 153

order = len(str(num))

summ = 0

temp = num
# sum of power of each digit
while temp > 0:
    digit = temp % 10
    summ = summ + digit ** order
    temp = temp // 10

if num == summ:
    print("Is Armstrong number.")
else:
    print("Is not Armstrong number.")

print("*-----------------------------------------------*")

lower = 1
upper = 1000

for num in range(lower, upper + 1):

    order = len(str(num))
    summ = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        summ += digit ** order
        temp //= 10

    if num == summ:
        print(num)
