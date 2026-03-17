import random

def check_win(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'snake' and computer == 'water') or \
         (user == 'water' and computer == 'gun') or \
         (user == 'gun' and computer == 'snake'):
        return "You win!"
    else:
        return "Computer wins!"

choices = ['snake', 'water', 'gun']
computer_choice = random.choice(choices)
user_choice = input("Enter your choice (snake, water, gun): ").lower()

result = check_win(user_choice, computer_choice)

print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")
print(result)