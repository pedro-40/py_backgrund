from colorama import Fore




def welcom () :
    '''Welcome Message and Directory Check'''

    print(Fore.CYAN+"welcome to the Py-Bak script!"+Fore.RESET, end="\n")


def password_input() :
    '''Password Access Confirmation'''
    pas = input("Enter your password: ").strip()
    return pas

def img_input() :

    try :
        img_name = input(Fore.CYAN+"Enter the name of the desired photo  "+Fore.RESET).strip()

        if img_name.endswith(".jpg") or img_name.endswith(".png"):
            return img_name
        else:
            print(Fore.RED+"Please enter a valid image file name (with .jpg or .png extension)."+Fore.RESET)
            return None
    except :
        print(Fore.RED+"Error reading image name."+Fore.RESET)
        return None
    
    