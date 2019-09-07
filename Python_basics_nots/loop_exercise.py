# Write your function here
def add_greetings(names):
    greeting_list = []
    for name in names:
        mid = "Hello, " + name
        greeting_list.append(mid)
    return greeting_list


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))


#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))