# 1
def check_bit4(integer):
    verify = 0b1000
    switch = integer & verify
    if switch > 0:
        return "on"
    else:
        return "off"

# 2
a = 0b10111011
mask = 0b100
desired = a | mask
print(bin(desired))
check_bit4(5)

# 3
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print(bin(desired))

# 4


def flip_bit(number, n):
    bit_to_flip = 0b1 << (n -1)
    result = number ^ bit_to_flip
    return bin(result)


flip_bit(32, 6)

