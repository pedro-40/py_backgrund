import subprocess
import os
from colorama import Fore

def img_mkdir() :
    ''' create a back_ground dir if it doesn't exist'''

    try :
        os.makedirs("back_grond", exist_ok=True)

    except :
        print(Fore.RED+"Error creating back_ground dir")


def find_img(img_name) :
    '''Find the image in the back_ground directory'''

    try :
        img_address = subprocess.check_output(["find", "/home", "-name", img_name], text=True).strip()
        if img_address:
            img_address = img_address.split("\n")[0]  # Get the first match
            print(Fore.GREEN+"Image found at: "+img_address+Fore.RESET)
            return img_address
        else:   
            print(Fore.RED+"Image not found."+Fore.RESET)
            return None
    except:
        print(Fore.RED+"Error finding image."+Fore.RESET)
        return None

def img_copy(img_address) :
    '''Copy the image to the back_ground directory'''

    try :
        if img_address:
            os.system(f"cp {img_address} back_grond/")
            print(Fore.GREEN+"Image copied successfully."+Fore.RESET)
            return True
        else:
            print(Fore.RED+"No image address provided."+Fore.RESET)
            return False
    except :
        print(Fore.RED+"Error copying image."+Fore.RESET) 
        return False
