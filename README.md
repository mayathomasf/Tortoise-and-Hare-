# Tortoise-and-Hare-

This code recreates the race of the tortoise and the hare. Random number generation was used to develop a simulation of this event.

The contenders begin the race at square 1 of 70 squares. Each square represents a position along the race course. The finish line is at square 70. The first contender to reach  or pass square 70 is rewarded with a pail of fresh carrots and lettuce. The course weaves its way up the side of a slippery mountain, so occasionally the contenders lose ground.


A clock ticks once per second. With each tick of the clock, the application adjusts the position of the animals according to the rules in the table below. Use variables to keep track of the positions of the animals (i.e. position numbers are 1-70). Start each animal at position 1 (the "starting gate"). If an animal slips left before square 1, move it back to square 1. 

![image](https://github.com/user-attachments/assets/2a9f05ba-7804-483a-8110-b32c4a05a81c)
 

Occasionally, the contenders will land on the same square. In this case, the tortoise bites the hare, and the application displays “OUCH!!!” at that position.


After each line displayed, a test is done for whether either animal has reached or passed square 70. If so, the winner is displayed and the simulation is terminated. If both animals win on the same tick of the clock, it is declared that the race is a tie.
