try:
    age = int(input("Age: "))
    print(age)
    income = 1000
    risk = income / age
except ZeroDivisionError:
    print("Age cnnot be 0.")
except ValueError:
    print("Invlid value.")