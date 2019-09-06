list = [4, 4, 6, 7, 8, 9, 0, 3, 6, 7, 7, 8, 4, 2, 1]
uniq = []
for number in list:
    if number not in uniq:
         uniq.append(number)
print(uniq)