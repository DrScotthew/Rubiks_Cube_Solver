from typing import Self
import magiccube
import sys
import io
from magiccube.cube import CubePrintStr
import random
from magiccube.cube import Cube
from magiccube.solver.basic.basic_solver import BasicSolver
from numpy import char


with open(r"C:\Users\Scott\Downloads\myFile.txt") as file:
    userInputRead = file.read()     #open previously entered user input...
   
print(userInputRead)    #print out previously entered rubik's cube input...
    

cube = magiccube.Cube(
    3, userInputRead)   #assigns 3x3 rubiks cube using user input...
print(cube)     #prints layout of cube based on user input given from HTML page...

solver = BasicSolver(cube)
solvedcube = solver.solve()     #assign variable for solving history...

# Create the cube with a fixed state
# cube = magiccube.Cube(
#     3, "OGOBBYWROGOBYOWWGBOYBBWGYOWRWROGBROYYBGRRRBRGWWYWYGRYG")  #OGOBBYWROGOBYOWWGBOYBBWGYOWRWROGBROYYBGRRRBRGWWYWYGRYG  #YYYYYYGGGGGWRRRRRROOOGGWGGWYBBOOOOOORRRYBBYBBWWBWWBWWB
# print(cube)
# Reset to the initial position
# cube.reset()

# Scramble the cube
# cube.scramble()

# Print the move history
print("History: ", solvedcube)

# for val in solvedcube:
#     #set this as parameter for cube.rotate...repeat until finished with list
#     # CubePrintStr.print_cube
#     print([val])
#     test=char([val])
#     # cube1 = cube.rotate(test)
#     cube.rotate(solvedcube(test))  #...this literally takes forever and I'm not sure why...
#     #     #this goes in a loop continously...need to stop...
    

#     # print(cube1)     #will print out solved cube (preprogrammed...)
#     # actualcube=str(cube)
    
#     # sys.stdout=open(r"history.txt", "w") #need to convert the whole cube layout into cube notation...
#     #                                     #then save to file, read from it, compare by simple strings...
#     # sys.stdout.close
#     # move_history=open("history.txt", "r").readlines()
#     # CubePrintStr.print_cube
#     # if val!=move_history:
#     #     print(cube)
#     # else:    
#     #     break

# Print the moves to reverse the cube history
# cube.rotate(cube.reverse_history())

for val in solvedcube:
    print(val)
    print(cube)

# Print the cube
print("Solved Cube")
print(cube)