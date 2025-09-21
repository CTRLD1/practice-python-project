class Student:
    # Store a student's name, and a list of grades.
    def __init__(self, name):
        self.name = name
        self.grades = []

# we do this so the prompt doesnt show in the code
if __name__ == '__main__':
    student_name = input('Enter the new student name: ')
    new_student = Student(student_name)
    print(f'welcome {new_student.name}')
