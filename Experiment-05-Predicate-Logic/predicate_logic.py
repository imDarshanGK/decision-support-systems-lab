students = {
    "Alice",
    "Bob",
    "Charlie",
    "David"
}

high_attendance = {
    "Alice",
    "Charlie",
    "David"
}

low_attendance = {
    "Bob"
}

good_performance = {
    "Alice",
    "Bob",
    "David"
}

low_performance = {
    "Charlie"
}

needs_support = set()
eligible = set()
not_recommended = set()

for student in students:
    if student in low_attendance:
        needs_support.add(student)

for student in students:
    if student in low_performance:
        needs_support.add(student)

for student in students:
    if student in high_attendance and student in good_performance:
        eligible.add(student)

for student in needs_support:
    not_recommended.add(student)

print("==============================================")
print("KNOWLEDGE BASE")
print("==============================================")

print("\nStudents:")
print(students)

print("\nHigh Attendance:")
print(high_attendance)

print("\nLow Attendance:")
print(low_attendance)

print("\nGood Performance:")
print(good_performance)

print("\nLow Performance:")
print(low_performance)

print("\n==============================================")
print("INFERRED KNOWLEDGE")
print("==============================================")

print("\nStudents Requiring Academic Support:")
for student in sorted(needs_support):
    print(student)

print("\nStudents Eligible for Progression:")
for student in sorted(eligible):
    print(student)

print("\nStudents Not Recommended for Immediate Progression:")
for student in sorted(not_recommended):
    print(student)

print("\n==============================================")
print("QUERY RESULTS")
print("==============================================")


def query_student(student):
    print("\nStudent:", student)

    if student in needs_support:
        print("Needs Academic Support: YES")
    else:
        print("Needs Academic Support: NO")

    if student in eligible:
        print("Eligible for Progression: YES")
    else:
        print("Eligible for Progression: NO")

    if student in not_recommended:
        print("Immediate Progression Recommendation: NO")
    else:
        print("Immediate Progression Recommendation: YES")


query_student("Alice")
query_student("Bob")
query_student("Charlie")
query_student("David")