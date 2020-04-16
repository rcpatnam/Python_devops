def check(string):
    p = set(string)

    s = {'0', '1'}  # set is like a list but no repeated elements, is decalred in {''} or as set()

    if s == p or p == {'0'} or p == {'1'}:
        print('Yes')
    else:
        print('No')

b = '100'
check(b)


print("\n*********************\n")

# Using iteration by checking for 0 and 1 in the number
def check2(string):
    t = '01'

    count = 0

    for char in string:
        if char not in t:
            count = 1
            break
        else:
            pass

    if count:
        print('No')
    else:
        print('Yes')

b = '11'
check2(b)
