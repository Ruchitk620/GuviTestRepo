# Question 1 : Guess the number
import random

num = random.randint(1,50) # choose the random number
name = str(input("Enter your name bro : ")) # ask the name of the gamer 
guess = int (input("Guess the number... : ")) # ask to gues the numer

while guess != num :  # the loop runs until gamer guessd the right number

    if guess > num :
        print("Bro the number you guessed is too high")

    elif guess < num :
        print("Brooo its too low")

    guess= int(input("try again ..."))

print(f"{name} you won! My number is", num , "and your number was", guess)


# Question 2: word guessing game
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium'] #list of words
         
word = random.choice(words) # choose the random word
rand_list = list(word) # the random word is segregated to list
random.shuffle(rand_list) # the segregated list is shuffle
scramble = ''.join(rand_list) # the shuffled list is joined agin (divide->shuffle->join)

print(f"guess the word {name} :",scramble)
guess1 = input("enter your guess ")

while guess1 != word: #loop runs untill gamer guess the rught word
     if guess1 == word:
         print("Correct the answer",guess)
     else :
        print("wrong")
     guess1= input("try again...")
    
print("finally you won") # finally you won 

print("------------ Result -------------") # printing the final result of game
print("Game1",num)
print("Game2",word)
