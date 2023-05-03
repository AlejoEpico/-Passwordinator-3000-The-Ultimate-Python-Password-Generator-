import string 
import random

characters = list(string.ascii_letters + string.digits + '!@#%^&*()1234567890')

def generate_password():
    the_password_length = int(input("How long do you want the password? "))

    random.shuffle(characters)

    password = []

    for x in range(the_password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input('Generate a random password? (YES/NO): ').lower()
if option == "yes":
    generate_password()
elif option == 'no':
    print('Programm ended')
else:
    print('Invalid input, enter YES or NO')
    quit()
