import sys
import hashlib
import requests
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

################ Program Parameters ##############################################

API_URL = "https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange"

###################################################################################

################### Rich Terminal Settings #######################################

custom_theme = Theme(
    {
        "bad password": "red",
        "good password": "green",
    }
)

console = Console(theme=custom_theme)

table = Table()
table.add_column("Password")
table.add_column("# of Leaks")
table.add_column("Diagnostic")


#####################################################################################


def request_api_response(hashed_password):
    password_hash_url = "https://api.pwnedpasswords.com/range/" + hashed_password
    api_response = requests.get(password_hash_url)
    if api_response.status_code != 200:
        raise RuntimeError(f"Please, check the password format in {API_URL}")
    else:
        return api_response


def get_pwnd_count(api_hashes_response, password_hash):
    hash_split = (hashes.split(":") for hashes in api_hashes_response.text.splitlines())
    for h, count in hash_split:
        if h == password_hash:
            return int(count)
    return 0


def password_checker(password):
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    password_begin, password_end = hashed_password[:5], hashed_password[5:]
    response = request_api_response(password_begin)
    return get_pwnd_count(response, password_end)


def main(passwords_to_check):
    for password in passwords_to_check:
        number_leaks = password_checker(password)
        if number_leaks:
            table.add_row(password, str(number_leaks), "Insecure", style="bad password")
        else:
            table.add_row(password, str(number_leaks), "Secure", style="good password")

    console.print(table)


if __name__ == "__main__":
    main(sys.argv[1:])
