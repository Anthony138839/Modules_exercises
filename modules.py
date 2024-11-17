from func import *

a, b = eval(input("Enter values of a and b, separated by commas: "))
result =  add(a, b)
print(result)


'''The os module'''
import os
# Creating a directory
directory = 'Geeks for geeks'
parent_dir = "Day 5 - 8"
path = os.path.join(parent_dir, directory)
os.mkdir(path)
print(f"Directory created: {path}")


'''The sys module'''
import sys
file_name = sys.argv[0]
print(f"Welcome {sys.argv[1]}. Enjoy {sys.argv[1]} challenge!")

print(sys.path)


'''The statistics module'''
from statistics import *
ages = [31, 24, 22, 19, 20, 35]
print(mean(ages))


'''The string module'''
from string import *
# To print out all ascii characters(letters only)
print(ascii_letters)
# To print out all digits
print(digits)
# To print out all punctuations
print(punctuation)



'''The random function'''
from random import *
# To generate a random number from 0 to 6
x = random() * 6
print(x)


'''Exercise 1: Write a function which generates a six-digit/character random_user_id'''
from random import *
from string import *

def random_user_id():
    for i in range(n):
        element = random.choice(char)
        user_id_list.append(element)
    return ''.join(user_id_list)
    
    
user_id_list = []
n = eval(input("Enter number of characters: "))
letters = string.ascii_letters
num = string.digits
characters = letters, num
char = ''.join(characters)

print(random_user_id())




'''Exercise 2: Modify the previous task. Declare a function named "user_id_gen_by_user". It doesn't take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second is the number of IDs which are supposed to be generated.'''

'''Method 1'''

import random, string

def user_id_gen_by_user():
    no_random_char = []
    random_word_count = 0
    while random_word_count < id_no:
        count = 0
        char_list = []
        while count < n:
            char_result = random.choice(char_str) 
            count += 1
            char_list.append(char_result)
            random_char = "".join(char_list)
        
        random_word_count += 1
        no_random_char.append(random_char)
    return no_random_char
  
n = eval(input("Enter number of characters: "))
id_no = eval(input("Enter number of IDs to be generated: "))
letters = string.ascii_letters
numbers = string.digits
char = letters, numbers
if isinstance(char, tuple):
    char_str = "".join(char)
print(user_id_gen_by_user())


'''Method 2: Using more than one function'''

import random, string

def generate_random_char(char_str):
    count = 0 
    char_list = []
    
    while count < n:
        char = random.choice(char_str)
        count += 1
        char_list.append(char)
    return "".join(char_list)
 
n = eval(input("Enter number of characters: "))
letters = string.ascii_letters
numbers = string.digits
characters = letters, numbers
if  isinstance(characters, tuple):
    char_str = "".join(characters)

def user_id_gen_by_user():
    random_count = 0
    random_char = []
    
    while random_count < id_no:
        string_char = generate_random_char(char_str)
        random_char.append(string_char)
        random_count += 1
    return random_char
        
id_no = eval(input("Enter number of random IDs: "))
print(user_id_gen_by_user())


""" Method 3 """

import random, string

def user_id_gen_by_user():
    num_random_user_id = []
    user_id_count = 0
    while user_id_count < num_id:
        result = random_user_id()
        user_id_count += 1
        num_random_user_id.append(result)  
    result = ", ".join(num_random_user_id)
    return f"IDs: {result}"

    
num_char = eval(input("Enter number of characters: "))
num_id = eval(input("Enter number of IDs to be generated: ")) 
letter = string.ascii_letters
number = string.digits
characters = letter, number
char = "".join(characters)

def random_user_id():
    user_id_list = []
    for i in range(num_char):
        user_id = random.choice(char)
        user_id_list.append(user_id)
        random_user = "".join(user_id_list)
    return random_user

print(user_id_gen_by_user())


'''Exercise 3: Write a function named "rgb_color_gen". It will generate rgb colors (3 values ranging from 0 to 255 each).'''

import random
def rgb_color_gen():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    
    color = r, g, b
    return f'rgb{color}'

print(rgb_color_gen())



'''Exercise 4: Write a function "generate_colors" which can generate any number of hexa or rgb colors.'''
""" Method 1 """

import random, string
def generate_colors(choice, n):
    if choice == "hexa":
        hexa_n = eval(input("Enter number of hexa characters: "))
        hexa_list = []
        hexa_count = 0
        while hexa_count < n:
            count = 0
            char_list = []
            while count < hexa_n:
                char = random.choice(string_char)
                count += 1
                char_list.append(char)
                hexa_color = "".join(char_list)
            # return f"#{hexa_color}"
            hexa_count += 1
            hexa_list.append(hexa_color)
        return hexa_list

    elif choice == "rgb":
        rgb_list = []
        rgb_count = 0
        while rgb_count < n:
            r = random.randrange(0, 255)
            g = random.randrange(0, 255)
            b = random.randrange(0, 255)

            color = f"rgb{r, g, b}"
            rgb_count += 1
            rgb_list.append(color)
        return f"rgb{rgb_list}"                 
    
choice = input("Hexa or rgb: ").lower()
n = eval(input("Enter number of hexa or rgb colors: "))
letters = string.ascii_lowercase
numbers = string.digits
characters = letters, numbers
if isinstance(characters, tuple):
    string_char = "".join(characters)
    
print(generate_colors(choice, n))


'''Method 2: The use of more than one function'''

import random, string

def rgb_colors():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return f"rgb{r, g, b}"

def hexa_colors():
    color_list = []
    for i in range(6):
        char_choice = random.choice(char)
        color_list.append(char_choice)
    color = "".join(color_list)
    return f"#{color}"
    
alpha = ["A", "B", "C", "D", "E", "F"]
letter = "".join(alpha)
digit = string.digits
character = letter, digit
char = "".join(character)

def generate_colors(choice, num):
    if choice == "hexa":
        hexa_count = 0
        hexa = hexa_colors()
        while hexa_count < num:
            hexa = hexa_colors()
            hexa_count += 1
            hexa_color_list.append(hexa)
        return hexa_color_list
    elif choice == "rgb": 
        for j in range(num):
            rgb = rgb_colors()
            rgb_color_list.append(rgb)
        rgb_result = ", ".join(rgb_color_list)
        return f"[{rgb_result}]"
    else:
        return None

 
hexa_color_list = [] 
rgb_color_list = []     
choice = input("Hexa or rgb colors: ")
num = eval(input("Enter number of hexa or rgb colors: "))
print(generate_colors(choice, num))


'''Exercise 5: Call your function "shuffle_list", it takes a list as a parameter and it returns a shuffled list'''

import random
def shuffle_list():
    shuffled_lst = random.shuffle(lst)
    return f"Shuffled list: {lst}"
    
    
lst = ["apple", "ball", "cat", "dog", "egg"]
print(shuffle_list())


'''Exercise 6: Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.'''

import random
def random_numbers():
    num_list = []
    count = 0
    for i in range(n):
        num = random.randrange(0, 9)
        count += 1
        # if i.count(num) == 1:
        num_list.append(num)
    # return num_list
    for j in num_list:
        if num_list.count(j) > 1:
            target_index = num_list.index(j)
            num_list[target_index] += 1 
    return num_list
      
    
n = eval(input("Enter number of random numbers: "))
print(random_numbers())