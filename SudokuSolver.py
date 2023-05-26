def ConvertToOutput(var):
	Output = [[0 for r in range(9)] for r in range(9)]
	for number in range (9): #for number in sudoku
		for x in var[number]: #for position of number in sudoku
			Output[x[0]][x[1]]=number+1 #2d matrix position = number
	return Output

def Print_Output(Output):
	for x in range(9): #display 2d matrix line by line
		for y in range(9):
			print(Output[x][y],end='')
			if y in [2,5]:
				print('|',end='')
			else:
				print(' ',end='')
		print('')
		if x in [2,5]:
			print("-----------------")

class Node: # Define a Node class for the binary search tree
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None

def build_bst(lst): # Define a function to build the binary search tree
	root = Node(lst[0])
	for i in range(1, len(lst)):
		insert_node(root, lst[i])
	return root

def insert_node(root, val): # Define a function to insert a node into the binary search tree
	if root is None:
		root = Node(val)
	elif val < root.val:
		if root.left is None:
			root.left = Node(val)
		else:
			insert_node(root.left, val)
	else:
		if root.right is None:
			root.right = Node(val)
		else:
			insert_node(root.right, val)

def search_bst(root, val): # Define a function to search for a value in the binary search tree
	if root is None:
		return False
	elif root.val == val:
		return True
	elif val < root.val:
		return search_bst(root.left, val)
	else:
		return search_bst(root.right, val)







def solve(sudoku):
	
	AllPossibleValuesCoordinates = [[(x, y) for y in range(9)] for x in range(9)]	
	SectionList = [
	[0, 1, 2, 9, 10, 11, 18, 19, 20],
    [3, 4, 5, 12, 13, 14, 21, 22, 23],
    [6, 7, 8, 15, 16, 17, 24, 25, 26],
    [27, 28, 29, 36, 37, 38, 45, 46, 47],
    [30, 31, 32, 39, 40, 41, 48, 49, 50],
    [33, 34, 35, 42, 43, 44, 51, 52, 53],
    [54, 55, 56, 63, 64, 65, 72, 73, 74],
    [57, 58, 59, 66, 67, 68, 75, 76, 77],
    [60, 61, 62, 69, 70, 71, 78, 79, 80]
	]

	SectionListLink = [0,0,0,1,1,1,2,2,2,0,0,0,1,1,1,2,2,2,0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,3,3,3,4,4,4,5,5,5,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,6,6,6,7,7,7,8,8,8,6,6,6,7,7,7,8,8,8]

	LineList = [[i for i in range(j, j+9)] for j in range(0, 81, 9)]
	LineListLink = [(i // 9) % 9 for i in range(81)]

	ColumnList = [[i+j*9 for i in range(9)] for j in range(9)]
	ColumnListLink = [i % 9 for i in range(81)]

	PossibleIndexes = [[x for x in range(81)] for y in range(9)]

	#possible coordinates 9*9
	PossibleCoordinates = [(x, y) for x in range(9) for y in range(9)]

	NumberIndexValues = [[]for x in range (9)]
	AddValues = []	
	RemoveValues = []
	IndexValue = 0


	for numberx in range(9): #for each digit in the sudoku
		for NC in sudoku[numberx]:
			NumberIndexValues[numberx].append(NC[1]+NC[0]+NC[0]*8)
	
	
	
	Print_Output(ConvertToOutput(sudoku))

	for rand in range(1):
	
		for number in range(9): #Remove placed numbers from Number Possible Values
			bst = build_bst(PossibleIndexes[number])
			for numberx in range(9):
				for value in NumberIndexValues[numberx]:
					if search_bst(bst, value):
						PossibleIndexes[number].remove(value)	

		for number in range(9): #Remove Corressponding section from Number Possible Values
			bst = build_bst(PossibleIndexes[number])
			for value in NumberIndexValues[number]:
				for val in SectionList[SectionListLink[value]]:
					if search_bst(bst, val):
						PossibleIndexes[number].remove(val) 
		
		for number in range(9): #Processing To remove Possible Values and Append to Sudoku
			
			bst = build_bst(PossibleIndexes[number])
			for value in NumberIndexValues[number]:
				for val in ColumnList[ColumnListLink[value]]:
					if search_bst(bst, val):	
						PossibleIndexes[number].remove(val) 

			bst = build_bst(PossibleIndexes[number])
			for value in NumberIndexValues[number]:
				for val in LineList[LineListLink[value]]:
					if search_bst(bst, val):
						PossibleIndexes[number].remove(val) 


	for x in PossibleIndexes:
		print(x)



"""
sudoku = [[],[],[],[],[],[],[],[],[]]
	for x in range (9):
		line=input("Input Sudoku square line "+str(x+1)+":")
		for y in range (9):
			number=line[y];
			sudoku[int(number)-1].append((x,y)) 
	for u in range (9):
		print(sudoku[u])
"""

sudoku = [
		[(0,4),(2,0),(4,3)],
		[(5,0),(4,5),(8,1)],
		[(1,3),(2,8),(8,2)],
		[(0,7),(4,4),(3,8),(7,5)],
		[(3,1),(5,5),(8,4),(6,8)],
		[(1,1),(0,6),(6,0),(7,7)],
		[(1,7)],
		[(2,5),(3,3),(6,2)],
		[(2,6),(5,7),(6,3),(7,1)]
		]
solve(sudoku)

Print_Output(ConvertToOutput(sudoku))






















