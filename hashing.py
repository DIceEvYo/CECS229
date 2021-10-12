# hash table
class hash_table:

	# constructor
	# inputs: size (defaults to 8 if no arguments are provided)
	def __init__(self, size = 8):
		# self.table: empty hash table of indicated size
		self.table = (None,) * size
		# self.size: number of positions in table
		self.size = size


	# Already completed function!
	# INSERTS value INTO HASHTABLE AT index
	# example: insert(5, 10) will place 5 into index#10
	def insert(self, value, index):
		temp = list(self.table)
		temp[index] = value
		self.table = tuple(temp)


	# function name: linear_probe
	# input: value- value to be inserted
			#start_index- where linear probing starts
	# output: returns the index of the hash_table that the value should be 
		#	inserted after linear probing
	# restrictions: Although you can implement this function with just one input, 
		# DO NOT alter the function heading
	# assumptions: value will always be an integer
		#	your table will always be big enough
	def linear_probe(self, value, start_index):
		# hint: empty spots in tuples are labeled as None
		if (self.containsN(start_index)):
			self.insert(value, start_index)
		else:
			fullRound = 0
			while (not (self.containsN(start_index)) and fullRound < self.size):
				start_index += 1
				if (start_index == self.size):
					start_index = 0
				fullRound += 1
			if (self.containsN(start_index)):
				self.insert(value, start_index)
		return value
		#print(self.table)



	# function name: insert
	# input: value- value to be inserted
	# output: Do not return anything. Just insert value into the proper position
		#	in self.table. Utilize linear_probe and insert in this function
	# assumptions: value will always be an integer
		#	your table will always be big enough
	def hash(self, value):
		index = (value%(self.size))
		if (self.containsN(index)):
			self.insert(value, index)
		else:
			fullRound = 0
			while(not(self.containsN(index)) and fullRound < self.size):
				index += 1
				if(index == self.size):
					index = 0
				fullRound+= 1
			if(self.containsN(index)):
				self.insert(value,index)
		#print(self.table)
		# hint: empty spots in tuples are labeled as None


	def containsN(self, index):
		temp = list(self.table)
		if (temp[index] == None):
			return True
		else:
			return False


	# Already completed function!
	def get_table(self):
		return self.table


	# Already completed function!
	def __str__(self):
		return str(self.table)




"""
# test cases
# Everything below MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run


def checker(expected, actual):
	if expected == actual:
		print("CORRECT!")
	else:
		print("expected " + str(expected) + ", but got " + str(actual))



test1 = hash_table(5)
test1.hash(9)
test1.hash(25)
test1.hash(10)
test1.hash(14)
expected1 = (25, 10, 14, None, 9)

checker(expected1, test1.get_table())




test2 = hash_table(8)
test2.hash(5)
test2.hash(30)
test2.hash(52)
test2.hash(95)
test2.hash(45)
expected2 = (45, None, None, None, 52, 5, 30, 95)

checker(expected2, test2.get_table())



test3 = hash_table(8)
print(test3.linear_probe(16,0))
print(test3.linear_probe(107,3))
test3.linear_probe("c",4)
test3.linear_probe("d",4)
test3.linear_probe("e",5)
test3.linear_probe("f",6)
test3.linear_probe("g",0)
test3.linear_probe("h",2)
print(test3.get_table())
"""
