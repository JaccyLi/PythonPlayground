# ##### lesson one

# Write your sum_values function here:


def sum_values(my_dictionary):
    sum = 0
    for i in my_dictionary.values():
        sum += i
    return sum
# Uncomment these function calls to test your sum_values function:
# print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
# print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


# ##### lesson two
# Write your sum_even_keys function here:


def sum_even_keys(my_dictionary):
    sum = 0
    for key, value in my_dictionary.items():
        if key % 2 ==0:
            sum   += my_dictionary[key]
    return sum

# Uncomment these function calls to test your  function:
# print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
# print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


# ##### lesson three
# Write your add_ten function here:
def add_ten(my_dictionary):
    for k in my_dictionary.keys():
        my_dictionary[k] += 10
    return my_dictionary

# Uncomment these function calls to test your  function:
# print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
# print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}


# ##### lesson four

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
    value_keys = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            value_keys.append(value)
    return value_keys


# Uncomment these function calls to test your  function:
# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
# print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


# ##### lesson five
# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
# print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
# print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


# ##### lesson six
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  new = {
    item: len(item)
    for item
    in words
  }
  return new
# Uncomment these function calls to test your  function:
# print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
# print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}



# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    dict = {}
    for word in words:
        if word not in dict:
            dict[word] = 0
        dict[word] += 1
    return dict


# ##### lesson seven
# Uncomment these function calls to test your  function:
# print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
# print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}


# ##### lesson eight
def unique_values(my_dictionary):
    uniq =[]
    for value in my_dictionary.values():
        if value not in uniq:
            uniq.append(value)
    return len(uniq)

# Uncomment these function calls to test your  function:
# print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
# print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

