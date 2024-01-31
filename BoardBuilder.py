#This is the function to build the board.


def new_board():
    board_size = 0
    while board_size == 0:
      size = str(input("Please enter S / M / L for board size")).upper()
      if size == "S":
          board_size = 6
      if size == "M":
          board_size = 9
      if size == "M":
          board_size = 12
      elif board_size == 0:
          print("Invalid input. Please type only S / M / L")

    return board_size

new_board()
