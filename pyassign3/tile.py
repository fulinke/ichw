# !/usr/bin/env python3

"""Foobar.py: Description of what foobar does.
__author__ = "Fu Linke"
__pkuid__  = "1800011782
__email__  = "1800011782@pku.edu.cn
"""

#定义一个铺砖函数，a,b分别为地面的长和宽，m，n分别为砖的长和宽
#由于m=n且能铺满时，铺法显然只有一种，本函数不予考虑，定义m！=n
#method代表铺法，alternative是代表地砖坐标的中间体
#ans是储存所有铺法的列表，gd是墙面/地板
def ocp(a, b, m, n, gd, method, ans, alternative):
	if a*b%(m*n)!=0:							  
		print ("no way, bro")
	else:
		count = 0
		h = 0
		for w in range(a*b):
			if gd[w] == 0 and h == 0:
				startrow = w//a + 1
				startcol = w%a + 1 #找到第一个未被铺砖的位置，确定其坐标
				h = 1
				#判断起始到横着铺的区域在没有超出地面的情况下是否全部空白
				if (startcol + m) <= (a + 1) and (startrow + n)<=(b + 1):
					for i in range(startrow, startrow + n) :
						for j in range(startcol,startcol + m):
							if gd[(i-1)*a + j - 1] == 0:
	#此处以及以下的所有‘(i-1)*a + j - 1’均表示第i行，第j列所对应的列表中的一维坐标
								count +=1
				alternative = []
				if count == m*n:#如果全部空白，就可以横着铺
					for i in range(startrow, startrow + n):
						for j in range(startcol,startcol + m):
							gd[(i-1)*a + j - 1] = 1
							#改变砖的状态为1，表示已经铺上
							alternative.append((i-1)*a + j - 1)
					method.append(alternative)#将一块砖的坐标加入method
					if 0 not in gd:
						ans.append(method.copy())
					else:
						ocp(a, b, m, n, gd, method, ans, alternative)
					#拆转
					for i in range(startrow, startrow + n):
						for j in range(startcol,startcol + m):
							gd[(i-1)*a + j - 1] = 0
					del method[-1]#删除砖的坐标
						
				count = 0 #现在开始竖着铺，一切基本同上
				alternative = []
				if startcol + n <= a+1 and  startrow + m <= b+1:
					for i in range(startrow, startrow + m):
						for j in range(startcol,startcol + n):
							if gd[(i-1)*a + j - 1] == 0:
								count+=1
				if count == m*n:
					for i in range(startrow, startrow + m):
						for j in range(startcol,startcol + n):
							gd[(i-1)*a + j - 1] = 1
							alternative.append((i-1)*a + j - 1)
					method.append(alternative)
					if 0 not in gd:
						ans.append(method.copy())					
					else:
						ocp(a, b, m, n, gd, method, ans, alternative)
					for i in range(startrow, startrow + m):
						for j in range(startcol,startcol + n):
							gd[(i-1)*a + j - 1] = 0
					del method[-1]
		return ans

#定义可视化的函数
def draw(a,b,m,n,method):
	import turtle
	p = turtle.Pen()
	p.speed(0)
	p.pencolor('blue')	#画墙面
	p.pensize(0.5)
	p.penup()
	p.goto(-15*a, -15*b)
	p.pendown()
	for i in range(b): #画横线
		for j in range(a):#标坐标
			p.forward(10)
			p.write(i*a + j)
			p.forward(20)
		p.penup()
		p.goto(-15*a, -15*b + 30*(i+1))
		p.pendown()
	p.penup()#此处是画出不用标坐标的那一条横线
	p.goto(-15*a, -15*b+30*(b))
	p.pendown()
	p.forward(30*a)
	p.left(90)
	p.penup()
	for i in range(a+1):#画竖线
		p.goto(-15*a + 30*i, -15*b)
		p.pendown()
		p.forward(30*b)
		p.penup()
	p.pencolor('black')#画地砖
	p.pensize(3)
	for alternative in method:
		if alternative[-1] - alternative[0] == m-1  + (n-1)*a:  	#判断为横着铺的砖
			p.goto(-15*a + 30*(alternative[0]%a), -15*b + 30*(alternative[0]//a))
			p.pendown()
			p.forward(30*n)
			p.right(90)
			p.forward(30*m)
			p.right(90)
			p.forward(30*n)
			p.right(90)
			p.forward(30*m)
			p.right(90)
			p.penup()
		else:#竖着来
			p.goto(-15*a + 30*(alternative[0]%a), -15*b + 30*(alternative[0]//a))
			p.pendown()
			p.forward(30*m)
			p.right(90)
			p.forward(30*n)
			p.right(90)
			p.forward(30*m)
			p.right(90)
			p.forward(30*n)
			p.right(90)
			p.penup()
	p.hideturtle()
	turtle.done()


def main():		  
	print('显然地砖长宽相等时只有一种铺法，请输入长宽不等的地砖')
	a = int(input('地板的长度'))
	b = int(input('地板的宽度'))
	m = int(input('地砖的长度'))
	n = int(input('地砖的宽度'))
	gd = [0]*a*b  #构建地面
	ans = []
	ocp(a, b, m, n, gd, [], ans, [])	
	for i in range(len(ans)):
		print('第%d种'%(i+1), ans[i])
		print('\n')
	print('共有%d种铺法'%len(ans))
	choice = int(input('您选择的方案号：'))
	draw(a, b, m, n, ans[choice-1])


if __name__ == '__main__':
	main()