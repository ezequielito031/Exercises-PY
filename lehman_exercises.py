class LehmanCourse:
    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits
        self._student_count = 0

    def enroll_student(self):
        self._student_count += 1

    def display_info(self):
        print(f"Course: {self.course_name} | Credits: {self.credits} | Enrolled: {self._student_count}")


class LabCourse(LehmanCourse):
    def __init__(self, course_name, credits, lab_fee):
        super().__init__(course_name, credits)
        self.lab_fee = lab_fee

    def display_info(self):
        print(f"Course: {self.course_name} | Credits: {self.credits} | Enrolled: {self._student_count} | Lab Fee: ${self.lab_fee:.2f}")


class Professor:
    def get_role(self):
        return "Teaching and Research"


class Student:
    def get_role(self):
        return "Learning and Coding"


def print_role(person):
    print(f"Role: {person.get_role()}")


cmp269 = LehmanCourse("CMP 269", 4)
cmp269.enroll_student()
cmp269.enroll_student()
cmp269.enroll_student()
cmp269.display_info()

bio310 = LabCourse("BIO 310", 4, 75.00)
bio310.enroll_student()
bio310.enroll_student()
bio310.display_info()

prof = Professor()
student = Student()
print_role(prof)
print_role(student)
