import os

def mkdir_password():
    '''Create a password file if it doesn't exist'''
    
    try :
        # Create the password.txt file if it doesn't exist
        os.makedirs("password", exist_ok=True)

    except :
        print("Error creating password file")


def touch_password_file():
    '''Create a password file if it doesn't exist'''
    
    try:
        # Create the password.txt file if it doesn't exist
        os.chdir("password")
        ls = os.listdir()
        if ("password.txt" not in ls) :
            with open("password.txt", "w", encoding="utf-8") as file:
                file.write("")
            return True
        else:
            print("Password file already exists.")
            return None
    except :
        print("Error creating password file")
        return None





def password_save(password):
    '''Save the password to the file'''
    
    try:
        # Change to the password directory and save the password
        if os.path.getsize("password/password.txt") == 0:
            with open("password.txt", "w", encoding="utf-8") as file:
                file.write(password)
        else:
            print("Password file is not empty.")
    except :
        print("Error saving password to file")



def chaek_password(password):
    '''Check if the password file exists and is not empty'''
    
    try:
        os.chdir("password")
        if os.path.exists("password.txt") and os.path.getsize("password.txt") > 0:
            f = open("password.txt", "r")
            if f.read().strip() == password:
                print("Password is correct.")
                return True
            
        else:
            print("Password file does not exist or is empty.")
            return None
    except :
        print("Error checking password file")
        return None

