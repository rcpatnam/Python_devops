# x >> y = x // (2 ** y)

def countBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

i = 9
print(countBits(i))

