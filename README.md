
![image](https://user-images.githubusercontent.com/8209798/112394472-86123a00-8cdb-11eb-9cf5-6e539255b3f5.png)

# Password Security Checker

This project allows you to verify the security of your passwords.
It is done via this [API](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange), which allows
the use of the first 5 characters of the password hash. 

Summarizing, the password never leaves the local machine. 

## Command Line Interface 

``` python3 password_security.py "my_password" ```


