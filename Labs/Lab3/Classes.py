
#Task 1
class StringHandler:
    def __init__(self):
        self.string = ""


    def getString(self):
        self.string = input("Enter a string: ")


    def printString(self):
        print(self.string.upper())

p1=StringHandler()
p1.getString()
p1.printString()


"""
#Task 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
    
p2=Shape()
print(p2.area())
p3=Square(8)
print(p3.area())




# Task 3
class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
shape=Shape()
print(shape.area())
rectangle=Rectangle(9, 5)
print(rectangle.area())





# Task 4

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
point1=Point(3, 6)
point1.show()

point2=Point(6, 7)
print("Distance: ", point1.dist(point2))






# Task 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

# Testing Account class
acc = Account("John Doe", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(1500)




# Task 6
import math
primes = lambda x: all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)) and x > 1

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17]
prime_numbers = list(filter(primes, numbers))

print(f"Prime numbers in the list: {prime_numbers}") 

"""
