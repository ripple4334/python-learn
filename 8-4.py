#(1)创建空字典
dic_sthudent = {}
#(2)录入5名学生的信息
for i in range(5):
    print(f"请输入第{i+1}名学生的信息：")
    classroom=input("班级：")
    name = input("姓名：")
    age = input("年龄：")
    height = input("身高（cm）：")
    weight = input("体重（kg）：")
    dic_sthudent[name] = [age, height, weight, classroom]
#(3)输出字典内容
print("\n字典dic_sthudent的内容为：")
for name, info in dic_sthudent.items():
    print(f"{info[3]}\t{name}\t{info[0]}\t{info[1]} cm\t{info[2]} kg")