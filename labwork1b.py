students = []
courses = []
marks = {} 

def input_number_of_students():
    count = int(input("Enter number of students: "))
    return count


def input_student_info():
    num_students = input_number_of_students()
    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter Date of Birth (DoB): ")
        students.append({"id": student_id, "name": name, "dob": dob})


def input_number_of_courses():
    count = int(input("Enter number of courses: "))
    return count


def input_course_info():
    num_courses = input_number_of_courses()
    for i in range(num_courses):
        print(f"\n--- Course {i + 1} ---")
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append({"id": course_id, "name": name})


def input_marks_for_course():
    if not courses:
        print("No courses available! Please add courses first.")
        return
    if not students:
        print("No students available! Please add students first.")
        return

    list_courses()
    course_id = input("\nSelect a course ID to enter marks: ")

    course_exists = any(c["id"] == course_id for c in courses)
    if not course_exists:
        print("Invalid course ID!")
        return

    if course_id not in marks:
        marks[course_id] = {}

    print(f"\n--- Entering marks for course {course_id} ---")
    for student in students:
        s_id = student["id"]
        mark = float(
            input(
                f"Enter mark for student {student['name']} (ID: {s_id}): "
            )
        )
        marks[course_id][s_id] = mark


def list_courses():
    print("\n--- List of Courses ---")
    if not courses:
        print("No courses added yet.")
        return
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")


def list_students():
    print("\n--- List of Students ---")
    if not students:
        print("No students added yet.")
        return
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")


def show_student_marks():
    if not marks:
        print("No marks available yet.")
        return

    course_id = input("\nEnter course ID to show marks: ")
    if course_id not in marks:
        print("No marks entered for this course!")
        return

    print(f"\n--- Marks for Course {course_id} ---")
    for s_id, mark in marks[course_id].items():
        # Find student name
        s_name = next(
            (s["name"] for s in students if s["id"] == s_id), "Unknown"
        )
        print(f"Student ID: {s_id} | Name: {s_name} | Mark: {mark}")


def main():
    while True:
        print("\n================ SYSTEM MENU ================")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("0. Exit")
        print("=============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            input_student_info()
        elif choice == "2":
            input_course_info()
        elif choice == "3":
            input_marks_for_course()
        elif choice == "4":
            list_students()
        elif choice == "5":
            list_courses()
        elif choice == "6":
            show_student_marks()
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again!")


if __name__ == "__main__":
    main()
