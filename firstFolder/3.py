student_list = []


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def average_mark(self):
        number = len(self.marks)
        if number == 0:
            return 0
        total = sum(self.marks)
        return total / number


def create_student():
    name = input("Please enter the new student's name: ")
    # student_data = {
    #     'name': name,
    #     'marks': []
    # }
    student_data = Student(name)
    return student_data


def add_mark(student, mark):
    student.marks.append(mark)


# # def calculate_average_mark(student):
# #     number = len(student['marks'])
# #     if number == 0:
# #         return 0

#     total = sum(student['marks'])
#     return total/number


def print_student_details(student):
    print(f'{student.name}, average mark: {student.average_mark()}.')


def print_student_list(students):
    for i, student in enumerate(students):
        print(f'ID: {i}')
        print_student_details(student)


def menu():
    # Add a student (to student_list)
    # Add a mark to student
    # print a list of students
    # exit the application
    selection = input("Enter 'p' to print the student list,"
                      "'s' to add a new student,"
                      "'a' to add a mark to a student"
                      "or 'q' to quit.\n"
                      "enter your selection: ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection == 'a':
            student_id = int(input('Enter the student ID to add a mark to: '))
            student = student_list[student_id]
            new_mark = int(input('Enter the new mark to be added: '))
            add_mark(student, new_mark)

        selection = input("Enter 'p' to print the student list,"
                          "'s' to add a new student,"
                          "'a' to add a mark to a student"
                          "or 'q' to quit.\n"
                          "enter your selection: ")


menu()
