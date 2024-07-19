
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
         turn_right()
         move()
    elif front_is_clear():
        move()
    else:
         turn_left()

#This code does't work here. This is the solution for the reeborg's final test at https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds/menus/reeborg_intro_en.json&name=Maze&url=worlds/tutorial_en/maze1.json.


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
