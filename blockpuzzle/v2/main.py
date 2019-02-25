from colored import fg, bg, attr
import numpy as np

#make blank 7x7 block
board = np.zeros(7)

#numbered the same as in the assignment
H = [(0,0), (0,3), (1,0), (1,4), (1,5), (3,2), (3,3), (4,1), (4,4), (4,6), (5,3), (6,0), (6,4), (6,5)]

# https://pypi.org/project/colored/ for color list
# unit list start at 0,0 top left. use coords as if the piece were encapsulated by a rectangle with that coordinate system.
class Piece:
  #rotate 90 degrees counterclockwise
  def rotate90(self, alist):
    for i, item in enumerate(alist):
      (x,y) = item
      tempx = -1 * y
      tempy = x
      alist[i] = (tempx, tempy)
    #return self.zeroup(alist.copy())
    return alist.copy()

  def __init__(self, color, unit_list):
    self.color = color
    self.rotation = [1,1,1,1]
    self.rotation[0] = unit_list.copy()
    self.rotation[1] = self.rotate90(unit_list.copy())
    self.rotation[2] = self.rotate90(self.rotation[1].copy())
    self.rotation[3] = self.rotate90(self.rotation[2].copy())
    self.unit_count = len(self.rotation[0])
    self.is_placed = False
    self.is_out_of_bounds = False

  def printme(self):
    for i in range(4):
      print(self.rotation[i] )
    print('-----------')

def printBoard(A):
  for line in A:
    for item in line:
      if isinstance(item, tuple):
        (block, color) = item
        print('%s%s%i%s' % (fg(color), bg(color), block, attr('reset')), end='')
      else:
        print('%s%s %s' % (fg('white'), bg('white'), attr('reset')), end='')
    print(' ')
  print(' ')

def showCoverage(A):
  for line in A:
    for item in line:
      if item > 1:
        print('%s%s %s' % (fg('gray'), bg('gray'), attr('reset')), end='')
      elif item == 1:
        print('%s%s %s' % (fg('green'), bg('green'), attr('reset')), end='')
      else:
        print('%s%s %s' % (fg('white'), bg('white'), attr('reset')), end='')

hole = Piece('black',[(0,0)])
pieces = [
  Piece('red', [
      (0,0), (0,1),
      (1,0), (1,1), (1,2), 
      (2,0), (2,1)
  ]),
  Piece('gold_1', [
      (0,0), (0,1),
             (1,1), (1,2),
                    (2,2)
  ]),
  Piece('green',[
             (0,1), (0,2),
      (1,0), (1,1), (1,2),
             (2,1), (2,2), (2,3)
  ]),
  Piece('dark_cyan', [
      (0,0), (1,0), (2,0), (3,0), (4,0)
  ]),
  Piece('dark_orange', [
      (0,0), (1,0)
  ]),
  Piece('orange_red_1', [
             (0,1),
      (1,0), (1,1),
      (2,0), (2,1),
             (3,1)
  ]),
  Piece('purple_1a', [
      (0,0),
      (1,0), (1,1),
      (2,0), (2,1), (2,2)
  ]),
  Piece('magenta', [
             (0,1),
      (1,0), (1,1), (1,2)
  ]),
  Piece('blue', [
      (0,0), (0,1), (0,2), (0,3),
                    (1,2)
  ])
] 

def validLocation(x,y):
  return x >= 0 and x < 7 and y >=0 and y < 7

def placePiece(board, piece, location, rotates):
  for unit in piece.rotation[rotates]:
    (x,y) = unit
    if validLocation(location[0]+x,location[1]+y):
      board[location[0]+x, location[1]+y] += 1
    else:
      piece.is_out_of_bounds = True
  return board

def fitness(board):
  score = 0
  for x in np.nditer(board):
    score += 2**abs(1-x)
  return score

#def findSolution(board, pieces, hole):
 # bestSolution = (board, fitness(board))



