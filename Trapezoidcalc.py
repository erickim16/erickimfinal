def rollDice():
  print(randint(1,6))

def askRoll(ans):
  yes = "yes"
no = "no"
if yes in ans:
  rollDice()
return(True)
 elif no in ans:
  print("\nOkay, until next time!")
return(False);
 else: 
   print ("\nYour response was incorrect")
return (True)
   print("Dice rolling simulator!\n")
rollDice()

anotherTime = "True"

while anotherTime:
    print ("Would you like to roll again?")
ans = input("> ")
anotherTime = askRoll(ans)