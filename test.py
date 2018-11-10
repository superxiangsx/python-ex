
#求绝对值的函数，即两点间距离的函数
'''def abs(x,y):
    if x > y:
      return x-y
    else:
      return y-x
'''
# y = |x-1| + 2*|x-2| + 3*|x-3| + 4*|x-4| + ...... + 100*|x-100|
#描述上述函数，min_x和max_x为区间的上下限
def jisuan(x,min_x,max_x):
	j = min_x
	z = 0
	for j in range(min_x, max_x+1):
		z = z + j * abs(x - j)
	print(f"x = {x}, the result is {z}")



for i in range(1,101):
	jisuan(i,1,100)



'''
	j = 1
	z = 0
	for j in range(1,101):
		z = z + j * abs(i - j)
	print(f"i = {i}, z = {z}")
'''

'''
i = 1
while i <= 100:
	j = 1
	z = 0
	for j in range(1,101):
		z = z + j * abs(i - j)
	print(f"i = {i},j = {j}, z = {z}")
	i = i + 1
'''
