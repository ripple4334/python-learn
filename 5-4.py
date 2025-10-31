#每行5个输出1000-2000之间的闰年
k=0
for year in range(1000, 2001):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, end=' ')
        k += 1
        if k % 5 == 0:
            print()