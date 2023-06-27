num_students = int(input())
students_grades = {}

for student in range(num_students):
    name, grade = tuple(input().split())
    grade = float(grade)
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(f"{float(grade):.2f}")

for name, grades in students_grades.items():
    print(f"{name} -> {' '.join([str(f'{grade}') for grade in grades])} (avg: "
          f"{(sum(float(num) for num in grades)/len(grades)):.2f})")

# number_of_students = int(input())
#
# result = {}
# for student in range(number_of_students):
#     student_name, student_grade = input().split()
#     result[student_name] = result.get(student_name, list())
#     result[student_name].append(f"{float(student_grade):.2f}")
#
# for name, grades in result.items():
#     print(f"{name} -> {' '.join(grades)} (avg: {(sum(float(num) for num in grades)/len(grades)):.2f})")

