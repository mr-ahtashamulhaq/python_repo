#1
i = int(input("Enter the number: "))
print(i)
while(i<=40):
  i = int(input("Enter the number: "))
  print(i)
else:
  print("number is greater than 40")

#2
num=int(input("enter number to calculae factorial : "))
i=num
fact=1
while(i>1):
  fact*=i
  i=i-1
print ("factorial is", fact)

#3
countodd=0
counteven=0
even=0
odd=0
for i in range(10):
  num=int(input("enter integer value:"))
  if(num%2==0):
    counteven=counteven+1
    even+=num
  else:
    countodd=countodd+1
    odd+=num

print("you have entered",counteven,"even values and",countodd,"odd values")
print("sum of even values is",even,"and sum of odd values is",odd)

#4
i=1
count=0
i=int(input("enter any number : "))
while(i>0):
  count+=1
  i//=10
print ("you have entered",count,"digit number")


  

    
    


