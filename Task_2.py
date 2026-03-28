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