# create a student class that takes in name and major in the contructor

class Student():
    def __init__(self, name_in = "Anonymous", major_in = "Bogus Major"):
        # some instance variables
        self.name = name_in
        self.major = major_in 
        self.grades = []

# a.	It should have a method to add all grades  (which are a list)
    def add_grades(self,grades):
        self.grades.extend(grades)

# b.	It should have a method to add a single grade(a float)
    def add_grade(self, grade):
        self.grades.append(grade)
# c.	It should have a method to compute the average grade and the letter grade
    def compute_grades(self):
        avg = sum(self.grades)/len(self.grades)
        if avg >= 90:
            letter = 'A'
        elif avg >= 80:
            letter = 'B'
        else:
            letter = 'Pass'
        return avg, letter
# d.	It should have a __str__() dunder method to print out the student's basic info: name and major
    def __str__(self) -> str:
        return f"{self.name}:{self.major}"