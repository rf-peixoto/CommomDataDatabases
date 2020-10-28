# Database Generator
# v0.4.0

from random import randint
import hashlib
# ---------------------------------------------------------- #
def get_data(filename):
    with open(filename, "r") as data:
        temp = data.read().split("\n")
        data.close()
        return temp
# ---------------------------------------------------------- #
firstnames = get_data(input("First name list: "))
surnames = get_data(input("Surname list: "))
passwords = get_data(input("Password list: "))
passmode = input("Password mode:\nh = MD5 hashed | p = Plain Text: ")
mails = get_data(input("Mail list: "))
number_of_data = int(input("Number of data: "))
# ---------------------------------------------------------- #
temp_name = ""
temp_mail = ""
temp_passwd = ""
mail_divs = ["", "-", "_", "."]
resultbase = []
# ---------------------------------------------------------- #
counter = 0
while counter <= number_of_data:
    #Reset Values:    
    temp_name = ""
    temp_mail = ""
    temp_passwd = ""
    surnames_number = randint(0, 2)
    surname_counter = 0

    # Name & Surname
    temp_name += firstnames[randint(1, len(firstnames) - 1)]
    while surname_counter <= surnames_number:
        temp_name += " " + surnames[randint(1, len(surnames) - 1)]
        surname_counter += 1
    print(temp_name)

    # Password
    temp_passwd = passwords[randint(1, len(passwords) - 1)]
    if passmode in "Hh":
        temp_passwd = hashlib.md5(temp_passwd.encode("utf-8")).hexdigest()
    print(temp_passwd)

    # Email
    temp_mail += temp_name.lower()
    temp_mail = temp_mail.replace(" ", mail_divs[randint(1, len(mail_divs) - 1)])
    temp_mail += "@" + mails[randint(1, len(mails) - 1)]
    print(temp_mail)

    # Save result:
    resultbase.append((temp_name, temp_mail, temp_passwd))

    # Continue
    counter += 1
# ---------------------------------------------------------- #
resultname = input("\nSave result as: ")
with open(resultname, "w") as new_data:
    for item in resultbase:
        item = str(item)
        while "(" in item:
            item = item.replace("(", "")
        while ")" in item:
            item = item.replace(")", "")
        new_data.write(item + "\n")
    new_data.close()

input("Done.")
