# Question 1
import random

num = random.randint(1,50)
name = str(input("Enter your name bro : "))
guess = int (input("Guess the number... : "))

while guess != num :

    if guess > num :
        print("Bro the number you guessed is too high")

    elif guess < num :
        print("Brooo its too low")

    guess= int(input("try again ..."))

print(f"{name} you won! My number is", num , "and your number was", guess)


# Question 2
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']
         
word = random.choice(words)
rand_list = list(word)
random.shuffle(rand_list)
scramble = ''.join(rand_list)

print(f"guess the word {name}",scramble)
guess1 = input("enter your guess ")

while guess1 != word:
     if guess1 == word:
         print("Correct the answer",guess)
     else :
        print("wrong")
     guess1= input("try again...")
    
print("finally you won")
