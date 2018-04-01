class User:
    """
    Class that generates new instances of user.
    """

    list_for_users = [] # Empty contact list

    def __init__(self,username, password):

      # docstring removed for simplicity

        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        save_user method saves user objects into list_for_users
        '''
        User.list_for_users.append(self)
    