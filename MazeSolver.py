from os import system
import time
import csv

# declare variables
maze = []
m = []
start = 0,0
end = 0,0
mode = 0
length = 0

# clear screen
def clear():
    _=system('cls')

# create a list of zeros with size n
def zeroListMaker(n):
    return ['0'] * n

# check for walls and move in possibe paths
def stepMove():
    global length
    global mode 
    # go through the maze
    for i in range(len(m)):
        for j in range(len(m[i])):
            # check the current position in maze
            if m[i][j] == length:
                # travel in forward direction (go through unvisited nodes)
                if mode == 0:
                    if i>0 and m[i-1][j] == 0 and maze[i-1][j] == 0:                #  up
                        m[i-1][j] = length + 1 
                    elif j>0 and m[i][j-1] == 0 and maze[i][j-1] == 0:              # left
                        m[i][j-1] = length + 1
                    elif i<len(m)-1 and m[i+1][j] == 0 and maze[i+1][j] == 0:       # down
                        m[i+1][j] = length + 1
                    elif j<len(m[i])-1 and m[i][j+1] == 0 and maze[i][j+1] == 0:    # right
                        m[i][j+1] = length + 1
                    else:
                        # if it is a dead end
                        mode = 1
                        m[i][j] = -1
                        length-=2
                        return

                # travel in reverse direction (go through visited nodes)
                else:
                    length-=1
                    if i>0 and m[i-1][j] == 0 and maze[i-1][j] == 0:                # up
                        mode = 0
                    elif j>0 and m[i][j-1] == 0 and maze[i][j-1] == 0:              # left
                        mode = 0
                    elif i<len(m)-1 and m[i+1][j] == 0 and maze[i+1][j] == 0:       # down
                        mode = 0
                    elif j<len(m[i])-1 and m[i][j+1] == 0 and maze[i][j+1] == 0:    # right
                        mode = 0
                    else:
                        # going through a visited node
                        m[i][j] = -1
                        length-=1
                    return

# set the current position of the robot
def roboMove(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if max(map(max,m)) == m[i][j]  and max(map(max,m)) != 0:
                sol[i][j] = 'R'
            elif start == (i,j):
                sol[i][j] = 'S'
            elif end == (i,j):
                sol[i][j] = 'D'
            elif m[i][j] == 0:
                sol[i][j] = 0
            else:
                sol[i][j] = '.'
        

# set the final path of the robot
def finalPath(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]>0:
                sol[i][j] = '+'
            else:
                sol[i][j] = '0'
            
# print a maze (list)
def printMaze(m):
    for i in range(1,len(m)-1):
        for j in range(1,len(m[i])-1):
            print( str(m[i][j]).ljust(2),end=' ')
        print()


choice = input("Enter the name of maze file : ")

with open(choice + '.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # add left and right wall to te maze
        row.insert(0, '0') 
        row.append('0')   
        maze.append(row)

# add a top and a bottom wall to the maze 
maze.append(zeroListMaker(len(maze[0])))
maze.insert(0,zeroListMaker(len(maze[0])))

# create a list as same size as maze
sol = [[0]*len(maze[0]) for _ in range(len(maze))] 

# create all zeroes list
for i in range(len(maze)):
    m.append([])
    for j in range(len(maze[i])):
        m[-1].append(0)

# change list to integer and taking the start and end point  
i=0
for row in maze:
    j=0
    for cell in row:
        if cell == 'S':
            start = i,j
            maze[i][j] = 0
            m[i][j] = 1
        elif cell == 'D':
            end = i,j
            maze[i][j] = 0
        elif cell == '0':
            maze[i][j] = 1
        else:
            maze[i][j] = 0
        j+=1
    i+=1

# clear screen
clear()
flag = 0

# move the robot until destination
while m[end[0]][end[1]] == 0:
    length += 1
    stepMove()
    roboMove(m)
    flag = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            # check the current position in maze
            if (m[i][j] != 0 and m[i][j] != -1):
                flag = 1
    if(flag==1):
        printMaze(sol)
    else:
        print('No solution in the maze!!! ')
        break
    time.sleep(1)
    clear()
  

# displaying final path
if flag == 1:
    print("Final path: ")
    finalPath(m)
    printMaze(sol)

input("\n\nPress any key to continue...")