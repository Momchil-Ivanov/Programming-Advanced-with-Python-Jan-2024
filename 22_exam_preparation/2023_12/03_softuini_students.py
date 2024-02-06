def softuni_students(*students, **courses):
    students_dict = {}
    for student_name in students:
        students_dict[student_name[1]] = student_name[0]

    finished_students_messages = []
    invalid_students = []
    result = ''
    for student_id in courses.keys():
        for name, current_id in students_dict.items():
            if current_id == student_id:
                finished_students_messages.append(f'*** A student with the username {name} has successfully finished the course {courses[student_id]}!\n')

    for name, current_id in students_dict.items():
        if not current_id in courses.keys():
            invalid_students.append(name)

    finished_students_messages = sorted(finished_students_messages)
    for student in finished_students_messages:
        result += student
    if invalid_students:
        result += f'!!! Invalid course students: {", ".join(sorted(invalid_students))}'

    return result

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))