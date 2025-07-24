#  Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.

i=0
qustion=0
option=0
answer=0
total=0

question=["Which is the largest planet in our solar system?","What is the currency of Japan?","Who painted the Mona Lisa?","What is the national animal of Pakistan?","Which gas do plants absorb from the atmosphere?","In which year did pakistan gain independence?","What is the chemical symbol for water?","Who is the author of 'Harry Potter' series?","Which country is known as the Land of the Rising Sun?","Which planet is known as the Red Planet?"]

option=["A. Earth  B. Jupiter  C. Saturn  D. Neptune","A. Yen  B. Yuan  C. Won  D. Dollar","A. Pablo Picasso  B. Vincent van Gogh  C. Leonardo da Vinci  D. Michelangelo","A. Lion  B. Tiger  C. Elephant  D. Markhor","A. Oxygen  B. Nitrogen  C. Carbon Dioxide  D. Hydrogen","A. 1945  B. 1947  C. 1950  D. 1952","A. H2  B. O2  C. CO2  D. H2O","A. J. R. R. Tolkien  B. C. S. Lewis  C. J. K. Rowling  D. Stephen King","A. China  B. South Korea  C. Japan  D. Thailand","A. Earth  B. Jupiter  C. Mars  D. Venus"]

answer=["B","A","C","D","C","B","D","C","C","C"]



print("=== WELCOME TO KON BANEGA CROREPATI ===")
print("\n\n* Game is going to start you will got 10 questions each worth 1Lac.")
print("* Choose correct option A/B/C/D\n")

while(i<10):
  print("\n\nQuestion",i+1)
  print(question[i])
  print(option[i])
  user_ans= input("\nEnter your answer : ")
  if(user_ans.upper()==answer[i]):
    total+=100000
    print("\nAnswers is correct! you won 1 lac")
    print("currently your total amount is:",total,"Rs")
  else:
    print("\nIncorrect answer!")
    print("currently your total amount is:",total,"Rs")
  
  i+=1

print("\n\nGAME ENDED!")
print("You won",total,"Rs.")
print("\nThankyou for playing this game")
  
