class Credentials:

    list_for_credentials = []


    '''
    class for storing credentials of users
    '''
    def __init__ (self, account_name, account, user_name, password):
        
        self.account_name = account_name
        self.account = account
        self.user_name = user_name
        self.password = password        

    def save_credentials(self):
        '''
        save functions adds credentials to the list
        '''
        self.list_for_credentials.append(self)
    
    def delete_credentials(self):
        '''
        delete credentials from the list
        '''
        Credentials.list_for_credentials.remove(self)

    @classmethod
    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a credentials that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for credential in cls.list_for_credentials:
            if credential.account_name == name:
                return credential
    
    @classmethod
    def credential_exists(cls,name):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credential in cls.list_for_credentials:
            if credential.account_name == name:
                return credential
    
    @classmethod
    def display_credentials(cls):

            '''
            method that returns the entire list_for_credentials
            '''

            return cls.list_for_credentials


     