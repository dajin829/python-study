grade=input("你的成绩是多少？")
grade=int(grade)
if(grade>=90 and grade<=100):
    print(f"你的成绩是{grade},评级是A！")
elif(grade>=80):
    print(f"你的成绩是{grade},评级是B！")
elif(grade>=70):
    print(f"你的成绩是{grade},评级是C！")
elif(grade>=60):
    print(f"你的成绩是{grade},评级是D！")
if(grade<60 and grade>=0):
    print(f"你的成绩是{grade},评级是不及格！")
if(grade>100 or grade<0):
    print(f"你的成绩是{grade},输入有误！")