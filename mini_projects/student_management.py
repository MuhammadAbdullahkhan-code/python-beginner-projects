"""
Mini Project: Student Management System
------------------------------------------
A small OOP-based system to manage students: add, view, update,
delete, and search records, plus compute simple grade statistics.
"""


class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks   # dict like {"Math": 85, "Science": 90}

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def __str__(self):
        return (f"ID: {self.student_id} | Name: {self.name} | "
                f"Average: {self.average():.2f} | Grade: {self.grade()}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}   # student_id -> Student object

    def add_student(self, student_id, name, marks):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
            return
        self.students[student_id] = Student(student_id, name, marks)
        print(f"Added student: {name}")

    def view_all(self):
        if not self.students:
            print("No students found.")
            return
        print("\n--- All Students ---")
        for student in self.students.values():
            print(student)
        print()

    def find_student(self, student_id):
        return self.students.get(student_id)

    def update_marks(self, student_id, subject, score):
        student = self.find_student(student_id)
        if not student:
            print(f"No student with ID {student_id}.")
            return
        student.marks[subject] = score
        print(f"Updated {student.name}'s {subject} score to {score}.")

    def delete_student(self, student_id):
        if student_id in self.students:
            removed = self.students.pop(student_id)
            print(f"Removed student: {removed.name}")
        else:
            print(f"No student with ID {student_id}.")

    def class_average(self):
        if not self.students:
            return 0
        total = sum(s.average() for s in self.students.values())
        return total / len(self.students)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students.values(), key=lambda s: s.average())

    def search_by_name(self, keyword):
        keyword_lower = keyword.lower()
        matches = [s for s in self.students.values() if keyword_lower in s.name.lower()]
        return matches


def demo():
    sms = StudentManagementSystem()

    sms.add_student(1, "Hira", {"Math": 88, "Science": 92, "English": 79})
    sms.add_student(2, "Talha", {"Math": 65, "Science": 70, "English": 60})
    sms.add_student(3, "Mariam", {"Math": 95, "Science": 98, "English": 91})

    sms.view_all()

    print("Updating Talha's Math score...")
    sms.update_marks(2, "Math", 85)
    sms.view_all()

    print(f"Class average: {sms.class_average():.2f}")

    top = sms.top_student()
    print(f"Top student: {top.name} with average {top.average():.2f}")

    print("Searching for students with 'ri' in their name:")
    results = sms.search_by_name("ri")
    for r in results:
        print(" -", r)

    print("\nDeleting student with ID 2...")
    sms.delete_student(2)
    sms.view_all()


if __name__ == "__main__":
    demo()
