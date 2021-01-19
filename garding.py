student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


def gradingEval(score):
    if score >= 91:
        return 'Outstanding'
    elif score >= 81:
        return 'Exceeds Expectations'
    elif score >= 71:
        return 'Acceptable'
    elif score <= 70:
        return 'Fail'


student_grades = {}

for key in student_scores:
    student_grades[key] = gradingEval(student_scores[key])

print(student_grades)
