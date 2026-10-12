guessLimit = 3
guessCount = 0
secretNum = 10

while guessCount < guessLimit:
  guessNum = int(input("Your guess: "))
  guessCount+=1
  if (guessNum == secretNum):
    print("You won!")
    break
else:
  print("You lose")



