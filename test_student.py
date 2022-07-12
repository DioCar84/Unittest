import unittest
from student import Student
from datetime import timedelta
from unittest.mock import patch

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

    def test_apply_extension(self):
        print('test_apply_extension')
        old_end_date = self.student.end_date
        self.student.apply_extension(30)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=30))


    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")


    def test_course_schedule_failed(self):
        """
        In the path "student" comes from the name of the file student.py
        If you have named the file something else - it will need to match
        eg, students.py would need "students.requests.get"
        """
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")


if __name__ == '__main__':
    unittest.main()
