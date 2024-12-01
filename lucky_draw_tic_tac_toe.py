import turtle
import math
import random

angle = 0
rotate = False
# Set up the screen
screen = turtle.Screen()
screen.title("Lucky Draw Tic Tac Toe")
screen.setup(width=800, height=800)
game_board = [['' for _ in range(3)] for _ in range(3)]
turn=False
angle = 0
rotate = False
rotation_speed = 1  # Initial rotation speed (milliseconds)
speed = random.randint(0, 100)
generating=True
board = turtle.Turtle()
board.speed(0)
board.width(5)

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

# Function to display text using Turtle graphics
def display_text(message, x, y,size=30):
    text_turtle.setheading(0.0)
    text_turtle.clear()
    text_turtle.goto(x, y)
    text_turtle.write(message, align="center", font=("Arial", size, "bold"))

def draw_turntable():
    board.setheading(0.0)
    board.penup()
    board.goto(0, 0)
    board.right(angle)
    x = 0 - 250 * math.sin(math.radians(angle))
    y = 0 - 250 * math.cos(math.radians(angle))
    board.goto(x, y)
    board.pendown()
    board.color("yellow")
    board.begin_fill()
    board.circle(250, 180)
    board.end_fill()
    board.color("red")
    board.begin_fill()
    board.circle(250, 180)
    board.end_fill()
    board.penup()

    board.left(angle)
    board.goto(0, 250)
    board.color("blue")
    board.right(270)
    board.penup()
    board.goto(20, 265)
    board.pendown()
    board.begin_fill()
    board.circle(20, 180)
    board.left(20)
    board.forward(60)
    board.left(140)
    board.forward(60)
    board.end_fill()

def rotate_turntable():
    global angle, rotate, rotation_speed,speed
    if rotate:
        angle += speed
        if angle>360:
            angle-=360
        draw_turntable()
        if speed > 1:
            speed*=0.9
            screen.ontimer(rotate_turntable(), rotation_speed)
        else:
            rotate = False
            stop_at_random_position()

def stop_at_random_position():
    global angle,speed,turn,generating
    turn= False if angle>180 else True
    display_text("Player O turn" if turn else "Player X turn", -200, 350)
    speed=random.randint(0, 100)
    generating=False
    board.clear()
    

def draw_board():
    global generating
    generating=True
    board.setheading(0.0)
    board.heading()
    board.color("black")
    board.penup()
    board.goto(-300, -100)
    board.pendown()
    board.forward(600)
    board.penup()
    board.goto(-300, 100)
    board.pendown()
    board.forward(600)
    board.penup()
    board.goto(-100, 300)
    board.right(90)
    board.pendown()
    board.forward(600)
    board.penup()
    board.goto(100, 300)
    board.pendown()
    board.forward(600)
    board.penup()
    board.hideturtle()
    for n in range(9):
        if game_board[n%3][n//3]=='X':
            draw_X(n%3, n//3)
        elif game_board[n%3][n//3]=='O':
            draw_O(n%3, n//3)   
    generating=False

def draw_X(row, col):
    board.setheading(0.0)
    x = col * 200
    y = row * 200

    board.penup()
    board.color("yellow")
    board.goto(x-200,-y+200)
    board.pendown()
    board.setheading(-45)
    board.forward(100)
    board.backward(200)
    board.forward(100)
    board.setheading(45)
    board.forward(100)
    board.backward(200)
    board.forward(100)
    board.penup()

def draw_O(row, col):
    board.setheading(45)
    x = col * 200
    y = row * 200

    board.penup()
    board.color("red")
    board.goto(x-145,-y+145)
    board.pendown()
    board.circle(80)
    board.penup()

def check_win():
    # Check rows
    for row in game_board:
        if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
            return True
    for col in range(3):
        if all(game_board[row][col] == 'X' for row in range(3)) or all(game_board[row][col] == 'O' for row in range(3)):
            return True
    if all(game_board[i][i] == 'X' for i in range(3)) or all(game_board[i][i] == 'O' for i in range(3)):
        return True

    if all(game_board[i][2 - i] == 'X' for i in range(3)) or all(game_board[i][2 - i] == 'O' for i in range(3)):
        return True

    return False

def check_tie():
    for n in range(9):
        if game_board[n%3][n//3]=='':
            return False
    return True

def click_handler(x, y):
    global turn,game_board,angle, rotate, rotation_speed,generating
    display_text("Player O turn" if turn else "Player X turn", -200, 350)
    if generating==False:
        col = int((x + 300) // 200)
        row = int((300 - y) // 200)
        if game_board[row][col]=='' and check_win()==False:
            if turn==False:
                game_board[row][col] = 'X'
                draw_X(row, col)

            else:
                game_board[row][col] = 'O'
                draw_O(row, col)
            
        board.clear()
        
        if not check_win() and not check_tie():
            generating=True
            if not rotate:
                rotate = True
                rotate_turntable()      
            draw_board()
        if check_win():
            display_text("Player O wins!" if turn else "Player X wins!", 0, 0, 60)
            game_board = [['' for _ in range(3)] for _ in range(3)]
            board.clear()
            draw_board()
        if check_tie():
            display_text("Tie", 0, 0)
            game_board = [['' for _ in range(3)] for _ in range(3)]
            board.clear()
            draw_board()



# Main game loop
display_text("Player O turn" if turn else "Player X turn", -200, 350)
draw_board()
screen.onclick(click_handler)

screen.mainloop()