import random
theComputerNumber =(random.randint (1,1000000))
print (theComputerNumber)
numberOfGuesses = 0
lowGuessRange = 1
highGuessRange = 1000000
gameOver = False

while gameOver != True:
    guess = int(input ("Enter a guess: "))
    if guess == theComputerNumber:
        print ("You win! You guessed the right number!")
        gameOver = True
    if guess < lowGuessRange:
        print ("Your guess is too low!")
    if guess > highGuessRange:
        print ("Your guess is too high!")
    if guess != theComputerNumber:
        print ("Incorrect, keep guessing!")
        numberOfGuesses = numberOfGuesses +1
        print ("Number of guesses:{}.".format(numberOfGuesses))
        gameOver = False
    if guess < theComputerNumber:
        highGuessRange == guess
        print ("The guess is lower than the number!")
    if guess > theComputerNumber:
        lowGuessRange == guess
        print ("The guess is higher than the number!")
    if numberOfGuesses == 20:
        print ("Game Over! You ran out of guesses!")
        gameOver = True
    
