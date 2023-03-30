"""
[Project 3A, Project 3B, Project 3C]

Programmer: Cox, Brandon

Course: CSC1019-FBN
"""

"""
Project 3A: Develop a program that converts feet to inches. Your program should ask the user for number of feet and then outputs the converted number of inches. In your program, make a function named "feet_to_inches" that accepts number of feet as an argument and returns the number of inches in that many feet (ex: 2 feet should return 24 inches). 
"""

print("--------- Project 3A ---------")
print("This program will convert feet into inches")
print("------------------------------")

while True:
  feet = input("\nInput distance in feet or press x to stop: ")
  x = "x"
  if feet.isnumeric():
    feet = int(feet)
    break
    
  elif feet == x:
    feet = feet.replace(x, "")
    break
    
  else:
    print("\nYou didn't enter a number")
    print("\n-------------------------------------")

def feet_to_inches(feet):
  while True:
    if feet:
      inches = feet*12
      print("Inches:", inches)
      break
    else:
      break

feet_to_inches(feet)

"""
Project 3B: Develop a number guessing game. The program should generate a random number and then ask the user to guess the number. Each time the user enters a guess, the program should indicate whether it was too high or too low. The game is over when the user correctly guesses the number. When the game ends, the program should display the number of guesses the user made. Break your program into functions where appropriate.
"""

print("\n--------- Project 3B ---------")
print("This program is a random number guessing game")
print("--------------------------------")

def guessProgram():
  count = 0
  
  while True:
    import random
    number = random.randint(0,9)

    inputNumber = -1
    count += 1
    
    while True:
      loopInputNumber = input("\nPlease Guess a number between 0 and 9 or enter x to stop: ")
      if loopInputNumber.isnumeric():
        loopInputNumber = int(loopInputNumber)
        inputNumber += 1
        inputNumber += loopInputNumber
        break
      elif loopInputNumber == "x":
        count = count - 1
        print(f"\nYou tried {count} times!")
        break
      else:
        print("\nYou didn't enter a number")
        print("\n-------------------------------------")

    if inputNumber == -1:
      break
    
    if inputNumber > number:
      print("\nYour number is too large, please try again")
      print("The number was", number)
      print("\n------------------------------")
      
    if inputNumber < number:
      print("\nYour number is too small, please try again")
      print("The number was", number)
      print("\n------------------------------")
      
    elif inputNumber == number:
      print("\nCongratulations you chose the right number!")
      print(f"You tried {count} times!")
      break

guessProgram()

"""
Project 3C - Develop a program that simulates a slot machine. When the program runs, it should do the following:
Ask the user to enter the amount of money they want to insert
Instead of displaying images, the program will randomly select a word from the following list: Cherry, Orange, Plums, Bell, Melon, Bar. The program will select and display a word from this list three times. 
If none of the randomly selected words match, the program will inform the user that they've won $0. If two words match, the program will inform the user that he or she has won two time the amount entered. If three words match, the program will inform the user that they've won three times the amount entered.
The program will ask whether the user wants to play again. If so, the steps are repeated. If not, the program displays the total amount of money entered into the slot machine and the total amount won.esses the user made. Break your program into functions where appropriate.
"""

print("\n--------- Project 3C ---------")
print("This program is a gambling slot machine game")
print("------------------------------")

def gamble():
  moneyArray = []
  
  while True:
    while True:
      askForMoney = input("\nHow much money would you like to play with? Amount: ")
      if askForMoney.isnumeric():
        askForMoney = int(askForMoney)
        break
      else:
        print("\nYou didn't enter a number")
        print("\n-------------------------------------")
        
    money = 0
  
    print("\n-------------------------------------")
    
    print("\nYour Choices Are: [Cherry, Plums, Bell, Melon, Bar]")
    
    while True:
      askForInput = input("\nEnter one of the following options to gamble with: ")
      askForInput = askForInput.upper()

      if askForInput == "CHERRY" or askForInput == "PLUMS" or askForInput == "BELL" or askForInput == "MELON" or askForInput == "BAR":
        break
      
      if askForInput != "CHERRY" or askForInput != "PLUMS" or askForInput != "BELL" or askForInput != "MELON" or askForInput != "BAR":
        print("\nYou didn't enter one of the options")
        print("\n-------------------------------------")
      
    array = ["Cherry", "Plums", "Bell", "Melon", "Bar"]
    upperArray = [x.upper() for x in array]
  
    slotOptions = []

    import random
    option1 = random.choice(upperArray)
    option2 = random.choice(upperArray)
    option3 = random.choice(upperArray)
    slotOptions.append(option1)
    slotOptions.append(option2)
    slotOptions.append(option3)

    print("\n-------------------------------------")
    
    if askForInput == slotOptions[0] and askForInput == slotOptions[1] and askForInput == slotOptions[2]:
      money += askForMoney*3
      moneyArray.append(money)
      print(f"You earned three times your bet: ${money}")
      print(f"Your slot choices were: [{option1}, {option2}, {option3}]")
      
    elif askForInput == slotOptions[0] and askForInput == slotOptions[1] or askForInput == slotOptions[0] and askForInput == slotOptions[2] or askForInput == slotOptions[1] and askForInput == slotOptions[2]:
      money += askForMoney*2
      moneyArray.append(money)
      print(f"\nYou earned two times your bet: ${money}")
      print(f"Your slot choices were: [{option1}, {option2}, {option3}]")
      
    elif askForInput == slotOptions[0] or askForInput == slotOptions[1] or askForInput == slotOptions[2]:
      money += askForMoney
      moneyArray.append(money)
      print(f"\nYou earned back your bet: ${money}")
      print(f"Your slot choices were: [{option1}, {option2}, {option3}]")
      
    else:
      print("\nYou lost your bet: $0")
      print(f"Your slot choices were: [{option1}, {option2}, {option3}]")
    
    again = input("\nDo you want to play again?(Yes/No): ")
    again = again.upper()

    if again == "YES":
      print("\n-------------------------------------")
      continue

    if again == "NO":
      print("\n-------------------------------------")
      numsum = sum(moneyArray)
      print(f"\nYou earned ${numsum}")
      break
    
    if again != "YES" or again != "NO":
      while True:
        if again != "YES" or again != "NO":
          print("\nYou didn't enter yes or no")
          print("\n-------------------------------------")
          again = input("\nDo you want to play again?(Yes/No): ")
          again = again.upper()
          if again == "YES":
            break
          if again == "NO":
            break
          continue
        break
      
gamble()

print("\nHappy Coding!")