a = "!!! ahtasham!! ahtasham"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("ahtasham", "python"))
b="ahtasham ul haq"
print(b.split(" "))

c=" betty bought a bit of butter but the butter was bitter so betty bought some better butter to make the bitter butter better "
sep_bu=c.split("bu")
print("\n", sep_bu)

cap=("ahtasham ul haq")
print(cap.capitalize())
cap=("Ahtasham ul HAQ")
print(cap.capitalize())

str1=(input("enter the string : "))
cen=int(input("enter margin : "))
after_center=(str1.center(cen,"."))
print("length before center", len(str1))
print("length after center", len(after_center))
print(after_center)

print(after_center.count("."))
print(after_center.endswith("...."))
print(after_center.startswith("...."))

str2="i am ahtasham ul haq"
print(str2.find("ul"))
str2=str2.replace(" ", "")
print(str2.isalnum())
print(str2.isalpha())
str2="i am ahtasham ul haq"
print(str2.islower())
str2=str2.upper()
print(str2.isupper())

str2=str2.title()
print(str2.istitle())


#  all at once
sent=(input("Enter the sentence: "))
print("sentence in lower case: ", sent.lower())
print("sentence in upper case: ", sent.upper())
print("capitalized sentence: ", sent.capitalize())
print("sentence in title case: ", sent.title())
print("remove blank spaces: ", sent.title())
repeat=(input("enter the word want to check how many times it repeat: "))
print(repeat,"occured",sent.count(repeat),"times")
start_end=(input("enter the word to check if sentence start with : "))
print(sent.startswith(sent))
print(sent.endswith(sent))
print("sentence in reverse : ", sent[::-1])











