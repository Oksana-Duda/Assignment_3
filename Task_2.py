def get_succesful_students(student_list, passing_grade=60):
    suc_st = []
    for student in student_list:
        cnt = True
        for value in student["scores"].values():
            if value < passing_grade:
                cnt = False
        if cnt:
            suc_st.append(student)
    return suc_st

new_dict = {}
students_math_results = [
{"name": "Олександр", "scores": {"Calculus": 85,
"Algebra": 90, "Discrete Math": 78}},
{"name": "Марія", "scores": {"Calculus": 65, "Algebra":
55, "Discrete Math": 70}},
{"name": "Іван", "scores": {"Calculus": 92, "Algebra": 88,
"Discrete Math": 95}},
{"name": "Анна", "scores": {"Calculus": 45, "Algebra": 60,
"Discrete Math": 50}}
]
good_students = get_succesful_students(students_math_results)

for student in good_students:
    sum=0
    for value in student["scores"].values():
        sum = sum+value
    sum = sum/3
    new_dict[student["name"]] = round(sum, 2)
print(new_dict)