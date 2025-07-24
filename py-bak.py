import os
import inputs
import password



def __main__():
    '''Main Function to Execute the Script'''

    if ls := os.listdir():
        if "password" not in ls or "back_grund" not in ls :
            inputs.welcom()
            password.mkdir_password()
            password.touch_password_file()
            pas = inputs.inputs()
            password.password_save(pas)


if __name__ == "__main__" :

    __main__()

else :
    print("no")