import turtle as trtl

# variables ------------

x_turtles = []
y_turtles = []
centers = {
    1: (-50, 50),
    2: (0, 50),
    3: (50, 50),
    4: (-50, 0),
    5: (0, 0),
    6: (50, 0),
    7: (-50, -50),
    8: (0, -50),
    9: (50, -50)
}
available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
used = []
x_used = []
y_used = []
combos = [(1, 2, 3), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 5, 7), (3, 6, 9), (4, 5, 6), (7, 8, 9)]
player_one = True
end = False
message = ""

wn = trtl.Screen()
wn.addshape("x.gif")
wn.addshape("y.gif")
wn.setup(400, 400)
board = trtl.Turtle()
board.pensize(2)
board.pencolor("deeppink")
board.speed(0)

turn_writer = trtl.Turtle()
turn_writer.penup()
turn_writer.hideturtle()
turn_writer.goto(-175, 150)
turn_writer.color("deeppink")
turn_font = ("Arial", 15, "bold")
message_writer = trtl.Turtle()
message_writer.penup()
message_writer.hideturtle()
message_writer.goto(-175, -175)
message_writer.color("deeppink")
message_font = ("Arial", 30, "bold")

# setup ------------

for i in range(0, 9):
    x_turtles.append(trtl.Turtle())
    y_turtles.append(trtl.Turtle())
for x in x_turtles:
    x.hideturtle()
    x.shape("x.gif")
    x.speed(0)
for y in y_turtles:
    y.hideturtle()
    y.shape("y.gif")
    y.speed(0)

x_offset = -25
for i in range(0, 2):
    board.penup()
    board.goto(x_offset, 75)
    board.setheading(-90)
    board.pendown()
    board.forward(150)
    x_offset += 50
y_offset = 25
for i in range(0, 2):
    board.penup()
    board.goto(-75, y_offset)
    board.setheading(0)
    board.pendown()
    board.forward(150)
    y_offset -= 50
board.hideturtle()

# move turtles to top and bottom
count = 1
for x in x_turtles:
    x.setheading(90)
    x.penup()
    x.forward(100 + 35 * (count % 3))
    if count <= 3:
        x.left(90)
        x.forward(50)
    elif count <= 6:
        x.right(90)
        x.forward(50)
    count += 1
count = 1
for y in y_turtles:
    y.setheading(-90)
    y.penup()
    y.forward(100 + 35 * (count % 3))
    if count <= 3:
        y.left(90)
        y.forward(50)
    elif count <= 6:
        y.right(90)
        y.forward(50)
    count += 1

# methods ------------


def fill_spot(turtles, spot):
    peice = turtles.pop(0)
    peice.speed(3)
    x_cor = centers[spot][0]
    y_cor = centers[spot][1]
    peice.goto(x_cor, y_cor)
    peice.showturtle()


def write_turn():
    global player_one, turn_writer
    turn_writer.clear()
    if player_one:
        turn_writer.write("Turn: 1", font=turn_font)
    else:
        turn_writer.write("Turn: 2", font=turn_font)


def player_turn(x_cor, y_cor):
    global player_one, message, end, message_writer
    if x_cor <= -25:
        if y_cor >= 25:
            spot = 1
        elif y_cor <= -25:
            spot = 7
        else:
            spot = 4
    elif x_cor >= 25:
        if y_cor >= 25:
            spot = 3
        elif y_cor <= -25:
            spot = 9
        else:
            spot = 6
    else:
        if y_cor >= 25:
            spot = 2
        elif y_cor <= -25:
            spot = 8
        else:
            spot = 5

    if spot in available:
        if player_one:
            fill_spot(x_turtles, spot)
            x_used.append(spot)
        else:
            fill_spot(y_turtles, spot)
            y_used.append(spot)
        available.remove(spot)
        used.append(spot)
        player_one = not player_one
        write_turn()
    end = is_over()
    if end:
        wn.onclick(None)
        turn_writer.clear()
        message_writer.write(message, font=message_font)


# to work for the create project, this would need a parameter - maybe dont use global variables so you can pass in a parameter?
def is_over():
    global message, available
    count = 0
    for c in combos:
        for n in c:
            if n in x_used:
                count += 1
        if count >= 3:
            message = "Player 1 won!"
            return True
        else:
            count = 0
    for c in combos:
        for n in c:
            if n in y_used:
                count += 1
        if count >= 3:
            message = "Player 2 won!"
            return True
        else:
            count = 0
    if len(available) == 0:
        message = "It's a tie!"
        return True
    return False


# method calls ------------

write_turn()
wn.onclick(player_turn)
wn.listen()
wn.mainloop()
