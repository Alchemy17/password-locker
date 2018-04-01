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
        self.new_credential = Credential("Abdul","twitter","maanoatu1","12345a") # create credentials object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.list_for_credentials=[]

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_contact.account_name,"Abdul")
        self.assertEqual(self.new_contact.account,"twitter")
        self.assertEqual(self.new_contact.user_name,"maanoatu1")
        self.assertEqual(self.new_contact.password,"12345a")