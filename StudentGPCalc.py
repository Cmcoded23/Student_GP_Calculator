result = [
    {
        "Course_code": "MTH101",
        "Course_unit": 5,
        "Score": 70,
        "grade": 5
    }
]


def add_score(course_code, course_unit, Score):
    if 70 <= Score <= 100:
        grade = 5
    elif 60 <= Score <= 69:
        grade = 4
    elif 50 <= Score <= 59:
        grade = 3
    elif 45 <= Score <= 49:
        grade = 2
    elif 40 <= Score <= 44:
        grade = 1
    elif 0 <= Score <= 39:
        grade = 0
    elif Score < 0:
        print("Invalid Score")
    result.append(
        {
            "Course_code": course_code,
            "Course_unit": course_unit,
            "Score": Score,
            "grade": grade
        }
    )


def calc_gp():
    total_score = 0
    total_unit = 0
    unitXgradesum = 0
    for course in result:
        if course["Course_code"] != ("done" or "exit"):
            total_score += course["Score"]
            total_unit += course["Course_unit"]
            unitXgradesum += (course["Course_unit"]*course["grade"])
        else:
            break

    gp = unitXgradesum/total_unit
    print(gp)


course_code1 = None
course_unit1 = None
course_score = 0

while True:
    try:
        course_code1 = input("Enter Course Code:")
        course_unit1 = int(input("Enter Course Unit:"))
        course_score = int(input("Enter Your Score:"))
        if course_code1.lower() == ("done" or "exit"):
            break
        elif (course_unit1 or course_score) < 0:
            print("Negative Values Not Allowed")
            break
        add_score(course_code1, course_unit1, course_score)
    except ValueError:
        print("⚠️  Course Unit and Course Score Accepts only Integers")

calc_gp()
