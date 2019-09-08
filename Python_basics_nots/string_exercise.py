def username_generator(first_name, last_name):
    username = ""
    if len(first_name) > 3 and len(last_name) > 4:
        username = first_name[:3] + last_name[:4]
    elif len(first_name) <= 3 and len(last_name) > 4:
        username = first_name + last_name[:4]
    elif len(first_name) > 3 and len(last_name) <= 4:
        username = first_name[:3] + last_name
    else:
        username = first_name + last_name
    return username


test = username_generator("Zoe", "Lee")
print(test)


def password_generator(username):
    password = ""
    for w in range(0, len(username)):
        password += username[w - 1]
    return password


test2 = password_generator("UsErNamE")
print(test2)


def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
    return poem_desc


author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)
print(my_beard_description)


