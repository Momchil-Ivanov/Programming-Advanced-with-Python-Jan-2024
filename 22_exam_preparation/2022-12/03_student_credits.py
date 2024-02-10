def students_credits(*courses_info):
    credits_dict = {}
    total_credits = 0
    for course in courses_info:
        course_list = course.split('-')
        name = course_list[0]
        max_credits = int(course_list[1])
        max_points = int(course_list[2])
        reached_points = int(course_list[3])
        ratio = reached_points / max_points
        reached_credits = ratio * max_credits
        total_credits += reached_credits
        credits_dict[name] = reached_credits
    sorted_credits_dict = dict(sorted(credits_dict.items(), key=lambda kvp: -kvp[1]))
    result = ''
    if total_credits >= 240:
        result += f'Diyan gets a diploma with {total_credits:.1f} credits.\n'
    else:
        result += f'Diyan needs {(240 - total_credits):.1f} credits more for a diploma.\n'
    for key in sorted_credits_dict.keys():
        result += f'{key} - {sorted_credits_dict[key]:.1f}\n'
    return result


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
