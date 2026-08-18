students = {
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Ethan",
    "Fiona",
    "George",
    "Hannah",
    "Ivan",
    "Julia"
}

completed_courses = {
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Ethan",
    "Fiona",
    "George",
    "Hannah"
}

attendance_above_75 = {
    "Alice",
    "Bob",
    "David",
    "Ethan",
    "Fiona",
    "George",
    "Hannah",
    "Ivan"
}

has_backlog = {
    "Charlie",
    "Ivan",
    "Julia"
}

good_performance = {
    "Alice",
    "Bob",
    "David",
    "Ethan",
    "Fiona",
    "George",
    "Hannah"
}

eligible_for_scholarship = set()
needs_academic_support = set()
eligible_for_progression = set()
not_recommended = set()

for student in students:
    if (
        student in completed_courses
        and student in attendance_above_75
        and student in good_performance
        and student not in has_backlog
    ):
        eligible_for_scholarship.add(student)

for student in students:
    if (
        student not in attendance_above_75
        or student in has_backlog
    ):
        needs_academic_support.add(student)

for student in students:
    if (
        student in completed_courses
        and student in attendance_above_75
        and student in good_performance
        and student not in has_backlog
    ):
        eligible_for_progression.add(student)

for student in needs_academic_support:
    not_recommended.add(student)

print("==============================================")
print("STUDENT ACADEMIC DSS")
print("==============================================")

print("\nStudents:")
print(students)

print("\nCompleted Courses:")
print(completed_courses)

print("\nAttendance Above 75%:")
print(attendance_above_75)

print("\nStudents With Backlog:")
print(has_backlog)

print("\nGood Performance:")
print(good_performance)

print("\n==============================================")
print("INFERRED RESULTS")
print("==============================================")

print("\nStudents Eligible for Scholarship:")
for student in sorted(eligible_for_scholarship):
    print(student)

print("\nStudents Requiring Academic Support:")
for student in sorted(needs_academic_support):
    print(student)

print("\nStudents Eligible for Progression:")
for student in sorted(eligible_for_progression):
    print(student)

print("\nStudents Not Recommended for Immediate Progression:")
for student in sorted(not_recommended):
    print(student)

print("\n==============================================")
print("SCHOLARSHIP QUERY RESULTS")
print("==============================================")


def query_scholarship(student):
    print("\nStudent:", student)

    if student in eligible_for_scholarship:
        print("Eligible for Scholarship: YES")
    else:
        print("Eligible for Scholarship: NO")


query_scholarship("Alice")
query_scholarship("Bob")
query_scholarship("Charlie")
query_scholarship("David")
query_scholarship("Ethan")
query_scholarship("Fiona")
query_scholarship("George")
query_scholarship("Hannah")
query_scholarship("Ivan")
query_scholarship("Julia")