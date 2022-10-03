# 1- import string and random module
import string
import random

# store all characters in lists(upper\lower cases, digits, punctuations)

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# take number of characters from user
# make sure the number of characters is 6 or more

character_numbers = input("How many character of the password?: ")
while True:
    try:
        character_numbers = int(character_numbers)
        if character_numbers < 6 :
            print("you need at least 6 numbers ")
            character_numbers = input("please enter the number again: ")
        else:
            break
    except:
           print("please enter numbers only.")
           character_numbers = input("How many characters for the password?: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(character_numbers * (30 / 100))
part2 = round(character_numbers * (20 / 100))

password = []
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)
password = "".join(password[0:])

print(password)
