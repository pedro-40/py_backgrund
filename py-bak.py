import os
from colorama import Fore
import password

def welcom () :
    '''Welcome Message and Directory Check'''

    print(Fore.CYAN+"welcome to the Py-Bak script!"+Fore.RESET)


def inputs() :
    '''Password Access Confirmation'''

    global pas
    pas = input("Enter your password: ").strip()


def __main__():
    '''Main Function to Execute the Script'''

    if ls := os.listdir():
        if "password" and "back_grund" not in ls :
            welcom()
            password.mkdir_password()
            password.touch_password_file()
            inputs()
            password.password_save(pas)


if __name__ == "__main__" :

    __main__()

else :
    print("no")