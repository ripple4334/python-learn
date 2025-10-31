#计算1*2*3+3*4*5+5*6*7+...+97*98*99+99*100*101的值
total = 0
for i in range(1, 100, 2):
    total += i * (i + 1) * (i + 2)
print(total)