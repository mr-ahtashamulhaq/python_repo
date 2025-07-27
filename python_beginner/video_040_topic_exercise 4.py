# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


print("---Welcome to the Secret Code Language Translator---\n\n")
print("press 'C' for converting message into secret code\n")
print("press 'D' for decoding secret code\n")
choice = input("Enter your choice: ")
if (choice.upper() == 'C'):
  print("You have selected Coding")
  message = input("Enter the message you want to code: ")
  if (len(message)>=3):
    message1=message+message[0]
    message2=message1.replace(message1[0],"Akm",1)
    messagefin = message2 + "fyl"
    print(f"\nyour secret code is : {messagefin}")

  else:
    print(f"\nyour secret code is : {message[::-1]}")
    
elif(choice.upper() == 'D'):
  code = input("Enter the code you want to decode: ")
  if(len(code)<3):
    print(f"\nyour message is : {code[::-1]} ")
  else:
    code1 = code[3:-4]
    codefin = code[-4] + code1
    print(f"\nYou message is : {codefin}")
else:
  print("\nENTER VALID OPTION !")
  
    
  
  

