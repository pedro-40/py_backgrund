import subprocess



#List of supported desktop environments
gstting= [
    "GNOME",
    "KDE",
    "XFCE",
    "Cinnamon",
    "MATE",
    "LXQt",
    "Unity",
    "Pantheon",
    "Budgie"
]


def check_desktop_environment():
    '''Check the current desktop environment'''
    try:
        desktop_env = subprocess.run(["echo $XDG_CURRENT_DESKTOP"], shell=True, capture_output=True, text=True).stdout.strip()

        if desktop_env in gstting:
            return True
        else :
            return False
    except:
        print("Error checking desktop environment. Make sure you are running this script in a graphical environment.")
        return None



def feh_change_background(img_name):
    '''Change the desktop background using feh'''
    try:
        subprocess.run(["feh", "--bg-scale", img_name], check=True)
        print(f"Background changed to {img_name}")
    except :
        print("Error changing background. Make sure feh is installed and the image exists.")


def gsettings_change_background(img_name):
    '''Change the desktop background using gsettings'''
    try:
        subprocess.run(["gsettings", "set", "org.gnome.desktop.background", "picture-uri", f"file://{img_name}"], check=True)
        print(f"Background changed to {img_name}")
    except:
        print("Error changing background. Make sure gsettings is installed and the image exists.")




def __main__():
    img_name = subprocess.run(["ls", "back_grond"], capture_output=True, text=True).stdout.strip().split("\n")[0] # Get the first image in back_grond

    result = check_desktop_environment()

    if result is True :
        gsettings_change_background(img_name)
    elif result is False:
        feh_change_background(img_name)

if __name__ == "__main__":
    __main__()