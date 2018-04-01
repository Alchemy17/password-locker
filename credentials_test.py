import random
import unittest
from credentials import Credentials
from user import User

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("Abdul","twitter","maanoatu1","12345a") # create credentials object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.list_for_credentials=[]

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.account_name,"Abdul")
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.user_name,"maanoatu1")
        self.assertEqual(self.new_credential.password,"12345a")
    
    def test_save_credentials(self):
        '''
        Test case that checks if the save functions adds credentials to the list
        '''
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.list_for_credentials),1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Test","twitter","user","0124") # new credential
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.list_for_credentials),2)
    
    def test_delete_credentials(self):
        '''
        test_delete_credential to test if we can remove a credential from our credential list
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Test","twitter","user","0124") # new credential
        test_credential.save_credentials()

        self.new_credential.delete_credentials()# Deleting a credential object
        self.assertEqual(len(Credentials.list_for_credentials),1)

    def test_find_credential_by_name(self):
        '''
        checks if we can find an account by name
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Test","twitter","user","0124")
        test_credential.save_credentials()

        found_credential = Credentials.find_by_name("Test")
        self.assertEqual(found_credential.user_name,test_credential.user_name)

    def test_credential_exists(self):
        '''
        Test returns a boolean if contact exists or not.
        '''
        self.new_credential.save_credentials()
        test_credential = Credentials("Felix","twitter","Felback24")
        test_credential.save_credentials()

        credential_exist = Credentials.credential_exists("Felix")
        self.assertTrue(credential_exist)
       


if __name__ == '__main__':
    unittest.main()