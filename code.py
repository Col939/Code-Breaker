import random

code = ""

def mainGame():
  global code
  if len(code) == 3:
    print("Number 1 times Number 3 is " + str(int(code[0]) * int(code[2])))
    print("The difference between Number 1 * Number 3 and Number 2 is " + str( ( int(code[0]) * int(code[2]) ) - int(code[1]) ) )
    print("Number 3 plus Number 2 is " + str(int(code[2]) + int(code[1])) )
  
  i = input("Code: ")
  
  if(str(i) == str(code)):
    print("You got it!")
  print(code)
  
def startGame():
    
  global code
  
  for x in range(random.randint(3, 6)):
    code += str(random.randint(0,9))

  
  mainGame()
startGame()
