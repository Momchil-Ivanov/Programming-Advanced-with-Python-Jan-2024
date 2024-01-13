n_students = int(input())

students = {}

for x in range(0, n_students):
    student, score = input().split()
    grade = float(score)

    if student not in students:
        students[student] = []

    students[student].append(grade)

for name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '.join([f'{(g):.2f}' for g in grades])}"
    print(f"{name} -> {formatted_grades} (avg: {avg_grade:.2f})")