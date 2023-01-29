import string
import random

characters = list(string.ascii_letters + string.digits + "[email protected]#$%^&*()")


def generate_random_password():
    length = 10

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))


generate_random_password()

# funkcja generujaca losowe haslo 10 znakow(cyfry, litery male duze, znaki specjalne)



import base64

wiadomosc = "kodowanie"
wiadomosc_bytes = wiadomosc.encode('ascii')
base64_bytes = base64.b64encode(wiadomosc_bytes)
base64_wiadomosc = base64_bytes.decode('ascii')

print(base64_wiadomosc)

#dekodowanie przez https://www.base64decode.org/
#Python Online Compiler https://www.programiz.com/python-programming/online-compiler/
