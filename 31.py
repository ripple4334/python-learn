#定义一个lambda函数，计算一个数的平方,然后使用该函数将一个列表所有元素转化为对应平方值，最后求出这些平方值的和
square = lambda x: x ** 2
numbers = [1, 2, 3, 4, 7]
result = sum(map(square, numbers))
print(result)  