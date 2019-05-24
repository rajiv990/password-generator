import unittest
from password_gen import total_passwords, simple_password_gen
import re


class TestSimplePasswordGenerator(unittest.TestCase):

    # Number of passwords generated must be greater than or equal to one
    def test_check_correct_input(self):
        if total_passwords <= 0:
            print('The number of passwords to be entered must be greater than zero')

    # Number of passwords requested by a user must be the same as the number of passwords generated
    def test_number_of_passwords(self):
        count = 0
        while count != total_passwords:
            count += 1
        self.assertEqual(total_passwords, count, 'Invalid number of passwords created')

    # Length of password generated should be equal to length passed in the method
    def test_password_length(self):
        self.assertEqual(len(simple_password_gen(20)), 20, 'Password lengths are different')

    # Check if password has numbers, lowercase, uppercase and special characters
    def test_validate_criteria(self):
        password = simple_password_gen()
        self.assertTrue(re.search(r'\w', password) and      # Checking for alphanumeric characters
                        re.search(r'\W', password),         # Checking for special characters
                        'Password must have uppercase, lowercase, numbers and special characters ')


if __name__ == '__main__':
    unittest.main()

