#写出判断年份是否为闰年的程序，并输出2000-2030年之间的所有闰年。并控制每行五个输出
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
leap_years = []
for year in range(2000, 2031):
    if is_leap_year(year):
        leap_years.append(year)
print("2000-2030年之间的闰年有：")
for index, year in enumerate(leap_years):
    print(f"{year}", end=' ')
    if (index + 1) % 5 == 0:
        print()  # 每行输出五个闰年