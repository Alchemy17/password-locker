class User:
    """
    Class that generates new instances of user.
    """

    list_for_users = [] # Empty contact list

    def __init__(self,username, password):

        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        save_user method saves user objects into list_for_users
        '''
        self.list_for_users.append(self)
    
    @classmethod
    def user_exists(cls, username):
        '''
        A method that determines if a user exists
        '''
        for user in cls.list_for_users:
            if user.username == username:
                return True
        return False