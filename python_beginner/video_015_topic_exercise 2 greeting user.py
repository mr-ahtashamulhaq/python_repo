#Exercise 2:  Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.


import time
hour=int(time.strftime("%H"))
name=input("Enter your name: ")
name=name.title()

if(hour>=0 and hour<12):
  print("GOOD MORNING!",name,"have a nice day".title())
elif(hour>=12 and hour<17):
  print("GOOD AFTERNOON!",name,"hope your day is going well".title())
elif(hour>=17 and hour<22):
  print("GOOD EVENING!",name,"hope your day went very well".title())
else:
  print("GOOD NIGHT!",name,"sweet dreams".title())
  
