import os
import inputs
import password



def __main__():
    '''Main Function to Execute the Script'''

    if ls := os.listdir():
        if "password" not in ls or "back_ground" not in ls :
            inputs.welcom()
            password.mkdir_password()
            password.touch_password_file()
            pas = inputs.password_input()
            password.password_save(pas)


if __name__ == "__main__" :

    __main__()

else :
    print("no")