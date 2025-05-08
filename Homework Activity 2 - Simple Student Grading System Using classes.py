#Activity 2: Deadline 2 May - Simple Student Grading System Using classes
#Task: Create students, record their grades, and show results.

class Student:
    def __init__(self,name):
        self.name = name
        self.grade = None

    def set_grade(self,grade):
        if 0 <= grade <= 100:
            self.grade = grade
        else:
            print("Score must be between 0 and 100.")
    
    def get_letter_grade(self):
        if self.grade is None:
            return "-"
        if self.grade >= 90:
            return 'A'
        elif self.grade >= 80:
            return 'B'
        elif self.grade >= 70:
            return 'C'
        elif self.grade >= 60:
            return 'D'
        else :
            return 'F'
        
    def show_grade(self):
        print(f"\nStudent Name : {self.name}")
        print(f"Score : {self.grade}")
        print(f"Grade : {self.get_letter_grade()}")
        print("\n======================")

class GradeRecord:
    def __init__(self):
        self.students = {}

    def add_student(self,name):
        if name not in self.students:
            self.students[name] = Student(name)
        else:
            print(f"{name} is already in the system. Score will be updated")
    
    def record_grade(self,name,grade):
        if name in self.students:
            self.students[name].set_grade(grade)
        else:
            print(f"{name} not found in the system")

    def show_all_results(self):
        for student in self.students.values():
            student.show_grade()

#Start
gradebook = GradeRecord()

while True:
    name = input("\nPlease input student name (or 'exit' to show the results) : ")
    if name.strip().lower() == 'exit':
        break

    gradebook.add_student(name)

    while True:
        try:
            grade_input = float(input(f"please insert {name} score : "))
            if 0 <= grade_input <= 100: 
                gradebook.record_grade(name, grade_input)
                break
            else:
                print("Score must be between 0 and 100")
        except ValueError:
            print("Please enter the number")
          

print("\n ===== Student Grade =====")
gradebook.show_all_results()
