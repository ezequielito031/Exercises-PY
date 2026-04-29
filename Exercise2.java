class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        self._is_active = True
 
    def get_status(self):
        status = "Active" if self._is_active else "Inactive"
        return f"{self.name} is currently {status} with a {self.gpa} GPA."
 
 
class GradStudent(Student):
    def __init__(self, name, gpa, research_lab):
        super().__init__(name, gpa)
        self.research_lab = research_lab
 
    def get_status(self):
        base_status = super().get_status()
        return f"{base_status} They research in the {self.research_lab} lab."
 
 
class Robot:
    def get_status(self):
        return "BEEP BOOP. Robot systems nominal."
 
 
if __name__ == "__main__":
    student1 = Student("John Doe", 2.8)
    student2 = GradStudent("Jane Smith", 4.0, "Cybersecurity")
 
    print(student1.get_status())
    print(student2.get_status())
 
    entities = [
        Student("Alice", 3.5),
        GradStudent("Bob", 3.9, "AI Data"),
        Robot()
    ]
 
    for entity in entities:
        print(entity.get_status())
}
