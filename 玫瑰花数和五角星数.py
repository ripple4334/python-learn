def find_armstrong_numbers(n):
    """
    查找n位自幂数（玫瑰花数n=4，五角星数n=5）
    :param n: 数字位数
    :return: 所有n位自幂数列表
    """
    armstrong_nums = []
    # 确定n位数的范围（10^(n-1) 到 10^n - 1）
    start = 10 ** (n - 1)
    end = (10 ** n) - 1
    
    for num in range(start, end + 1):
        total = 0
        temp = num  # 临时变量，避免修改原数
        # 提取每一位数字并计算n次幂之和
        while temp > 0:
            digit = temp % 10  # 取个位数字
            total += digit ** n  # 累加n次幂
            temp = temp // 10  # 去掉个位数字
        # 判断是否为自幂数
        if total == num:
            armstrong_nums.append(num)
    return armstrong_nums

# 查找玫瑰花数（4位）和五角星数（5位）
rose_nums = find_armstrong_numbers(4)
star_nums = find_armstrong_numbers(5)

# 输出结果
print(f"玫瑰花数（4位自幂数）：{rose_nums}")
print(f"五角星数（5位自幂数）：{star_nums}")
