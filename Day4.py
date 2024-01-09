#!/bin/bash
"""
Love calculator

Author: Harsh Jain (github.com/jsjsdgfhjsdghjgsdf/)
"""

def main():
    print("The Love Calculator is calculating your score...")
    name1 = input("Enter the first person name: ") # What is your name?
    name2 = input("Enter the second person name: ") # What is their name?

    characters = ['T', 'R', 'U', 'E', 'L', 'O', 'V', 'E',]
    count, countn = 0, 0

    for i in name1.upper():
        if i in characters:
            count += 1
    for i in name2.upper():
        if i in characters:
            countn += 1
    count = int(str(count) + str(countn))
    del countn, characters, name1, name2

    if count <= 10 or count >= 90:
        print(f"Your score is {count}, you go together like coke and mentos.")
    elif count >= 40 and count <= 50:
        print(f"Your score is {count}, you are alright together.")
    else:
        print(f"Your score is {count}.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(1)
    except Exception as error:
        raise error
        print(f"[ Error: {error} ]")