"""Given an integer n. Write a program to find the first prime number greater than n."""
n = int(input("Enter number  : "))
numtocheck = n+1

numfind = True
while(numfind):
    isprime = True
    for i in range(2,numtocheck):
        if numtocheck%i == 0:
            isprime = False
            break
    if isprime:
        print("next prime is : ", numtocheck)
        numfind= False
    else:
        numtocheck +=1