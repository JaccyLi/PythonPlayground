# RGB --> HEX
def rgb_hex():
    invalid_msg = "Sorry, invalid values being entered."
    red = int(input("Input your red(R) value: "))
    if red < 0 or red > 255:
        print(invalid_msg, "(0-255)")
        return
    green = int(input("Input your green(G) value: "))
    if green < 0 or green > 255:
        print(invalid_msg, "(0-255)")
        return
    blue = int(input("Input your blue(B) value: "))
    if blue < 0 or blue > 255:
        print(invalid_msg, "(0-255)")
        return
    val = (red << 16) + (green << 8) + blue
    print("%s" % (hex(val)[2:]).upper())


# HEX --> RGB
def hex_rgb():
    invalid_msg = "Sorry, invalid values being entered."
    hex_val = input("Please enter the color(a hexadecimal digits value): ")
    if len(hex_val) != 6:
        print(invalid_msg, "make sure length is 6.")
        return
    else:
        hex_val = int(hex_val, 16)
    two_hex_digits = 2 ** 8
    blue = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digits
    print("Red: %s Green: %s Blue: %s" % (red, green, blue))


# call this func to run
def convert():
    while True:
        option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:")
        if option == '1':
            print("RGB to HEX ... ")
            rgb_hex()
        elif option == '2':
            print("HEX to RGB ... ")
            hex_rgb()
        elif option == 'X' or 'x':
            break
        else:
            print("Error... ")


convert()
