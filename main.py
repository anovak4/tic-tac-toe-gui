import turtle as trtl

class Board:

  centers = {1:(-50,50), 2:(0,50), 3:(50,50), 4:(-50,0), 5:(0,0), 6:(50,0), 7:(-50,-50), 8:(0,-50), 9:(50,-50)}
  combos = [(1,2,3), (1,4,7), (1,5,9), (2,5,8), (3,5,7), (3,6,9), (4,5,6), (7,8,9)]

  def __init__(self):
    self.available = [1,2,3,4,5,6,7,8,9]
    self.used = []
    self.x_spots = []
    self.y_spots = []
    self.is_player_one = True

    self.board_drawer = trtl.Turtle()
    self.board_drawer.hideturtle()
    self.board_drawer.pensize(3)
    self.board_drawer.pencolor("deeppink")
    self.board_drawer.speed(0)

    x_offset = -25
    for i in range(0, 2):
      self.board_drawer.penup()
      self.board_drawer.goto(x_offset, 75)
      self.board_drawer.setheading(-90)
      self.board_drawer.pendown()
      self.board_drawer.forward(150)
      x_offset += 50
    y_offset = 25
    for i in range(0, 2):
      self.board_drawer.penup()
      self.board_drawer.goto(-75, y_offset)
      self.board_drawer.setheading(0)
      self.board_drawer.pendown()
      self.board_drawer.forward(150)
      y_offset -= 50

    self.turn_writer = trtl.Turtle()
    self.turn_writer.hideturtle()
    self.turn_writer.penup()
    self.turn_writer.goto(-175, 140)
    self.turn_writer.color("deeppink")
    self.turn_font = ("Arial", 30, "bold")

    self.message_writer = trtl.Turtle()
    self.message_writer.hideturtle()
    self.message_writer.penup()
    self.message_writer.goto(-175, 120)
    self.message_writer.color("deeppink")
    self.message_font = ("Arial", 45, "bold")

  def fill_spot(self, turtles, spot):
    self.peice = turtles.pop()
    self.x_cor = self.centers[spot][0]
    self.y_cor = self.centers[spot][1]
    self.peice.goto(self.x_cor, self.y_cor)
    self.peice.showturtle()

  def write_turn(self):
    self.turn_writer.clear()
    if self.is_player_one:
      self.turn_writer.write("Turn: X", font=self.turn_font)
    else:
      self.turn_writer.write("Turn: Y", font=self.turn_font)

  # parameter spot_list is either x_spots or y_spots, lists of the spots filled by each letter
  def won(self, spot_list):
    count = 0
    for combo in self.combos:
      for spot in combo:
        if spot in spot_list:
          count += 1
      if count >= 3:
        self.turn_writer.clear()
        return True
      else:
        count = 0

  def is_over(self):
    if self.won(self.x_spots):
      self.message_writer.write("X won!", font=self.message_font)
      return True
    elif self.won(self.y_spots):
      self.message_writer.write("Y won!", font=self.message_font)
      return True
    elif len(self.available) == 0:
      self.turn_writer.clear()
      self.message_writer.write("It's a tie!", font=self.message_font)
      return True
    else:
      return False
  
  def reset(self):
    self.available = [1,2,3,4,5,6,7,8,9]
    self.used = []
    self.x_spots = []
    self.y_spots = []
    self.is_player_one = True

# setup ------------------------------------------------

board = Board()
x_turtles = []
y_turtles = []

wn = trtl.Screen()
wn.addshape("x.gif")
wn.addshape("y.gif")
wn.setup(400, 400)
wn.title("Tic Tac Toe")

# functions ------------------------------------------------

def create_turtles():
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

def player_turn(x_cor, y_cor):
  spot = determine_spot(x_cor, y_cor)
  if spot in board.available:
    if board.is_player_one:
      board.fill_spot(x_turtles, spot)
      board.x_spots.append(spot) # this isn't exactly good practice but check best practice for python...
    else:
      board.fill_spot(y_turtles, spot)
      board.y_spots.append(spot) # see note on x_spots.append()
    board.available.remove(spot)
    board.used.append(spot)
    board.is_player_one = not board.is_player_one
    board.write_turn()
    if board.is_over():
      wn.onclick(None)
      draw_restart_button()

def draw_restart_button():
  button = trtl.Turtle()
  button.hideturtle()
  button.penup()
  button.color("deeppink")
  button.pensize(2)
  button.speed(0)
  button.goto(-75, -100)
  button.pendown()
  for i in range(0,2):
    button.forward(150)
    button.right(90)
    button.forward(50)
    button.right(90)
  button.penup()
  button.goto(-55, -140)
  button.write("Restart?", font=("Arial", 20, "normal"))
  wn.onclick(restart)

def restart(x, y):
  global board
  if x >= -75 and x <= 75 and y <= -100 and y >= -150:
    wn.clearscreen()
    board = Board()
    x_turtles.clear()
    y_turtles.clear()
    create_turtles()
    board.write_turn()
    wn.onclick(player_turn)

# function calls ------------------------------------------------

create_turtles()
board.write_turn()
wn.onclick(player_turn)
wn.listen()
wn.mainloop()