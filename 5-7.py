#从键盘输入若干整数，当输入A时，求出这些整数奇数和，偶数和，和所有数平均值
odd_sum = 0
even_sum = 0 
count = 0
total_sum = 0
while True:
    s = input("请输入一个整数（输入A结束）：")
    if s.upper() == 'A':
        break
    try:
        num = int(s)
        total_sum += num
        count += 1
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    except ValueError:
        print("请输入有效的整数或A结束。")
if count > 0:
    average = total_sum / count
    print(f"奇数和: {odd_sum}")
    print(f"偶数和: {even_sum}")
    print(f"所有数的平均值: {average:.2f}")
else:
    print("没有输入任何整数。")