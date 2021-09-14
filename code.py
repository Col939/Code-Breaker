import random

code = ""

def mainGame():
  global code
  if len(code) == 3:
    print("Number 1 times Number 3 is " + str(int(code[0]) * int(code[2])))
    print("The difference between Number 2 and Number 1 * Number 3 is " + str((int(code[0]) * int(code[2])) - int(code[1]))

def startGame():
    
  global code
  
  for x in range(random.randint(3, 6)):
    code += str(random.randint(0,9))
  print(code)
  
  mainGame()
startGame()

