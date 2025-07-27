#1
isprime = True
num = int(input("enter number to check prime or not : "))
if (num < 2):
	isprime = False
else:
	i = 2
	while (i <= num // 2):
		if (num % i == 0):
			isprime = False
			break
		i = i + 1

if isprime:
	print("number is prime.")
else:
	print("number is not prime")

#2
while (True):
	i = (input("enter any value or enter \"stop\" to end loop : "))
	if (i == "Stop" or i == "STOP" or i == "stop"):
		print("loop ended")
		break
#3
name = input(
    "enter your name if there'll be an S in your name loop will break : ")

for i in name:
	if (i == 's'):
		print("\nfound s loop breaked")
		break
	else:
		print(i)
