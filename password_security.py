import hashlib
import requests

API_URL = "https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange"


def request_api_response(hashed_password):
    password_hash_url = 'https://api.pwnedpasswords.com/range/' + hashed_password
    api_response = requests.get(password_hash_url)
    if api_response.status_code != 200:
        raise RuntimeError(f"Please, check the password format in {API_URL}") 
    else:
        return api_response

def password_checker(password):
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    password_begin,password_end = hashed_password[:5],hashed_password[5:]
    response = request_api_response(password_begin)
    print(response.text)


password_checker("sandro_@12!")
