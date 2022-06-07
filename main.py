import random
 
choices = ["r","p","s"]

computer = random.choice(choices)
player = None

player = input("R(rock), P(paper), or S(scissors)?: ").lower()

while True:
  if player == computer:
   print("It's a Tie!")
   computer = random.choice(choices)
   player = input("R(rock), P(paper), or S(scissors)?: ").lower()
  if player != computer:
    break


while player not in choices:
  print("Not an option: pick either R, P or S")
  player = input("R(rock), P(paper), or S(scissors)?: ").lower()
  
  
  
if player == "r":
  if computer == "p":
    print(f"computer:paper ")
    print(f"player:rock ")
    print("you lose!")
  if computer == "s":
    print(f"computer:scissors ")
    print(f"player:rock ")
    print("you win!")
elif player == "s":
  if computer == "p":
    print(f"computer:paper ")
    print(f"player:scissors ")
    print("you win!")
  if computer == "r":
    print(f"computer:rock ")
    print(f"player:scissors ")
    print("you lose!")
elif player == "p":
  if computer == "r":
    print(f"computer:paper ")
    print(f"player:rock ")
    print("you win!")
  if computer == "s":
    print("computer:scissors ")
    print("player:paper ")
    print("you win!")    
         
    
