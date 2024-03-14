# import our modules

from student import Student
from info_logger import Logger
# student.Student

# let's get student details

# def get_name():
#     name = input("Name:")
#     return name
# def get_major():
#     major = input("Major:")
#     return major

def get_user_details():
    name = input("Name:")
    major = input("Major:")
    # create class instance of student
    my_student = Student(name_in= name, major_in= major)
    # details = {"major":major, "name":name}
    return my_student


if __name__ == "__main__":
    # name = get_name() # ask user for name
# major = get_major()  # major
    
    # create a logger

    my_logger = Logger()

    for _ in range(5):
        student_details  = get_user_details()
        # print(f"Hello {student_details.name} I hope you're enjoying your {student_details.major} major")
        my_logger.LogRow(f"{str(student_details)}")
