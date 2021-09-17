import random

code = ""

def mainGame():
  global code
  if len(code) == 3:
    print("3 Numbers \n")
    print("Number 1 times Number 3 is " + str(int(code[0]) * int(code[2])))
    print("The difference between Number 1 * Number 3 and Number 2 is " + str( ( int(code[0]) * int(code[2]) ) - int(code[1]) ) )
    print("Number 3 plus Number 2 is " + str(int(code[2]) + int(code[1])) )
    
  if len(code) == 4:
    print("4 Numbers \n")
    print("Number 1 plus Number 2 is " + str( int(code[0]) + int(code[1]) ) )
    print("Number 3 minus number 2 is " + str( int(code[2]) - int(code[1]) ) )
    print("Number 4 times Number 3 is " + str( int(code[3]) * int(code[2]) ) )
    print("Number 1 times Number 2 is " + str( int(code[0]) * int(code[1]) ) )
    print("Number 3 times Number 1 is " + str( int(code[2]) * int(code[0]) ) )
  
  i = input("Code: ")
  
  if(int(i) == int(code)):
    print("You got it!")
  print(code)
  
def startGame():
    
  global code
  
  for x in range(random.randint(3, 6)):
    code += str(random.randint(0,9))

  
  mainGame()
startGame()
