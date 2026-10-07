def list_students(students):
    print("\n--- LIST OF STUDENTS ---")
    if not students:
        print("No students found.")
        return
    for s in students:
        print(s)


def list_courses(courses):
    print("\n--- LIST OF COURSES ---")
    if not courses:
        print("No courses found.")
        return
    for c in courses:
        print(c)


def show_marks(students, courses, marks):
    if not marks:
        print("No marks recorded yet.")
        return

    c_id = input("\nEnter course ID to show marks: ")
    if c_id not in marks:
        print("No marks found for this course!")
        return

    print(f"\n--- MARKS FOR COURSE ID: {c_id} ---")
    for s_id, mark in marks[c_id].items():
        student = next((s for s in students if s.get_id() == s_id), None)
        s_name = student.get_name() if student else "Unknown"
        print(f"ID: {s_id} | Name: {s_name} | Mark: {mark}")
