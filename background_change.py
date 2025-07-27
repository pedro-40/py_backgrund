import subprocess
import os

def supported_desktop_environments():
    '''List of supported desktop environments'''
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
    return gstting


def check_desktop_environment():
    '''Check the current desktop environment'''
    try:
        desktop_env = subprocess.run(["echo $XDG_CURRENT_DESKTOP"], shell=True, capture_output=True, text=True).stdout.strip()
        print(f"Current desktop environment: {desktop_env}")

        if desktop_env in supported_desktop_environments():
            return True
        else :
            return False
    except:
        print("Error checking desktop environment. Make sure you are running this script in a graphical environment.")
        return None



















check_desktop_environment()
