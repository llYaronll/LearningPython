#如何使用數字、數字的用法

#更多數字函式
from math import *

#正數、負數、小數點
print(10)
print(-10)
print(10.1)

#加、減、乘、除、求商、求商整數、求餘數(有先乘除後加減,想先做運算可以用括弧)
print(5+6)
print(8-9)
print(10*8)
print(5/2)
print(5//2)
print(54%8)
print(20+8*7)
print((20+8)*7)

#變數進行運算
number=5
print(number/2)

#字串函式 function
# 1、轉變型態str(); "5"
print(str(number))

# 2、絕對值abs() ; |5|
print(abs(number))

# 3、次方pow() ; 5^2
print(pow(number,2))

# 4、找到數字最大max()
print(max(number,10,20,100))

# 5、找到數字最小min()
print(min(number,10,20,100))

# 6、四捨五入round()
print(round(3.14159))

# 7、無條件捨去floor()
print(floor(7.687))

# 8、無條件進位ceil()
print(ceil(8.1478))

# 9、開根號sqrt();√
print(sqrt(36))





