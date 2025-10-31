#0-100之间随机整数最大公约数和最小公倍数
import random
rnd1=random.randint(0,100)
rnd2=random.randint(0,100)
print(f"随机生成的两个整数是：{rnd1}和{rnd2}")
#计算最大公约数的函数
def gcd(a,b):
    if b==0:
        return a
    if a==0:
        return b
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
#计算最大公约数
greatest_common_divisor=gcd(rnd1,rnd2)
#计算最小公倍数
if rnd1==0 or rnd2==0:
    least_common_multiple=0
else:
    least_common_multiple=abs(rnd1*rnd2)//greatest_common_divisor
print(f"{rnd1}和{rnd2}的最大公约数是：{greatest_common_divisor}")
print(f"{rnd1}和{rnd2}的最小公倍数是：{least_common_multiple}")