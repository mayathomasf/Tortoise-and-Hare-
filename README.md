# Tortoise-and-Hare-

Instructions: 

In this problem, you'll re-create the classic race of the tortoise and the hare. You'll use random-number generation to develop a simulation of this memorable event.

 

Our contenders begin the race at square 1 of 70 squares. Each square represents a position along the race course. The finish line is at square 70. The first contender to reach  or pass square 70 is rewarded with a pail of fresh carrots and lettuce. The course weaves its way up the side of a slippery mountain, so occasionally the contenders lose ground.

 

A clock ticks once per second. With each tick of the clock, your application should adjust the position of the animals according to the rules in the table below. Use variables to keep track of the positions of the animals (i.e. position numbers are 1-70). Start each animal at position 1 (the "starting gate"). If an animal slips left before square 1, move it back to square 1. 

![image](https://github.com/user-attachments/assets/2a9f05ba-7804-483a-8110-b32c4a05a81c)


Create two functions that generate the percentages in the table for the tortoise and the hare, respectively, by producing a random integer i in the range 1 <= i <= 10. In the function for the tortoise, perform a “fast plod” when 1 <= i <= 5, a “slip” when 6 <= i <= 7 or a “slow plod” when 8 <= i <= 10. Use a similar technique in the function for the hare.

 

Begin the race by displaying:

 

BANG !!!!!

AND THEY’RE OFF !!!!!!

 

Occasionally, the contenders will land on the same square. In this case, the tortoise bites the hare, and your application should display “OUCH!!!” at that position.

 

After each line displayed, test for whether either animal has reached or passed square 70. If so, display the winner and terminate the simulation. If the tortoise wins, display TORTOISE WINS!!! YAY!!! If the hare wins, display Hare wins. Yuch. If both animals win on the same tick of the clock, you may want to favor the tortoise (the “underdog”), or your may want to display “It’s a tie”.
