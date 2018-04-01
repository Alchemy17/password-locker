#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
import random

def create_users(name,password):
    '''
    creates login for username
    '''
    new_run_user= User(name,password)
    return new_run_user

def save_new_user(user):
    '''
    Functions that appends a user to the credentials
    '''
    User.save_user()

def account_login(login):
    '''
    Function to login
    '''
    return User.user_login(login)

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