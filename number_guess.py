number=8
guess=0
while guess != number:
  guess=int(input("Enter your guess number: "))
  if guess>number:
    print("You entered too high number")
  elif(guess<number):
    print("You entered too low number")
  else:
    print("You guessed it right")
