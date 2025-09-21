import unittest

# because we only have one class in student file
from student.student import Student

class TestStudent(unittest.TestCase):
    # setup function to setup our student
    def setUp(self):
        self.student = Student('Danah')

    def test_create_student_object(self):
        # new_student = Student('Danah')
        self.assertEqual(self.student.name, 'Danah')

    def test_add_valid_grade(self):
        self.student.add_grade(50)
        self.assertIn(50, self.student.grades)
        self.student.add_grade(100)
        self.assertIn(100, self.student.grades)
        self.student.add_grade(0)
        self.assertIn(0, self.student.grades)

    def test_add_invalid_grade(self):
        with self.assertRaises(ValueError):
            self.student.add_grade(101)

        with self.assertRaises(TypeError):
            self.student.add_grade('hello')

        with self.assertRaises(ValueError):
            self.student.add_grade(-1)

    
    def test_average_no_grades(self):
        self.assertEqual(self.student.average(), 0)
    
    def test_average_with_grades(self):
        for grade in [20, 40, 60]:
            self.student.add_grade(grade)
        # i have to calculate the average myself
        self.assertEqual(self.student.average(), 40)