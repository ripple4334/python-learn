#重复元素判定，编写一个函数，接受一个列表作为参数，如果一个元素在列表中出现超过一次，则返回True，但不要改变原列表值
#最后在主程序测试该函数
def has_duplicates(lst):
    for item in lst:
        if lst.count(item) > 1:
            return True
    return False
#主程序测试
test_list1 = [1, 2, 3, 4, 5]
print(has_duplicates(test_list1))
test_list2 = [1,2,1,3]
print(has_duplicates(test_list2))