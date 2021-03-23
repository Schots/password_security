import sys
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

def get_pwnd_count(api_hashes_response,password_hash):
    hash_split = (hashes.split(":") for hashes in api_hashes_response.text.splitlines())
    for h,count in hash_split:
        if h == password_hash:
            return int(count)
    return 0

def password_checker(password):
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    password_begin,password_end = hashed_password[:5],hashed_password[5:]
    response = request_api_response(password_begin)
    return get_pwnd_count(response,password_end)

def main():
    number_leaks = password_checker(sys.argv[1])
    if number_leaks > 0:
        print(f"Wow! This password has been leaked {number_leaks} times. Try to change it now.")
    else:
        print("This password is safe for now. Zero leaks found.")

main()
