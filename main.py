# Binary to Decimal Conversion Using Doubling Method

# Enter the binary value for string
print('Enter binary string: ', end='')
st = input()

# Create original total
total = int(st[0])

# Using loop to calculate the final total number which is decimal number
for i in range(int(len(st) - 1)):
    next_number = int(st[i + 1])
    total = total * 2 + next_number

# Export the value
print('Decimal number: ', total)
