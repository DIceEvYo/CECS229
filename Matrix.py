""" 
Name: Dev Paul
"""
class Matrix:
	
	# input: mat (a 2d list)
	# Example: Matrix([[1, 2, 3], [2, 4, 6]]) makes a matrix like...
	# [1 2 3 ]
	# [2 3 6 ]
	def __init__(self, mat):
		# ALREADY DONE FOR YOU! DO NOT TOUCH
		self.m = mat 				# the matrix
		self.rows = len(mat)		# number of rows
		self.cols = len(mat[0])		# number of columns

	# get's the element of the matrix in row i, column j
	def get_element(self, i, j):
		# ALREADY DONE FOR YOU! DO NOT TOUCH
		return self.m[i][j]

	# Part3
	# TODO: implement matrix addition
	# inputs: self, other
	# output: if matrix addition is possible, return the sum Matrix
	#		  DO NOT RETURN A 2D LIST! YOU WILL GET IT WRONG!
	# 		  if matrix addition is not possible, return None
	def __add__(self, other):
		if (self.rows != other.rows) or (self.cols != other.cols):
			return None
		sum = [[0 for j in range(self.cols)] for i in range(self.rows)]
		#Line 30 (Above) Referenced from: https://www.kite.com/python/answers/how-to-initialize-a-2d-list-in-python#:~:text=Use%20a%20list%20comprehension%20to,of%20elem%20in%20each%20sublist.
		for i in range(self.rows):
			for j in range(self.cols):
				sum[i][j] = (self.get_element(i,j) + other.get_element(i,j))
		return Matrix(sum)

	# Part4
	# TODO: implement matrix subtraction
	# inputs: self, other
	# output: if matrix subtraction is possible, return the difference Matrix
	#		  DO NOT RETURN A 2D LIST! YOU WILL GET IT WRONG!
	# 		  if matrix subtraction is not possible, return None
	def __sub__(self, other):
		if (self.rows != other.rows) or (self.cols != other.cols):
			return None
		sub = [[0 for j in range(self.cols)] for i in range(self.rows)]
		#Line 46 (Above) Referenced from: https://www.kite.com/python/answers/how-to-initialize-a-2d-list-in-python#:~:text=Use%20a%20list%20comprehension%20to,of%20elem%20in%20each%20sublist.
		for i in range(self.rows):
			for j in range(self.cols):
				sub[i][j] = (self.get_element(i,j) - other.get_element(i,j))
		return Matrix(sub)


	# Part5
	# TODO: implement dot product
	# inputs: self, other
	# output: if matrix multiplication is possible, return the product Matrix
	#		  DO NOT RETURN A 2D LIST! YOU WILL GET IT WRONG!
	# 		  if matrix multiplication is not possible, return None
	def __mul__(self, other):
		if (self.cols != other.rows):
			return None
		mul = [[0 for j in range(other.cols)] for i in range(self.rows)]
		#Line 63 (Above) Referenced from: https://www.kite.com/python/answers/how-to-initialize-a-2d-list-in-python#:~:text=Use%20a%20list%20comprehension%20to,of%20elem%20in%20each%20sublist.
		for k in range(other.cols):
			for i in range(self.rows):
				total = 0
				for j in range(self.cols):
					total += (self.get_element(i,j) * other.get_element(j,k))
				mul[i][k] = total
				#print("k: ", k)
		return Matrix(mul)


	# DO NOT TOUCH! For debugging purposes
	def __str__(self):
		string = ""
		for r in self.m:
			string += "["
			for c in r:
				string += str(c) + " "
			string += "]\n"
		return string



# test cases
# Everything below MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run


def checker(expected, actual):
	if type(expected) == type(actual):
		if str(expected) == str(actual):
			print("CORRECT!")
		else: 
			print("expected:\n" + str(expected) + ", but got:\n" + str(actual))
	else:
		print("Data type issue!")

mat1 = Matrix([[1, 2, 3],
			  [4, 6, 8]])

mat2 = Matrix([[-10, 9, 4],
			  [ -19, 4, 2],
			  [7, -3, 2]])

mat3 = Matrix([[1, 6],
			  [-10, 7]])

mat4 = Matrix([[9, -4, 3],
			  [10, -2, 1]])

test1 = mat4 + mat1
expected1 = Matrix([[10, -2, 6], [14, 4, 9]])
checker(expected1, test1)

test2 = mat1 + mat2
expected2 = None
checker(expected2, test2)

test3 = mat4 - mat1
expected3 = Matrix([[8, -6, 0], [6, -8, -7]])
checker(expected3, test3)

test4 = mat1 - mat2
expected4 = None
checker(expected4, test4)

test5 = mat3 * mat1
expected5 = Matrix([[25, 38, 51], [18, 22, 26]])
#print("test5: " + test5)
checker(expected5, test5)

test6 = mat1 * mat3
expected6 = None
checker(expected6, test6)





