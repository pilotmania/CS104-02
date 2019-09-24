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
        print ("You win! You guess the right number!")
        gameOver = True
    if guess != theComputerNumber:
        print ("incorrect, keep guessing")
        numberOfGuesses = numberOfGuesses +1
        print ("Number of guesses:{}.".format(numberOfGuesses))
        gameOver = False
    if numberOfGuesses == 20:
        print ("Game Over! You ran out of guesses!")
        gameOver = True
    if guess < lowGuessRange:
        print ("Your guess is too low!")
    if guess > highGuessRange:
        print ("Your guess is too high!")
