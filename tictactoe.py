# get input1 
# check if its valid, if not, we ask for input again
# set input1 in a list
# print the list
#
# get input2
# check if its valid
# check if the game is done

game = 1
turn = 0
board = [ 'O', '-', '-', 'X', '-', '-', 'X', '-', '-'] 

def getinput():
    playernum = int(isodd(turn)) + 1  
    playerin = int(input(f"Player {playernum}'s choice: "))
    return playerin

def iseven(x):
    if x & 1:
        return False
    else:
        return True

def isodd(x):
    return not iseven(x)

def drawboard():
	for i in range(1, len(board)+1): 
		if i % 3 == 0:
			print(board[i-1], end='')
			print("", end='\n')
		else:
			print(board[i-1], end='')

def isvalid(move):
	if board[move] == 'O' or board[move] == 'X':
		return False
	else:
		return True

col = [ '-', '-', '-']
row = [ '-', '-', '-']
diag1 = [ '-', '-', '-']
diag2 = [ '-', '-', '-']		

def winningcondition(move):	
	win = True
	for i in range(9):
		if i % 3 == 0:
			i += 1
			print(board[i-1])
			if board[i-1] == 'X' and win:
				win = True
			else:
				win = False
	print( win )


winningcondition(3)

'''
turn = 0
while game:
	position = getinput() - 1
	if position <= 8 and position >= 0 and isvalid(position): 
			if turn >= 2 and winningcondition(position):
				game = 0
			if isodd(turn):
				board[position] = 'X'
			else:
				board[position] = 'O'
			turn += 1
			drawboard()
	else:
		print("Invalid move. Try again.")

else:
	playernum = int(isodd(turn)) + 1  
	print(f"Player {playernum} won!")
'''
