#1
a=input("enter grade of student :")
match a:
  case "a" | "A":
    print("student's grade is A")

  case "b" | "B":
   print("student's grade is B")

#2
color=input("Enter the color of light :")
color= color.lower()
match color:
  case "red":
    print("STOP !")

  case "yellow":
    print("READY TO GO!")
    
  case "green":
    print("GO!")
  case _:
    print("enter valid color name.")

#3
a,b= int(input("enter number 1 : ")),int(input("enter number 2 : "))
opr=input("entr operator +,-,*,/  : ")

match opr:
  case "+":
    print(a,"+",b,"=",a+b)
  case "-":
    print(a,"-",b,"=",a-b)
  case "*":
    print(a,"*",b,"=",a*b)
  case "/":
    print(a,"/",b,"=",a/b)
  case _:
    print("enter valid operator.")

#4
day=input("enter day of week: ")

match day:
  case "monday" |"tuesday" |"wednesday" |"thursday" | "friday":
    print("it is a weekday")
  case "saturday" | "sunday":
    print("it is weekend. ")
  case _:
    print("enter valid day.")

#5
shape=input("name of shape to calculate area :")
match shape:
  case "circle":
    rad=int(input("enter radius of circle: "))
    print("area of circle is:", 3.14*(rad**2) )

  case "square":
    side=int(input("enter side of square: "))
    print("area of square is :", side*side)

  case "rectangle":
    height,width=input("enter height of rectangle"),          input("enter width of recatngle :")
    print("area of rectangle :", int(width)*int(height))

  case _:
    print("enter valid shape name")
    
  