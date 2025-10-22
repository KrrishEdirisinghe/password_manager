import json
import time
def delay(message):
    print(message)
    time.sleep(1)


def add_credentials(site , username , password):
    with open('passwords.json' , 'r') as f:
        data = json.load(f)

    data[site] = {'username' : username , 'password' : password}

    with open('passwords.json' , 'w') as f:
        json.dump(data , f , indent = 4)
def view_passwords():
    with open('passwords.json' , 'r') as f:
        data = json.load(f)
        user = input('would you like to see your passwords?(y or n) ').lower()
        if user == 'y':
            print('//saved credentials//')
            for site , values in data.items():
                print(f'site : {site}')
                print(f'username : {values['username']}')
                print(f'password : {values['password']}')
    

def user_input():
    
    while True:
        ask_user = input('would you like to add a new password?(y or n) ').lower()
        if ask_user == 'y':
            website = input('website: ')
            username = input('username: ')
            password = input('password: ')
            add_credentials(website , username , password)
            continue
        elif ask_user == 'n':
            break
        else:
            print('please enter a valid input')
            continue
    


def main():
        delay('welcome to password manager')
        user_input()
        view_passwords()

main()

