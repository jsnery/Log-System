from toolsLog import *

clear()

user = input('Username: ')
while True:
    if user.isspace() or user == "":
        clear()
        logAppend('Empty username error')
        print('Empty username error! Try Again\n')
        user = input('Username: ')
        continue
    break

password = input('Password: ')
while True:
    if password.isspace() or password == "":
        clear()
        logAppend('Empty password error')
        print('Empty password error! Try Again\n')
        password = input('Password: ')
        continue
    break

...

