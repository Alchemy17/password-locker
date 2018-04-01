import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Abdulrahman", "Mohamed")
    
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.list_for_users=[]
    def test_init(self):
        '''
        this function tests an a user object is properly initialized
        '''
        self.assertEqual(self.new_user.username,"Abdulrahman")
        self.assertEqual(self.new_user.password,"Mohamed")
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list            
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.list_for_users),1)

if __name__ == '__main__':
    unittest.main()