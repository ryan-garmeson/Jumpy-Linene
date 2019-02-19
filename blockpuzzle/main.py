import puzzlerepresent as P
#setup
A = P.A
H = P.H
hole = P.hole
pieces = P.pieces
#hole
A = P.placePiece(A, hole, H[11])
#red 3x3
A = P.placePiece(A, pieces[0].rotate(-4), [1,0])
P.printBoard(A)
#print(' ')
#yellow 3x3
A = P.placePiece(A, pieces[1], [1,3])
P.printBoard(A)
#print(' ')
#green 3x4
A = P.placePiece(A, pieces[2].rotate(1), [3,0])
P.printBoard(A)
#print(' ')
#teal 1x5
A = P.placePiece(A, pieces[3].rotate(1), [6,2])
P.printBoard(A)
#print(' ')
#orange 1x2
A = P.placePiece(A, pieces[4].rotate(1), [5,4])
P.printBoard(A)
#print(' ')
#red 2x4 
A = P.placePiece(A, pieces[5].rotate(2), [2,3])
P.printBoard(A)
#print(' ')
#purple 3x3
A = P.placePiece(A, pieces[6].rotate(2), [0,4])
P.printBoard(A)
#print(' ')
#purple 2x3 
A = P.placePiece(A, pieces[7].rotate(1), [3,5])
P.printBoard(A)
#print(' ')
#blue 2x4
A = P.placePiece(A, pieces[8], [0,0])
#print to terminal
P.printBoard(A)
