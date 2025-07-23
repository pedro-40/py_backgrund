import os
from colorama import Fore, Style
import password

def welcom () :
    '''Welcome Message and Directory Check'''

    print(Fore.CYAN+"welcome to the Py-Bak script!"+Fore.RESET)


def inputs() :
    '''Password and Settings Access Confirmation'''

    global password
    password = input("Enter your password: ").strip()


def __main__():
    '''Main Function to Execute the Script'''

    if ls := os.listdir():
        if "password" and "back_grund" not in ls :
            welcom()
            password.mkdir_password()
            password.touch_password_file()
            password.
