

"""
#Task 1
def grams_to_ounces(grams):
    return grams * 28.3495231
grams=float(input("Enter the gram: "))
ounces=grams_to_ounces(grams)
print(ounces) 


#Task 2
def fahrenheit_to_centigrade(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

fahrenheit=float(input("Enter the temparature: "))
celcius=fahrenheit_to_centigrade(fahrenheit)
print(f"Temperature in Celcius is {celcius:.2f}")



#Task 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None, None

numheads=45
numlegs=116

chickens, rabbits=solve(numheads, numlegs)
print(f"Chickens -> {chickens} and rabbits -> {rabbits}")




#Task 4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

n=list(map(int, input("List of numbers: ").split()))
prime_numbers=filter_prime(n)
print(prime_numbers)




#Task 5
from itertools import permutations

def print_permutations():
    word=input("Enter word: ")
    perms = permutations(word)
    for perm in perms:
        print("".join(perm))

print_permutations()


#Task 6
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

sentence=str(input())
reversed_sentence=reverse_sentence(sentence)
print(reversed_sentence)

"""
#Task 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums = list(map(int, input("Enter numbers: ").split()))
print(has_33(nums))






#Task 8
def spy_game(nums):
    code = [0, 0, 7]
    code_index = 0
    for num in nums:
        if num == code[code_index]:
            code_index += 1
        if code_index == len(code):
            return True
    return False

numbers = list(map(int, input("Enter numbers: ").split()))
print(spy_game(numbers))





#Task 9
import math
def sphere_volume(radius):
    from math import pi
    return (4 / 3) * pi * radius**3

sphere_radius = float(input())
print(f"{sphere_volume(sphere_radius):.2f}")





#Task 10
def unique_list(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique
elements = list(map(int, input("Enter: ").split()))
print(unique_list(elements))



#Task 11
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

s = input("Enter: ")
if is_palindrome(s):
    print("Palindrome")
else:
    print("Not a Palindrome!")


#Task 12
def histogram(lst):
    for num in lst:
        print('*' * num)
numbers = list(map(int, input("Enter: ").split()))
histogram(numbers)


#Task 13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
guess_the_number()

#Task 14   
"""
if __name__ == "__main__":
    print(grams_to_ounces(100))  # Example usage
    print(fahrenheit_to_centigrade(98.6))
    print(solve(35, 94))
    print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print_permutations("abc")
    print(reverse_sentence("We are ready"))
    print(has_33([1, 3, 3]))
    print(spy_game([1, 2, 4, 0, 0, 7, 5]))
    print(sphere_volume(3))
    print(unique_list([1, 2, 2, 3, 4, 4, 5]))
    print(is_palindrome("madam"))
    histogram([4, 9, 7])

"""
    #Try to use this comments
    # Uncomment to play the game
    # guess_the_number()