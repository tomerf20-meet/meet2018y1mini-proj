# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name: Tomer Ferdman
Date: 08/07/2018
"""
import turtle
import random # We'll need this later in the lab
import time
turtle.tracer(1,0) # This helps the turtle move more smoothly
SIZE_A = 1000
SIZE_B = 1000
SIZE_X=550
SIZE_Y=550
score = 0
turtle.setup(SIZE_A, SIZE_B) # Curious? It's the turtle window size.  
border = turtle.clone()
border.color('dark orange')
border.penup()
border.width(20)
border.goto(-300,-300)
border.pendown()
border.goto(-300,300)
border.goto(300,300)
border.goto(300,-300)
border.goto(-300,-300)
border.penup()
turtle.penup()
border.hideturtle()
label_game = turtle.Turtle()
label_game.ht()
label_game.penup()
label_game.color('red')
label_game.width('10')
label_game.goto(-100, 350)
label_game.pendown()
label_game.write('SNAKE GAME!!!', font = ('Arial', 30, 'normal'))
num_label = turtle.Turtle()
num_label.ht()
num_label.color('light blue')
num_label.width(10)
num_label.penup()
num_label.goto(0, -400)
num_label.write(str(score))
SQUARE_SIZE = 20
START_LENGTH = 5

# Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
# Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape('square')
snake.color('dark blue')
# Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
# Draw a snake at the start of the game with a for loop
# for loop should use range() and count up to the number of pieces
# in the snake (i.e. START_LENGTH)
for snake1 in range(START_LENGTH):
    x_pos=snake.pos()[0]# Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    # Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE 

    my_pos=(x_pos,y_pos) # Store position variables in a tuple
    snake.goto(x_pos,y_pos) # Move snake to new (x,y)
   
    # Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    # Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.
    
    stamp_t = snake.stamp()
    stamp_list.append(stamp_t)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" # Make sure you pay attention to upper and lower 
                # case
LEFT_ARROW = "Left" # Pay attention to upper and lower case
DOWN_ARROW = "Down" # Pay attention to upper and lower case
RIGHT_ARROW = "Right" # Pay attention to upper and lower case
TIME_STEP = 150 # Update snake position after this many 
currentTIME_STEP = TIME_STEP # milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
# 1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
#### WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300
def up():
    global direction # snake direction is global (same everywhere)
    if not direction == DOWN:
        direction=UP # Change direction to up
                 # Update the snake drawing <- remember me later
        print("You pressed the up key!")
def left():
    global direction
    if not direction == RIGHT:
        direction=LEFT
        print('You pressed the left key!')
def down():
    global direction
    if not direction == UP:
        direction=DOWN
        print('You pressed the down key!')
def right():
    global direction
    if not direction == LEFT:
        direction=RIGHT
        print('You pressed the right key!')
# 2. Make functions down(), left(), and right() that change direction
#### WRITE YOUR CODE HERE!!
isPause = False

tpause = turtle.clone()

def pause():
    global isPause, TIME_STEP
    
    tpause.penup()
    tpause.goto(-100,0)
    isPause = not isPause
    if isPause:
        tpause.write('PAUSE', font = ('Arial', 60, 'normal'))
    else:
        tpause.clear()
    '''
    tpause = turtle.clone()
    tpause.penup()
    tpause.goto(-100,0)
    tpause.write('PAUSE', font = ('Arial', 60, 'normal'))
    if isPause:
        TIME_STEP = 100000
    else:
        TIME_STEP = currentTIME_STEP
        move_snake()
    while isPause:
        tpause.clear()
        time.sleep(.25)
        tpause.write('PAUSE', font = ('Arial', 60, 'normal'))
        time.sleep(.25)
    tpause.clear()
    '''
        


turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(pause, "space")
turtle.listen()
food = turtle.clone()
turtle.register_shape('trash.gif')

food.shape("trash.gif") 
food_pos = [(100,100)]
food_stamps = []

for this_food_pos in food_pos:
    food.goto(this_food_pos)
    food_stamp=food.stamp()
    food_stamps.append(food_stamp)
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)-1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)+1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x, food_y)
    food_turtle_pos = (food_x, food_y)
    food_pos.append(food_turtle_pos)
    food_stamp = food.stamp()
    food_stamps.append(food_stamp)
    print(food_pos)
def move_snake():
    if not isPause:
        my_pos = snake.pos()
        x_pos = my_pos[0]
        y_pos = my_pos[1]
        
        if direction==RIGHT:
            snake.goto(x_pos + SQUARE_SIZE, y_pos)
            print("You moved right!")
            my_pos=(x_pos + SQUARE_SIZE, y_pos)
        elif direction==LEFT:
            snake.goto(x_pos - SQUARE_SIZE, y_pos)
            print("You moved left!")
            my_pos=(x_pos - SQUARE_SIZE, y_pos)
        elif direction==UP:
            snake.goto(x_pos, y_pos + SQUARE_SIZE)
            print('You moved up!')
            my_pos=(x_pos, y_pos + SQUARE_SIZE)
        elif direction==DOWN:
            snake.goto(x_pos, y_pos - SQUARE_SIZE)
            print('You moved down!')
            my_pos=(x_pos, y_pos - SQUARE_SIZE)

        new_pos = snake.pos()
        new_x_pos = new_pos[0]
        new_y_pos = new_pos[1]

        # 4. Write the conditions for UP and DOWN on your own
        ##### YOUR CODE HERE
        if new_x_pos >= RIGHT_EDGE:
            print('You hit the right edge! Game over!')
            quit()
        elif new_x_pos <= LEFT_EDGE: 
            print('You hit the left edge! Game over!')
            quit()
        elif new_y_pos >= UP_EDGE:
            print('You hit the up edge! Game oover!')
            quit()
        elif new_y_pos <= DOWN_EDGE:
            print('You hit the down edge! game over!')
            quit()
        # Stamp new element and append new stamp in list
        # Remember: The snake position changed - update my_pos()
        my_pos=snake.pos() 
        pos_list.append(my_pos)
        new_stamp = snake.stamp()
        stamp_list.append(new_stamp)
        ######## SPECIAL PLACE - Remember it for Part 5
        if snake.pos() in pos_list[:-1]:
             print('You hit yourself! Game over!')
             quit()
        global food_stamps, food_pos, score
        if snake.pos() in food_pos:
            food_ind=food_pos.index(snake.pos())
            food.clearstamp(food_stamps[food_ind])
            food_pos.pop(food_ind)
            food_stamps.pop(food_ind)
            print('You have eaten the food!')
            score = score + 100
            global TIME_STEP
            if TIME_STEP > 10:
                TIME_STEP = int(TIME_STEP*0.9)
        else:
            old_stamp = stamp_list.pop(0)
            snake.clearstamp(old_stamp)
            pos_list.pop(0)
           
            
        # pop zeroth element in pos_list to get rid of last the last 
        # piece of the tail
        score = score + 1
        num_label.clear()
        num_label.write(str(score), font = ('Arial', 40, 'normal'))
       
        if len(food_stamps) <= 1:
            make_food()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

turtle.mainloop()

