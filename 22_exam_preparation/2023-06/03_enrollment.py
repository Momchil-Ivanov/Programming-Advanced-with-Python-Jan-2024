def gather_credits(needed_credits: int, *course_info):
    needed_credits_left = needed_credits
    courses_dict = {}
    credits_gained = 0
    for course in course_info:
        if credits_gained >= needed_credits:
            break
        name = course[0]
        credits = int(course[1])
        if name not in courses_dict.keys():
            courses_dict[name] = credits
            needed_credits_left -= credits
            credits_gained += credits
    result = ''
    if credits_gained >= needed_credits:
        sorted_dict = dict(sorted(courses_dict.items(), key=lambda kvp: [kvp[0]]))
        result += f'Enrollment finished! Maximum credits: {credits_gained}.\n'
        result += f'Courses: {", ".join(sorted_dict.keys())}'
    else:
        result += f'You need to enroll in more courses! You have to gather {needed_credits_left} credits more.'
    return result


print(gather_credits(
    60,
    ("Fundamentals", 27),
    ("Basics", 27),
    ("Advanced", 30),
    ("Web", 30)
))
