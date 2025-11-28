# 1. 读取score.txt文件内容
students = []
with open("C:/Users/wangh/Desktop/作业/python作业/9-14/score.txt", "r", encoding="utf-8") as f:
    next(f)
    for line in f:
        line = line.strip() 
        if line: 
            sno,平时,期末 = line.split(",")
            平时 = int(平时)
            期末 = int(期末)
            总评 = round(平时 * 0.4 + 期末 * 0.6)
            students.append( (sno, 平时, 期末, 总评) )

# 2. 按总评成绩降序排序
students.sort(key=lambda x: x[3], reverse=True)

# 3. 保存到新文件（比如new_score.txt）
with open("C:/Users/wangh/Desktop/作业/python作业/9-14/newscore.txt", "w", encoding="utf-8") as f:
    f.write("学号,平时成绩,期末成绩,总评成绩\n")
    for s in students:
        f.write(f"{s[0]},{s[1]},{s[2]},{s[3]}\n")

print("结果已保存到new_score.txt")
