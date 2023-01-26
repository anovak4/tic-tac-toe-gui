import turtle as trtl

x_turtles = []
y_turtles = []
centers = {1: (-50, 50), 2: (0, 50), 3: (50, 50), 4: (-50, 0), 5: (0, 0), 6: (50, 0), 7: (-50, -50), 8: (0, -50), 9: (50, -50)}
available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x_spots = []
y_spots = []
combos = [(1, 2, 3), (1, 4, 7), (1, 5, 9), (2, 5, 8), (3, 5, 7), (3, 6, 9), (4, 5, 6), (7, 8, 9)]
is_player_one = True

wn = trtl.Screen()
wn.addshape("x.gif")
wn.addshape("y.gif")
wn.setup(400, 400)

board = trtl.Turtle()
board.hideturtle()
board.pensize(3)
board.pencolor("deeppink")
board.speed(0)

turn_writer = trtl.Turtle()
turn_writer.penup()
turn_writer.hideturtle()
turn_writer.goto(-175, 140)
turn_writer.color("deeppink")
turn_font = ("Arial", 30, "bold")
message_writer = trtl.Turtle()
message_writer.penup()
message_writer.hideturtle()
message_writer.goto(-175, -175)
message_writer.color("deeppink")
message_font = ("Arial", 45, "bold")



for i in range(0, 5):
  x = trtl.Turtle()
  x.hideturtle()
  x.shape("x.gif")
  x.speed(0)
  x.penup()
  x.goto(0,100)
  x_turtles.append(x)
  
  y = trtl.Turtle()
  y.hideturtle()
  y.shape("y.gif")
  y.speed(0)
  y.penup()
  y.goto(0,-100)
  y_turtles.append(y)

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



def fill_spot(turtles, spot):
  peice = turtles.pop()
  x_cor = centers[spot][0]
  y_cor = centers[spot][1]
  peice.goto(x_cor, y_cor)
  peice.showturtle()

def determine_spot(x_cor, y_cor):
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
  return spot

def write_turn():
  turn_writer.clear()
  if is_player_one:
    turn_writer.write("Turn: X", font=turn_font)
  else:
    turn_writer.write("Turn: Y", font=turn_font)

def player_turn(x_cor, y_cor):
  global is_player_one
  spot = determine_spot(x_cor, y_cor)
  if spot in available:
    if is_player_one:
      fill_spot(x_turtles, spot)
      x_spots.append(spot)
    else:
      fill_spot(y_turtles, spot)
      y_spots.append(spot)
    available.remove(spot)
    is_player_one = not is_player_one
    write_turn()
    is_over()

# parameter spot_list is either x_spots or y_spots, lists of the spots filled by each letter
def won(spot_list):
  count = 0
  for combo in combos:
    for spot in combo:
      if spot in spot_list:
        count += 1
    if count >= 3:
      return True
    else:
      count = 0

def is_over():
  if won(x_spots):
    wn.onclick(None)
    turn_writer.clear()
    message_writer.write("X won!", font=message_font)
  elif won(y_spots):
    wn.onclick(None)
    turn_writer.clear()
    message_writer.write("Y won!", font=message_font)
  elif len(available) == 0:
    wn.onclick(None)
    turn_writer.clear()
    message_writer.write("It's a tie!", font=message_font)



write_turn()
wn.onclick(player_turn)
wn.listen()
wn.mainloop()