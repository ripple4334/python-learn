#写出判断素数的函数并生成300以内的素数列表并控制一行五个输出
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
prime_numbers = [num for num in range(2, 300) if is_prime(num)]
print("300以内的素数列表如下：")
for index, prime in enumerate(prime_numbers):
    print(f"{prime:4}", end=' ')
    if (index + 1) % 5 == 0:
        print()  # 每行输出五个素数
