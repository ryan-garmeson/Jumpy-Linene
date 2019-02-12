from colored import fg, bg, attr

#make blank 7x7 block
A = [[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],
[1,1,1,1,1,1,1],]

#numbered the same as in the assignment
H = [[0,0], [0,3], [1,0], [1,4], [1,5], [3,2], [3,3], [4,1], [4,4], [4,6], [5,3], [6,0], [6,4], [6,5]]

# https://pypi.org/project/colored/ for color list
# unit list start at 0,0 top left. use coords as if the piece were encapsulated by a rectangle with that coordinate system.
class Piece:
  def __init__(self, color, unit_list):
    self.color = color
    self.unit_list = unit_list
    self.unit_count = len(unit_list)

hole = Piece('black',[[0,0]])
pieces = [
  Piece('red', [[0,0], [0,1], [1,0], [1,1], [2,0], [2,1], [1,2]]),
  Piece('gold_1', [[0,0], [0,1], [1,1], [1,2], [2,2]]),
  Piece('green', [[0,1], [0,2], [1,0], [1,1], [1,2], [2,1], [2,2], [2,3]]),
  Piece('dark_cyan', [[0,0], [1,0], [2,0], [3,0], [4,0]]),
  Piece('dark_orange', [[0,0], [1,0]]),
  Piece('orange_red_1', [[0,1], [1,0], [1,1], [2,0], [2,1], [3,1]]),
  Piece('purple_1a', [[0,0], [1,0], [1,1], [2,0], [2,1], [2,2]]),
  Piece('magenta', [[0,1], [1,0], [1,1], [1,2]]),
  Piece('blue', [[0,0], [0,1], [0,2], [0,3],[1,2]])
]  

def willFit(board, piece, location):
  for unit in piece.unit_list:
    if board[location[0]+unit[0]][location[1]+unit[1]] != 1:
      return False
  return True

def placePiece(board, piece, location):
  if willFit(board, piece, location):
    for unit in piece.unit_list:
      board[location[0]+unit[0]][location[1]+unit[1]] = (piece.unit_count, piece.color)
  return board

def printBoard(A):
  for line in A:
    for item in line:
      if isinstance(item, tuple):
        (block, color) = item
        print('%s%s%i%s' % (fg(color), bg(color), block, attr('reset')), end='')
      else:
        print('%s%s %s' % (fg('white'), bg('white'), attr('reset')), end='')
    print(' ')
#how to use it
A = placePiece(A, pieces[0], [0,0])
#print to terminal
printBoard(A)
