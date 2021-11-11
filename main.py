#!/usr/bin/python3
# Program to allow a user to easily memorize passwords by breaking up the password in small segments
from authorlib import AuthorLib
from generator import generate
from split import split_password
import os
from colorama import Fore

AuthorLib(
    "ProtonDev", "Password Memorizer", "CYAN"
).output()  # Use local author lib module from directory, use it to display figlet text


def clear():
    os.system("clear")


def memorizePassword(password: str):
    full_pass = ""
    password = split_password(password)
    for i in range(0, len(password)):
        full_pass += password[i]
        current_string = password[i]
        counter = 0
        print(
            f"Helping Memorize: Section {i + 1} Of Password, will move to next section after 5 correct tries"
        )
        while counter < 5:
            memorize = input(f"Please Type: {current_string}\n> ")
            if counter == 5:
                print(f"Passed Section {i + 1} of password")
                break
                counter = 0
            elif memorize == current_string:
                print(Fore.GREEN + "Correct, Good Job!" + Fore.RESET)
                counter += 1
            else:
                counter = 0
                print(
                    Fore.RED
                    + "Incorrect, Better Luck Next Time! Reset Counter!"
                    + Fore.RESET
                )
    counter = 0
    while counter < 5:
        memorize = input(f"Please Type: {full_pass}\n> ")
        if counter == 5:
            print(f"Finished Memorizing Password {i + 1} of password")
            break
            counter = 0
        elif memorize == full_pass:
            print(Fore.GREEN + "Correct, Good Job!" + Fore.RESET)
            counter += 1
        else:
            counter = 0
            print(
                Fore.RED
                + "Incorrect, Better Luck Next Time! Reset Counter!"
                + Fore.RESET
            )


has_password = int(
    input(
        "Do You Know The Password You Want To Memorize?\n1. Yes\n2. No Please Help Me Generate One\n> "
    )
)

if (
    has_password == 1
):  # If the user already knows what the password they want to memorize is
    password_input = input("What Is The Password You Are Trying To Memorize?\n> ")
    memorizePassword(password=password_input)
elif has_password == 2:  # If the user needs a password generated
    password_input = (
        input("Amount Of Passwords To Generate? (Leave blank for 1)\n> ") or 1
    )
    generated = generate(amount=int(password_input))
    memorizePassword(generated)
