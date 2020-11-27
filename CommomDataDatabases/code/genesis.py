# ================================================================== #

from random import randint
from colorama import Fore, Back, Style
import hashlib
import colorama
import sys

# ================================================================== #
# | CONFIG

# Prompt Colors
normal_background = Fore.LIGHTGREEN_EX + Back.BLACK
yellow_dot = Fore.LIGHTYELLOW_EX + " [+] " + Fore.GREEN
error_msg = Fore.WHITE + Back.RED
success = Fore.WHITE + Back.GREEN
title = """
+---------------------------+
|.-. .-. . . .-. .-. .-. .-.|
||.. |-  |\| |-  `-.  |  `-.|
|`-' `-' ' ` `-' `-' `-' `-'|
+---------------------------+
"""

# ================================================================== #
# | INITIALIZE
colorama.init()
print(Style.NORMAL + normal_background)
print(title)
# | VARS
temp_name = ""
temp_mail = ""
temp_passwd = ""
mail_divs = ["", "-", "_", "."]
resultbase = []
counter = 0
# ================================================================== #

# Open Files:
def get_data(filename):
    try:
        with open(filename, "r") as data:
            temp = data.read().split("\n")
            data.close()
        return temp
    except Exception as error:
        print(error_msg + "{0}".format(error))
        sys.exit()

# ================================================================== #
print(yellow_dot + "First names file:")
firstnames = get_data(input(" "))
print(yellow_dot + "Surnames file:")
surnames = get_data(input(" "))
print(yellow_dot + "Passwords file:")
passwords = get_data(input(" "))
print(yellow_dot + "Password mode:")
print(Fore.YELLOW + " p" + Fore.GREEN + ": Plain Text" + " | " + Fore.YELLOW + "m" + Fore.GREEN + ": MD5")
passmode = input(" ").lower()
print(yellow_dot + "eMail Domains file:")
mails = get_data(input(" "))
print(yellow_dot + "Number of registers:")
number_of_data = int(input(" "))
print(yellow_dot + "Verbose?:")
print(Fore.YELLOW + " y" + Fore.GREEN + ": Yes" + " | " + Fore.YELLOW + "n" + Fore.GREEN + ": No")
option = input(" ").lower()
if option == "y":
    verbose = True
else:
    verbose = False
# ================================================================== #
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
    #print(temp_name)

    # Password
    temp_passwd = passwords[randint(1, len(passwords) - 1)]
    if passmode == "h":
        temp_passwd = hashlib.md5(temp_passwd.encode("utf-8")).hexdigest()
    #print(temp_passwd)

    # Email
    temp_mail += temp_name.lower()
    while " " in temp_mail:
        temp_mail = temp_mail.replace(" ", mail_divs[randint(1, len(mail_divs) - 1)], 1)
    temp_mail += "@" + mails[randint(1, len(mails) - 1)]
    #print(temp_mail)

    # Save result:
    if verbose:
        print("{0}:{1}:{2}".format(temp_name, temp_mail, temp_passwd))
    resultbase.append((temp_name, temp_mail, temp_passwd))

    # Continue
    counter += 1
# ================================================================== #
resultname = "db" #input("\nSave result as: ")
with open(resultname, "w") as new_data:
    for i in resultbase:
        item = str(i)
        while "(" in item:
            item = item.replace("(", "")
        while ")" in item:
            item = item.replace(")", "")
        new_data.write(item + "\n")
        # print("*", end="")
    new_data.close()
# ================================================================== #
print(success + "Done. " + normal_background + "Press 'Enter' to quit.")
input()
