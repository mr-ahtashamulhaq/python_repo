#1
name="ahtasham"
for i in name:
	print(i)

#2
for j in range(0,41,2):
	print(j)
#3
for k in range(10,0,-1):
	print(k)
#4
num=input("enter number to print table : ")
for m in range(1,11,1):
	print(num,"*",m,"=",int(num)*int(m))

#5
num=input("enter the number to which you want to print square of all numbers : ")
for n in range(1,int(num)+1):
	print(n*n)

#extra task
for a in range(0,6):
	for b in range(0,a):
		print("*", end=" ")
	print("\n")	

for a in range(0,6):
	for b in range(0,a):
		print(b, end=" ")
	print("\n")