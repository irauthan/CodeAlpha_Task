#SubjectGradeTracker
class StudentGradeTracker:
    def __init__(self):
        self.grades = {}
    
    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]
    
    def calculate_average(self):
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count > 0 else 0
    
    def display_grades(self):
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")
    
    def run(self):
        while True:
            print("Welcome to Subject Grade Tracker")
            print("\n1.For Add Grade\n2.For Display Grades\n3.For Calculate Average\n4. Exit Program")
            choice = input("Enter your choice:___")
            
            if choice == '1':
                subject = input("Enter subject:____ ")
                try:
                    grade = float(input("Enter grade:___ "))
                    self.add_grade(subject, grade)
                except ValueError:
                    print("Invalid grade. Please enter a number.")
            elif choice == '2':
                self.display_grades()
            elif choice == '3':
                print(f"Average Grade: {self.calculate_average():.2f}")
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    tracker = StudentGradeTracker()
    tracker.run()
