from colorama import Fore




def welcom () :
    '''Welcome Message and Directory Check'''

    print(Fore.CYAN+"welcome to the Py-Bak script!"+Fore.RESET, end="\n")


def inputs() :
    '''Password Access Confirmation'''
    pas = input("Enter your password: ").strip()
    return pas