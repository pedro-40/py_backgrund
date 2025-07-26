import hashlib
from colorama import Fore

def password_hashing(password: str ) -> str:
    """
    Hash a password using SHA-256 and return the hexadecimal digest.
    
    :param password: The password to hash.
    :return: The hexadecimal digest of the hashed password.
    """
    try :
        pas = password.encode() 
        pas_hash = hashlib.sha256(pas)
        print(Fore.GREEN + "Password hashed successfully" + Fore.RESET)
        
        return pas_hash.hexdigest()

    except :
        print(Fore.RED+ "Error in hashing the password"+Fore.RESET)
        return None
