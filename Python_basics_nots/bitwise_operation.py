print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print(int("33", 8))


shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))


print(int(bin(0b1110 & 0b101), 2))


print(bin(0b1110 | 0b0101))
print(bin(0b1110 ^ 0b101))   # XOR
