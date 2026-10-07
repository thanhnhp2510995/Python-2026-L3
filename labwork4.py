import math
import os
import pickle
import zipfile


#ENTITY CLASSES
class Student:

    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
def get_id(self):
  return sefl.__id

def get_name(self):
        return self.__name
def get_dob(self):
        return self.__dob
ef __str__(self):
        return f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}"

class coures:
  def __init__(self, course_id, name, credits):
        self.__id = course_id
        self.__name = name
        self.__credits = credits
  def get__id(self):
    return self.__id
  def get__name(self):
    return sefl.__name
  def get_credit(self):
    return self.__credit
  def __str__(self):
        return f"ID: {self.__id} | Name: {self.__name} | Credits: {self.__credits}"
  class MarkManagementSystem:

    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
        self.dat_file = "students.dat"
    def load_data(self):
      if os.path.exists(self.dat_file):
            print(f"[PW5] Found '{self.dat_file}'. Decompressing and loading data..."
            )
      try:
        with zipfile.Zipfile(self.dat_file, "r") as zip_ref:
          zip_ref.extractall(".")
          if os.path.exists("data.pkl"):
                    with open("data.pkl", "rb") as f:
                        self.students, self.courses, self.marks = pickle.load()    
                  print("[PW5] Data loaded successfully!")
            except Exception as e:
                print(f"[PW5] Error loading data: {e}")
        else:
            print(
                f"[PW5] '{self.dat_file}' not found. Starting with empty system."
            )
        def save_data(self):
        print(f"\n[PW5] Saving and compressing data into '{self.dat_file}'...")

        # 1. Write text files
        with open("students.txt", "w") as f:
            for s in self.students:
                f.write(f"{s.get_id()},{s.get_name()},{s.get_dob()}\n")

        with open("courses.txt", "w") as f:
            for c in self.courses:
                f.write(f"{c.get_id()},{c.get_name()},{c.get_credits()}\n")

        with open("marks.txt", "w") as f:
            for c_id, student_marks in self.marks.items():
                for s_id, mark in student_marks.items():
                    f.write(f"{c_id},{s_id},{mark}\n")
        # 2. Serialize current state
        with open("data.pkl", "wb") as f:
            pickle.dump((self.students, self.courses, self.marks), f)

        # 3. Compress into students.dat
        with zipfile.ZipFile(
            self.dat_file, "w", zipfile.ZIP_DEFLATED
        ) as zip_ref:
            zip_ref.write("students.txt")
            zip_ref.write("courses.txt")
            zip_ref.write("marks.txt")
            zip_ref.write("data.pkl")

        # Clean up temporary text/pickle files
        for temp_file in [
            "students.txt",
            "courses.txt",
            "marks.txt",
            "data.pkl",
        ]:
            if os.path.exists(temp_file):
                os.remove(temp_file)

        print("[PW5] Compression completed. Goodbye!")

    def input_student(self):
      count = int(input("Enter numbers of student: "))
      for i range(count):
          print(f"\n--- Student {i + 1} ---")
          s_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter DoB: ")
            self.students.append(Student(s_id, name, dob))
        
    def input_course(self):
      count = int(input("Enter numbers of course:"))
      for i range(count):
          print(f"\n--- Course {i + 1} ---")
          s_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            credits = float(input("Enter credits: "))
            self.courses.append(Course(c_id, name, credits))

    def input_marks(self):
        if not self.courses or not self.students:
            print("Please add both students and courses first!")
            return

        self.list_courses()
        c_id = input("\nSelect course ID to enter marks: ")

        course = next((c for c in self.courses if c.get_id() == c_id), None)
        if not course:
            print("Invalid course ID!")
            return

        if c_id not in self.marks:
            self.marks[c_id] = {}

        print(f"\n--- Entering marks for course {course.get_name()} ---")
        for s in self.students:
            raw_mark = float(
                input(
                    f"Enter mark for {s.get_name()} (ID: {s.get_id()}): "
                )
            )
            rounded_mark = math.floor(raw_mark * 10) / 10.0
            self.marks[c_id][s.get_id()] = rounded_mark
            def list_students(self):
        print("\n--- List of Students ---")
        if not self.students:
            print("No students added yet.")
            return
        for s in self.students:
            print(s)


    def list_courses(self):
        print("\n--- List of Courses ---")
        if not self.courses:
            print("No courses added yet.")
            return
        for c in self.courses:
            print(c)


    def show_marks(self):
        if not self.marks:
            print("No marks available.")
            return

        c_id = input("\nEnter course ID to show marks: ")
        if c_id not in self.marks:
            print("No marks found for this course!")
            return

        print(f"\n--- Marks for Course ID: {c_id} ---")
        for s_id, mark in self.marks[c_id].items():
            s = next(
                (stud for stud in self.students if stud.get_id() == s_id), None
            )
            s_name = s.get_name() if s else "Unknown"
            print(f"ID: {s_id} | Name: {s_name} | Mark: {mark}")
    
    def run(self):
      self. load_data()
      while True:
        choice = input("Enter choice": )
        if choice == "0":
            self.save_data()
            break
