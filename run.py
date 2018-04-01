#!/usr/bin/env python3.6
import random
from user import User
from credentials import Credentials

def create_users(name,password):
    '''
    creates login for username
    '''
    new_run_user= User(name,password)
    return new_run_user

def save_new_user(user):
    '''
    Functions that appends a user to the list
    '''
    user.save_user()

def user_exist(name):
    '''
    Function that returns a boolean value based on whether the exists
    '''
    return User.user_exists(name)

def create_credentials(account_name, account, user_name, password):
    '''
    Function to create new credentials
    '''
    new_credentials = Credentials(account_name, account, user_name, password)
    return new_credentials

def save_user_credential(credentials):
    '''
    Function to save credentials
    '''
    Credentials.save_credentials()

def delete_credential(credentials):
    '''
    Function to delete credentials from list
    '''
    Credentials.delete_credentials()

def find_credentials(name):
    '''
    Function that finds a credentials by account
    '''
    return Credentials.find_by_name(name)

def credentials_exists(name):
    '''
    Function that returns a boolean value based on whether the user 
    being sough exists
    '''
    return Credentials.credential_exists(name)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Welcome to password locker")
    while True:
        print("  ___________________")
        print(" |    su - sign up   | \n |    lg - login     | \n |    ex - exit      |")
        print(" |___________________|")
        short_code = input().lower()
        if short_code == "su":
            print("Input Username: ")
            su_username = input()
            print("Input Password: ")
            su_password = input()
            print('  ----------------------')

            save_new_user(create_users(su_username, su_password))
            print("\n | User Has Been Created | \n")
            print('  ---------------------')
            print("USER             PASSWORD")
            print(f"{su_username}             {su_password} ")
        elif short_code == "lg":
            print("Input User Name:")
            lg_username = input()
            print("Input Password: ")
            lg_password = input()

            if user_exist(lg_username):
                print(f"Welcome {lg_username}")
                while True:
                    print ('-'*10)
                    print("cc :to add a credential")
                    print("dc :to display a credential") 
                    print("dl :to delete a credential")
                    print("ex :to exit")
                    short_code = input() 

                    if short_code == 'cc':
                        while True:
                            print("1 : to insert password")
                            print("2 : generate password")
                            print("3 : back to main menu")
                            short_code1 = input()

                            if short_code1 == '1':
                                print(f"WELCOME {credential_user_name}, ADD A CREDENTIAL") 
                                print ('-'*10)
                                print("ENTER CREDENTIAL NAME")
                                name_of_credential =input()
                                print("ENTER CREDENTIAL'S PASSWORD")
                                password_of_credential = input()

                                save_credential_run(create_credential(credential_user_name,name_of_credential,password_of_credential))
                                
                                print("YOUR CREDENTIALS")
                                print ('-'*10)
                                for credential in Credentials.display_all_credentials():
                                    if credential_user_name == credential.user_name:
                                        print(f"CREDENTIAL:{credential.credential_name}......PASSWORD:{credential.credential_password}")
                                        print ("\n")
                            

                            elif short_code1 == '2':
                                print ('-'*10)
                                print(f"WELCOME {credential_user_name}, ADD A CREDENTIAL")
                                print ('-'*10) 
                                print("ENTER CREDENTIAL NAME")
                                name_of_credential =input()
                                print("YOUR PASSWORD HAS BEEN GENERATED")
                                password_of_credential = random.randint(10000,99000)

                                save_credential_run(create_credential(credential_user_name,name_of_credential,password_of_credential))
                                
                                print("YOUR CREDENTIALS")
                                print ('-'*10)
                                for credential in Credentials.display_all_credentials():
                                    if credential_user_name == credential.user_name:
                                        print(f"CREDENTIAL:{credential.credential_name}......PASSWORD:{credential.credential_password}")
                                        print ("\n")

                            elif short_code1 == 'ok':
                                break

                            elif short_code1 == 'ex':
                                break
                            else:
                                    print("INVALID INPUT PLEASE USE THE PROVIDED SHORTCODES")
                                    print ("\n")                                   
            
        


if __name__ == '__main__':
    main()
