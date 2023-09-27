"""Author: Rawan Khaled  https://github.com/RawanKhaled20/Codsoft-Python.git"""

import random
import string
import time
def generate_password(length):
    # The passowrd is a mix of uppper and lower case letters, digits from 0-9 and punctuation symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def convenience_measure():
    delay = 0.5
    time.sleep(delay)
    print("Is it of the required complexity")
    time.sleep(delay)
    print("1.yes")
    print("2.No")
    time.sleep(delay)
    x = int(input("please choose 1 or 2: "))
    if x!=1 and x!=2:
        print("Invalid, Try again")
        time.sleep(delay)
        x = int(input("please choose 1 or 2: "))
    return x

def main():
    global length
    delay = 0.5
    print("Password Generator")
    print("------------------")

    #Inputing a positive number of password length
    try:
        length = int(input("Enter desired password length: "))
        while True:
            if length <= 0:
                print("Invalid password length. Please enter a positive number.")
                length = int(input("Enter desired password length: "))
            elif length > 15:
                print("Too long, the maximum length is 15 ")
                length = int(input("Enter desired password length: "))
            else:
                break

        password = generate_password(length)
        print(f"Generated Password: {password}")

        #Check if this is the complexity required
        x=convenience_measure()
        while x==2:
            time.sleep(delay)
            print("sorry for the inconvenience, will generate another one for you ")
            password = generate_password(length)
            time.sleep(delay)
            print(f"Generated Password: {password}")
            x=convenience_measure()
        print("Thanks for using the password generator app")

    #Error solving In case of entering a character instead of a number
    except ValueError:
        print("Invalid input. Please enter a valid number (No letters or symbols).")


if __name__ == "__main__":
    main()
