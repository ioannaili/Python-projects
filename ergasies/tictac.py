import random 
board=[' ' for x in range(10)]

def insertLetter(letter,pos):
     board[pos]=letter

def spaceIsFree(pos):
     return board[pos]==' '

def drawBoard(board):

     print('   |   |')

     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

     print('   |   |')

     print('-----------')

     print('   |   |')

     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

     print('   |   |')

     print('-----------')

     print('   |   |')

     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

     print('   |   |')

def isWinner(bo, le):

   return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le))

def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def playerMove():
     run=True
     while run:
          move=input('Select a position to place an X: ')
          try:
               move=int(move)
               if move>0 and move<10:
                     if spaceIsFree(move):
                          run=False
                          insertLetter('X',move)
                     else:
                          print('This spot is taken!')
               else:
                    print('Enter a valid number')
          except:
               print('Invalid input')
def compMove():

         random.seed()
         move=random.randint(0,8)
         
         if spaceIsFree(move):
               return move
             
     
print('Welcome')
drawBoard(board)
    
while not(isBoardFull(board)):
   if not(isWinner(board,'O')):
       playerMove()
       drawBoard(board)
   else:
       print('You lost!')
       break

   if not(isWinner(board,'X')):

       move=compMove()
       if move==0:
          print('It\'s a tie')
       else:
          insertLetter('O',move)
          print('Computer placed an \'O\' in position', move , ':')
          drawBoard(board)
   else:   
          print('You won!')
          break
          
if isBoardFull(board):
    print('It\'s a tie')
            
            




