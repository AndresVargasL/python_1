from email import charset
import random

def generar_password():
    mayus = ['A', 'B', 'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
    minus = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    numb = ['0','1','2','3','4','5','6','7','8','9']
    simb = ['!','#','$','%','&','/','(',')','¡','¿','?']

    charcter = mayus + minus + numb + simb

    password = []

    for i in range(20):
        char_random = random.choice(charcter)
        password.append(char_random)

    password = "".join(password)
    return password

def run():
    password = generar_password()
    print('Your new password is: ' + password)


if __name__ == '__main__':
    run()