# 111111
class Animal(object):
    """Makes cute animals."""
    is_alive = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Add your method here!
    def description(self):
        print(f"My name is {self.name}.")
        print(f"I'm {self.age} years old.")
        return


hippo = Animal("jack", 5)
hippo.description()




# 22222222
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Add your method here!
    def description(self):
        print(self.name)
        print(self.age)


hippo = Animal("Anderson", 36)
hippo.description()
print(hippo.health)
sloth = Animal("ladyslo", 12)
print(sloth.health)
sloth.health = "bad"
print(sloth.health)
ocelot = Animal("manner", 16)
print(ocelot.health)


# 3333333333333333
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")


my_cart = ShoppingCart("me")
my_cart.add_item("NoteBook", 4000)
print(my_cart.items_in_cart)


# 4 Inheritance
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print("I'm a string that stands in for the contents of your shopping cart!")


class ReturningCustomer(Customer):
    def display_order_history(self):
        print("I'm a string that stands in for your order history!")


monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()


# 5 Inheritance and overrite it

class Employee(object):
    def __init__(self, name):
        self.name = name

    def greet(self, other):
        print("Hello, %s" % other.name)


class CEO(Employee):
    def greet(self, other):
        print("Get back to work, %s!" % other.name)


ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!


# 666666666666  super超类方法调用

class Employee(object):
    """Models real-life employees!"""

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


# Add your code below!
class PartTimeEmployee(Employee):
    def __init__(self, name):
        self.name = name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)


normal = Employee("steve")
part = PartTimeEmployee("jaccy")
milton = PartTimeEmployee("mil")

print(normal.calculate_wage(5))
print(part.calculate_wage(5))
print(milton.full_time_wage(5))


# 777777777777777