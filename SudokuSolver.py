
# learn to use git to come back to previous commits (off subject)
# process each cell or (lbl,cbc)
# each cell: use list matching nubmers in two list: (of 0-8 --> nubmers != c or l) --> use Possible l and c for 
# It will search the smallest nubmer in the list in the section, if number > smallest in l or c the next smallest number
#
#
# scan PossibleLine if 0>2 next line; if 0<2 append sudoku, RS + RD + RC + RL
# scan PossibleCol if 0>2 next Col; if 0<2 append sudoku, RS + RD + RC + RL
# scan PossibleSection if 0>2 next section; if 0<2 append sudoku, RS + RD + RC + RL
#

def main(sudoku):

	SectionList = [
	[0, 1, 2, 9, 10, 11, 18, 19, 20],
    [3, 4, 5, 12, 13, 14, 21, 22, 23],
    [6, 7, 8, 15, 16, 17, 24, 25, 26],
    [27, 28, 29, 36, 37, 38, 45, 46, 47],
    [30, 31, 32, 39, 40, 41, 48, 49, 50],
    [33, 34, 35, 42, 43, 44, 51, 52, 53],
    [54, 55, 56, 63, 64, 65, 72, 73, 74],
    [57, 58, 59, 66, 67, 68, 75, 76, 77],
    [60, 61, 62, 69, 70, 71, 78, 79, 80]]
	SectionListLink = [0,0,0,1,1,1,2,2,2,0,0,0,1,1,1,2,2,2,0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,3,3,3,4,4,4,5,5,5,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,6,6,6,7,7,7,8,8,8,6,6,6,7,7,7,8,8,8]
	LineList = [[i for i in range(j, j+9)] for j in range(0, 81, 9)]
	LineListLink = [(i // 9) % 9 for i in range(81)]
	ColumnList = [[LineList[j][i] for j in range(9)] for i in range(9)]
	ColumnListLink = [i % 9 for i in range(81)]

	PossibleCol = [[0 for i in range(9)] for j in range(9)]
	PossibleLine = [[0 for i in range(9)] for j in range(9)]
	PossibleSec = [[0 for i in range(9)] for j in range(9)]
	PossibleIndexes = [[0 for x in range(81)] for y in range(9)]
	PossibleCoordinates = [(x, y) for x in range(9) for y in range(9)]
	AllPossibleValuesCoordinates = [(y, x) for y in range(9) for x in range(9)]	
	placed = True


	def unsearch(INC) #Index_Number_of_Coordinate

		PossibleLine[number][LineListLink[INC]] = 1
		PossibleCol[number][ColumnListLink[INC]] = 1
		PossibleSec[number][SectionListLink[INC]] = 1

		for numberD in range(9): #Process each digit in Possible Coordinates
			PossibleIndexes[numberD][INC] = 1	
		for SINC in SectionList[SectionListLink[INC]]: # IN each Section for each Number
			PossibleIndexes[number][SINC] = 1
		for CINC in ColumnList[ColumnListLink[INC]]: # In each Column for each number
			PossibleIndexes[number][CINC] = 1
		for LINC in LineList[LineListLink[INC]]: # In Line for each number
			PossibleIndexes[number][LINC] = 1 


	def searchandplace(Possible,List):
		for number in range(9):	
			for n in range(9):
				if Possible[number][n] == 0:
					count = 0
					for INC in List[n]:
						if PossibleIndexes[number][INC] == 0:
							count = count + 1
							storedINC = INC
					if count == 1:
						placed = True
						sudoku[number].append(PossibleCoordinates[storedINC])
						unsearch(storedINC)
	

	for number in range(9): #Init
		for NC in sudoku[number]:
			INC = NC[1]+NC[0]+NC[0]*8
			unsearch(INC)

						
	while placed == True: #Search And Place
		placed = False
		searchandplace(PossibleLine,LineList)
		searchandplace(PossibleCol,ColumnList)
		searchandplace(PossibleSec,SectionL:wist)



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



if __name__ == "__main__":
	Print_Output(ConvertToOutput(sudoku))
	main(sudoku)
	print()
	Print_Output(ConvertToOutput(sudoku))






















