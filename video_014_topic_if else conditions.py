#check number is even or odd
num=int(input("enter the number"))
if(num%2==0):
  print("number is even.")
else:
  print("number is odd")

#Calculator
num1=int(input("enter number 1 : "))
num2=int(input("enter number 2 : "))
opr=input("enter the operation +,-,*,/ : ")

if(opr=="+"):
  print(num1,"+",num2,"=",num1+num2)
elif(opr=="-"):
  print(num1,"-",num2,"=",num1-num2)
elif(opr=="*"):
  print(num1,"*",num2,"=",num1*num2)
elif(opr=="/"):
  print(num1,"/",num2,"=",num1/num2)

#student grade calculator
mark=int(input("enter student marks: "))
if(mark>=50):
  if(mark>=90 and mark<=100):
    print("Excellent!")
    print("student got A+ grade.".title())
  elif(mark>=80 and mark<90):
    print("Good job".title())
    print("student got A grade.".title())
  elif(mark>=70 and mark<80):
    print("Good job".title())
    print("student got B grade.".title())
  elif(mark>=60 and mark<70):
    print("Needs improvement".title())
    print("student got C grade.".title())
  elif(mark>=50 and mark<60):
    print("Needs improvement".title())
    print("student got D grade.".title())

elif(mark<50):
  print("student is fail".title())
else:
  print("inavlid input!".title())



  
  
  
  
  
