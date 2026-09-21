students=[]
n=int (input("请输入学生人数："))
for i in range(n):
    name=input(f"请输入第{i+1}名学生的姓名：")
    score=float(input(f"请输入学生{name}成绩"))
    student={"name":name,"score":score}
    students.append(student)
print("\n------成绩单------") 
for student in students:
    print(f"{student["name"]}的成绩是{student["score"]}")
total=0
for student in students:
    total=total+student["score"]
average=total/len(students)
best_student=students[0]
for student in students:
    if student["score"]>best_student["score"]:
        best_student=student        
print(f"最高分学生：{best_student["name"]},"
      f"成绩：{best_student["score"]}")