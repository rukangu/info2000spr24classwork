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
    details = {"major":major, "name":name}
    return details

# name = get_name() # ask user for name
# major = get_major()  # major
student_details  = get_user_details()

# print(f"Hello {student_details[0]} I hope you're enjoying your {student_details[1]} major")

# dictionary
print(f"Hello {student_details['name']} I hope you're enjoying your {student_details['major']} major")