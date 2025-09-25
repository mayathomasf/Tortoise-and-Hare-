# Tortoise and Hare Project
# Maya Thomas-Fubler

import random
import time

# Initialize introduction function
def intro():
# Print welcome statement & beginning sequence
# Use the time module to slow down the output of the introduction print statements. This creates a smooth presentation for the beginning sequence. 

  print("Welcome to the big race!!!!!")
  time.sleep(3)

  print("Ready . . .")
  time.sleep(2)

  print("Set . . . ")
  time.sleep(2)

  print("BANG!!!!!!")
  time.sleep(1)

  print("AND THEY'RE OFF!!!!")
  time.sleep(1)

  print("")

# Call introduction function
intro()

# Initalize the game function
def game():
# Initialize position at 0 for each animal
  tort_pos = 0
  hare_pos = 0

# Initialize the movement types of the animals, they are currently set to 0 as they have not moved yet.
  tort_move = 0
  hare_move = 0

# Initialize time as 1
  clock = 1

# Initialize while loop
  while True:

#TIME PERCENTAGES:
# The percentage of time an animal uses to move dictates the type of move it has done. To get the percentage of time, we use the random module to generate a random percentage of time for each animal. 
# The random number generator will generate a number between 1-10 (10-100%)
# Initialize variable for 2 random numbers between 1 & 10.
    tort_percent = random.randint(1,10)
    hare_percent = random.randint(1,10)


#MOVE TYPES: 
# Print out assigned move type message after move type is established
# Use If statement to test for all numbers 1-10 for move type

# For Tortoise: 10-50% of the time is the move “Fast plod”; 60-70% is a “Slip” and 80-100% is a “Slow plod" 
    if tort_percent == 1 or tort_percent == 2 or tort_percent == 3 or tort_percent == 4 or tort_percent == 5:
      tort_move = 1
      print("The tortoise is plodding fast.")
    elif tort_percent == 6 or tort_percent == 7:
      tort_move = 2
      print("The tortoise has slipped.")
    elif tort_percent == 8 or tort_percent == 9 or tort_percent == 10:
      tort_move = 3
      print("The tortoise is plodding slowly.")

# For Hare: 10-20% of the time is the move “Sleep”; 30-40% is a “Big hop”; 50% is a “Big slip”; 60-80% is a “Small hop” and 90-100% is a “Small slip” 
    if hare_percent == 1 or hare_percent == 2:
      hare_move = 1
      print("The hare is sleeping.")
    elif hare_percent == 3 or hare_percent == 4:
      hare_move = 2
      print("The hare has done a big hop.")
    elif hare_percent == 5:
      hare_move = 3
      print("The hare had a big slip.")
    elif hare_percent == 6 or hare_percent == 7 or hare_percent == 8:
      hare_move = 4
      print("The hare has done a small hop.")
    elif hare_percent == 9 or hare_percent == 10:
      hare_move = 5
      print("The hare had a small slip.")

#TIME ELAPSED:
# Print out time elapsed (seconds)
    print("Time elapsed: ", clock)

# POSITIONS:
# Corresponding to move type, add to position for both animals
# Moving to the right is forwards which means that the poistion is added to
# Moving to the left is backwards, meaning that the poition is subtracted from
# If either animal slips before square 1, they move back to square 1 
# Add the validation that the position of the animal is at least 1 after establishing the position of the animal.

# For Tortoise: Fast plod (move 1) = 3 squares to the right; Slip (move 2) = 6 to the left; Slow plod (move 3) = 1 to the right
    if tort_move == 1:
      tort_pos += 3
    elif tort_move == 2: 
      tort_pos = tort_pos - 6
    elif tort_move == 3:
      tort_pos += 1

#Ensure that if the position of the tortoise is under 1 (slip before 1/past first square), that it is set to 1
    if tort_pos < 1:
      tort_pos = 1


# For Hare: Sleep (move 1) = 0 squares moved; Big hop (move 2) = 9 squares to the right; Big slip (move 3) = 12 squares to the left; Small hop (move 4) = 1 squares to the right; Small slip (move 5) = 2 squares to the left
    if hare_move == 1:
      hare_pos = hare_pos + 0 
    elif hare_move == 2:
      hare_pos += 9
    elif hare_move == 3:
      hare_pos = hare_pos - 12
    elif hare_move == 4:
      hare_pos += 1
    elif hare_move == 5:
      hare_pos = hare_pos - 2

# Ensure that if the position of the hare is under 1 (slip before 1/past first square), that it is set to 1
    if hare_pos < 1:
      hare_pos = 1

#There are only 70 squares so ideally the position of either animal should not reach over 70.
#Use if statements to ensure that if the position of either animal has reached over 70, the position should print as 70. 
    if tort_pos > 70:
      tort_pos = 70

    if hare_pos > 70:
      hare_pos = 70

# Print updated position for both animals
    print("The tortoise is in position: ", tort_pos)
    print("The hare is in position: ", hare_pos)
    print("")

# When both animals are on the same square, the tortoise bites the hare
# If position numbers of both animals equal each other - print bite statement
    if hare_pos == tort_pos:
      print("OUCH !!!, The tortoise bit the hare!!")
      print("")

#RESULTS:
#Once either animal reaches the 70th square, it has won. A tie is also possible.

# Test for 70 & same square:
# Use if statement to test if either of the positions are 70 or passed 70.
# If - one is >= 70 - print win message for specific animal and break while loop
# Elif - they are both >= 70 - print tie message and break while loop
# Else - Continue loop and Add to time variable (+=)
    if hare_pos >= 70 and tort_pos >= 70: 
      print("It's a tie.")
      break

    elif hare_pos >= 70:
      print("Hare wins. Yuch.")
      break

    elif tort_pos >= 70:
      print("TORTOISE WINS!!! YAY !!!")
      break

    else:
      clock += 1
      continue

#Call game function
game()

