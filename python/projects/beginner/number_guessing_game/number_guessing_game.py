#Number guessing game.
#User set the number between 0 and X
#Computer generates a number between 0 and X
#User is asked to enter a number, and the computer will say either
#higher, lower or correct.

from random import randint

#Get a number from the user
userNumber = input("Enter a number: ")

#generate another number between 1 and whatever the user entered
randomNumber = randint(1,int(userNumber))

#Print the randomNumber to make it easier to cheat. (and to test that the code works)
#print(randomNumber)

#Assign the guess value to Zero so the loop will always run (because the randomly chosen number starts at 1)
guessNumber = 0

#Start a loop which will finish when the user guesses the number
while randomNumber != guessNumber:
    #Ask the user for another number, the guess
    guessNumber = int(input("Enter your guess: "))
    
    #If the guess is lower than the number, say lower
    if guessNumber<randomNumber:
        print("The secret number is higher. Guess again!")
    #If the guess is higher than the number, say higher
    if guessNumber>randomNumber:
        print("the secret number is lower. Guess again!")
    #If the guess is correct, say yay and then exit the loop.
    if guessNumber==randomNumber:
        print("Correct. Thank you for playing.")