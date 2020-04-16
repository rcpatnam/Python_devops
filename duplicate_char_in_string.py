# Using count
string = 'HelloThereYouEdward'
x = 'e'
countstring = string
counter = countstring.count(x)

print(f'{x} occurs {counter} times in {string}')

print("\n******************************\n")

# Iterative method
test_string = 'HelloThereEdward'
test_char = 'e'

count = 0

for i in test_string:
    if i == test_char:
        count += 1

print(f'Count of {test_char} in {test_string}: {str(count)}')

# List method

myString = 'Hello Hello there'
newString = []

for i in list(myString):
    if i not in newString:
        newString.append(i)

print(newString)