customer = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
phone = input("Phone number:")
for num in phone:
    output += customer.get(num , " !") + " "
print(output)

