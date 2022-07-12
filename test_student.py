import unittest
from student import Student

class TestStudent(unittest.TestCase):

    @classmethod
    # used to create a set up for all tests in the class
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    # used to remove the set up for all tests in the class
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        # used to create a set up for a test
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        # used to remove the set up for a test
        print('tearDown')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')


    def test_email(self):
        print('test_email')
        self.assertEqual(self.student.email, 'john.doe@email.com')

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)


if __name__ == '__main__':
    unittest.main()

