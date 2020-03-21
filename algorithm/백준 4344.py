n = int(input())
student_lists = list()

for _ in range(n):
    student_lists.append(list(map(int, input().split())))

for student_list in student_lists:
    num_of_students = student_list[0]
    mean = sum(student_list[1:])/num_of_student 
    count = 0
    for score in student_list[1:]:
        if mean < score:
            count += 1
    print('%0.3f' %((count/num_of_student)*100)+ '%')