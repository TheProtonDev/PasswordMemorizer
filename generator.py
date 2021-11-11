import requests


def requestPasswords(amount: int):
    global retrieved_password
    if amount == 1:
        retrieved_password = requests.get(
            "https://www.passwordrandom.com/query?command=password&scheme=CvvCVCvVNNN"
        ).text
        print(f"#{1} | {retrieved_password}")
        return retrieved_password
    elif amount != 1:
        retrieved_passwords = requests.get(
            f"https://www.passwordrandom.com/query?command=password&count={amount}&scheme=CvvCVCvVNNN"
        )
        print("Generated Passwords:")
        retrieved_passwords = (
            retrieved_passwords.text.splitlines()
        )  # Make a list from the passwords
        counter = 0  # Create a counter to keep track of each password printed to the terminal in the for loop
        for password in retrieved_passwords:
            counter = counter + 1
            print(f"#{counter} | {password}")
        return retrieved_passwords


def generate(amount: int):
    while True:
        generated_passwords = requestPasswords(amount=amount)
        select_generated_password = input(
            "Generated Password To Select? (Leave blank for regeneration of passwords)\n> "
        )
        if select_generated_password == "":
            continue  # go back to the beginning of the method if user wants to regenerate password(s)
        else:
            if type(generated_passwords) == list:
                select_pass = generated_passwords[int(select_generated_password) - 1]
                return select_pass
                break
            else:
                return generated_passwords
                break

    else:
        select_pass = generated_passwords[int(select_generated_password)]
