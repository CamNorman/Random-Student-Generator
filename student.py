"""
basic introduction of a student identifying your name, age,
and what school you are attending
"""

import random

# Creating the student Class
class Student:

    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def introduce(self):
        return f"""Hey I'm {self.name}, I am {self.age} years
                old and I'm from {self.school}."""

    def fun_fact(self, fun_fact):
        self.fun_fact = fun_fact
        return f"A fun fact about{self.name} is {self.fun_fact}"


if __name__ == "__main__":
    my_self = Student("Cameron", 23, "Univeristy High School")
    # print(my_self.name)
"""
#Stringing student into the bloomtech student but adding another action
#it will also generate 30 random student names and print you out one at random
"""

# Creating the Bloomtech Student Class
class BloomTechStudent(Student):
    def __init__(self, name, age, school, planned_graduation):
        super().__init__(name, age, school)
        self.planned_graduation = planned_graduation

    def __repr__(self):
        return f"""{self.name} plans on graduating {self.school}
                    in {self.planned_graduation}"""


if __name__ == "__main__":
    myself = BloomTechStudent("Cameron", 23, "BloomTech", 2024)
    # print(myself.name)

# Calling a student Generator
def student_generator(num_students=30):

    first_names = ["John", "Cameron", "Jason", "AAron", "TJ"]
    last_names = ["Namron", "Gordon", "Jones", "Kelce", "Trudeau"]

    random_first_name = random.choice(first_names)
    random_last_name = random.choice(last_names)

    random_name = random_first_name + " " + random_last_name

    age = random.randint(18, 68)

    school = "Bloomtech"

    students = []

    for _ in range(num_students):
        students.append(Student(random_name, age, school))

    return students


student_list = student_generator(30)


print(student_list[0].name)
print(student_list[0].age)
print(student_list[0].school)
