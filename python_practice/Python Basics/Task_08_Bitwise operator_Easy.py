"""Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
1. d = a ^ a
2. e = c ^ b
3. f = a & b
4. g = c | (a ^ a)
5. e = ~ e
Note: ^ is for xor.
Then print d e f g space seperately. Move the cursor to the next line after printing."""
a=int(input("enter a : "))
b=int(input("enter b : "))
c=int(input("enter c : "))
#code here
#Do a^a below
d= a^a
#Do c^b below
e=c^b
#Do a&b below
f=a&b
#Do c|(a^a) below
g= c| (a^b)
#Do ~e below
e= ~e
print(d, e, f, g)