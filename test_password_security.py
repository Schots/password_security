import hashlib
from password_security import password_checker,get_pwnd_count

def test_password_checker():
    assert password_checker("123") == 1078184



