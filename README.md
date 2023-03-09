
![Continuous Integration on Git Push](https://github.com/Schots/password_security/actions/workflows/main.yml/badge.svg)

![](https://img.shields.io/github/license/schots/password_security)

[![image](https://user-images.githubusercontent.com/8209798/112394472-86123a00-8cdb-11eb-9cf5-6e539255b3f5.png)](https://haveibeenpwned.com/)

# Password Security Checker

This project allows you to verify the security of your passwords.
It is done via this [API](https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange), which allows
the use of the first 5 characters of the password hash. 

Summarizing, the password never leaves the local machine. 

## Command Line Interface 

### Installation

To start using the application,please install it by using the command below.

``` make install ```

### Usage

``` python3 password_security.py 'my_password' ```

### Usage Streamlit

```streamlit run verificador_de_senhas.py ```
