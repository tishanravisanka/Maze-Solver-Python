# Maze-Solver-Python
Algorithm for a robot that moving through a maze and find the destination while avoiding dead ends and loops

Maze games are very popular among the young children, where the player
should find a path which connects the source and destination while avoiding
dead ends and loops

In this, the maze is stored to csv file, where the bricks and paths are
represented by 0 and 1, respectively. The starting point and the destination is
marked with ‘S’ and ‘D’, respectively. 

Assume a small robot is moving from Starting point to the Destination and it can  view four adjacent squares from its position as shown below. The robot can
move either left, right, top, or bottom directions and a one square at a time.

This is a programme to move the robot from Starting point to Destination.
The motion of the robot  will be printed in each step to the screen and keep one second delay
between each step. 
  In moving;;
    S - starting point
    D - destination
    R - robot
    0 - bricks
    . - road
Once the robot reach the destination, the correct path will print with ‘+’ sign in the
map
