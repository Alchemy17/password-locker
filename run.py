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
    credentials.save_credentials()

def delete_credential(credentials):
    '''
    Function to delete credentials from list
    '''
    credentials.delete_credentials()

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
                    print("fc :to find a credential")
                    print("dl :to delete a credential")
                    print("ex :to exit")
                    print("\nInput here:") 
                    short_code = input()
                    print("\n") 

                    if short_code == 'cc':
                        while True:
                            print("1 : to insert a new credential")
                            print("2 : generate password")
                            print("3 : back to main menu")
                            short_code1 = input()

                            if short_code1 == '1':
                                print(f"New Credential") 
                                print ('-'*10)
                                print("Insert the account name: ")
                                acct_name = input()
                                print("Account for: ")
                                acct = input()
                                print("User Name: ")
                                u_name = input()
                                print("Password: ")
                                p_word = input()
                                save_user_credential(create_credentials(acct_name,acct,u_name, p_word))
                                
                                print("Listing credentials")
                                print ('-'*10)
                                for credential in Credentials.display_credentials():
                                    if acct_name == credential.account_name:
                                        print(f"credential: {credential.account_name}        Password:{credential.password}")
                                        print ("\n")
                            

                            elif short_code1 == '2':
                                print("Here is a generated password")
                                new_password = random.randint(10000,99000)

                                print(f"{new_password}")

                            elif short_code1 == '3':
                                break

                            elif short_code1 == 'ex':
                                break
                            else:
                                    print("Kindly use the the following short codes. Thank You.")
                                    print ("\n")  

                    elif short_code == 'dc':
                        if display_credentials():       
                            print("Listing credentials")
                            print ('-'*10)
                            for credential in credential.display_credentials():
                                print(f"Account : {credential.account_name}\nAccount for : {credential.account} \n Username: {credential.user_name} \n Password : {credential.password}")

                                print('')
                        else:
                            print('')
                            print("Oops! Nothing here try 'cc' to add some")
                            print('')           
                    elif short_code == 'fc':
                            print("Enter the Account you want")
                            find_name = input()
                            if credentials_exists(find_name):
                                    find_name = find_credentials(find_name)
                                    print(f"{find_name.account_name}")
                                    print('-'*20)
                                    print(f"Account    {find_name.account_name}")
                                    print(f"Password   {find_name.password}")
                                    print('')

                            else:
                                    print('')
                                    print("Credentials do not exist")
                                    print('')
        
                    elif short_code == 'dl':
                        print("Input name of account to be deleted")
                        delete =input()

                        if user_exist(delete):
                            delete_credential(find_credentials(delete))
                            print ('-'*10)
                            print(f"{delete} haas been deleted \n")                        
                        else:
                            print('-'*10)
                            print ("User doesn't exist")
                    
                    elif short_code == "ex":
                            print("Thanks")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
        elif short_code == "ex":
                print("GoodBye Monsieur.")
                break

if __name__ == '__main__':
    main()
