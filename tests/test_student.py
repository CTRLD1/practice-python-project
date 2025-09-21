import unittest

# because we only have one class in student file
from student.student import Student

class TestStudent(unittest.TestCase):

    def test_create_student_object(self):
        new_student = Student('Danah')
        self.assertEqual(new_student.name, 'Danah')