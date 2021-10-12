# function name: to_decimal
# input: num (a non-negative non-decimal int as string)- ex: 11101, 7712, ABC
		#base (the number system you're converting from as an int)- ex: 2, 8, 16
# output: decimal representation of num AS INTEGER 
# restrictions: you are NOT allowed to use the Python int function
				# that will convert it to decimal for you. You should use
				# implement the algorithm discussed in class
# assumptions: num will always be non-negative
			#  num will always be a valid number ex: 31112 (base2) won't be an input
			#. if num has letters, they will always be capitalized
			#  base will be 2, 8, or 16
def to_decimal(num: str, base: int) -> int:
	#check(5, to_decimal('101', 2)), given 101. base value 2
	if(base != 2 and base != 8 and base != 16):
		print("Please provide a valid base. (2,8,16)")
		return None

	j = len(num)-1
	sum = 0
	for i in range (0 , len(num)):
		#	1[0]	0[1]	1[2]: 0 to num.len
		#	(base)^[2]	(base)^[1]	(base)^[0]: num.len to 0

		# 0 - 9
		if(num[i] == "0"):
			temp = 0*(base**j)
		elif (num[i] == "1"):
			temp = 1 * (base ** j)
		elif(base == 8 or base == 16):
			if (num[i] == "2"):
				temp = 2 * (base ** j)
			elif (num[i] == "3"):
				temp = 3 * (base ** j)
			elif (num[i] == "4"):
				temp = 4 * (base ** j)
			elif (num[i] == "5"):
				temp = 5 * (base ** j)
				#print("5 works")
			elif (num[i] == "6"):
				temp = 6 * (base ** j)
			elif (num[i] == "7"):
				#print("7 works")
				temp = 7 * (base ** j)
			#Hexadecimal System
			elif(base == 16):
				if (num[i] == "8"):
					temp = 8 * (base ** j)
				elif (num[i] == "9"):
					temp = 9 * (base ** j)
				# A - F
				elif (num[i] == "A"):
					#print("A works!")
					temp = 10 * (base ** j)
				elif (num[i] == "B"):
					temp = 11 * (base ** j)
				elif (num[i] == "C"):
					temp = 12 * (base ** j)
				elif (num[i] == "D"):
					temp = 13 * (base ** j)
				elif (num[i] == "E"):
					temp = 14 * (base ** j)
				elif (num[i] == "F"):
					temp = 15 * (base ** j)
		else:
			print("Please fill in a number with valid digits for your chosen base.")
			print("2: (0-9), 8: (0-7), 16: (0-9,A-F)")
			return None
		#print("Temp: ", temp, "		w/o base: ", temp/(base**j))
		sum += temp
		j -= 1
		#print("Sum of i(", i, "): ", sum)
	return sum




# funtion name: to_base
# input: dec_num (a positive decimal integer)- ex: 1, 6, 10, 68, 102...
		#base (the number system you're converting to as an int)- ex: 2, 8, 16
# output: non-base-10 representation of dec_num AS STR
# restrictions: you are NOT allowed to use the Python int function
				# that will convert it for you. You should use
				# implement the algorithm discussed in class
# assumptions: dec_num will always be non-negative
			#  base will be 2, 8, or 16				
def to_base(dec_num: int, base: int) -> str:
	#check('1111011', to_base(123, 2))
	#Division eq+ a = dq + r
	valid = True
	newNum = ""
	#i = 0
	while(valid):
		#i+= 1
		d = dec_num//base
		r = dec_num-(d*base)
		#print("Interation: ", i, "d: ", d, "r: ", r,)
		if (r == 0):
			newNum = "0" + newNum
		elif (r == 1):
			newNum = "1" + newNum
		elif (base == 8 or base == 16):
			if (r == 2):
				newNum = "2" + newNum
			elif (r == 3):
				newNum = "3" + newNum
			elif (r == 4):
				newNum = "4" + newNum
			elif (r == 5):
				newNum = "5" + newNum
			elif (r == 6):
				newNum = "6" + newNum
			elif (r == 7):
				newNum = "7" + newNum
			# Hexadecimal System
			elif (base == 16):
				if (r == 8):
					newNum = "8" + newNum
				elif (r == 9):
					newNum = "9" + newNum
				# A - F
				elif (r == 10):
					newNum = "A" + newNum
				elif (r == 11):
					newNum = "B" + newNum
				elif (r == 12):
					newNum = "C" + newNum
				elif (r == 13):
					newNum = "D" + newNum
				elif (r == 14):
					newNum = "E" + newNum
				elif (r == 15):
					newNum = "F" + newNum
		else:
			print("This statement shouldn't run. If it runs...")
			print("There is an error.")
			return None
		#Run this if statement last, to ensure the final remainder gets counted.
		if(dec_num//(base)==0):
			valid = False
		dec_num = d
	#print("newNum: ", newNum)
	return newNum




'''
# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
def check(expected, yours):
	if type(expected) != type(yours):
		print("your data type is", type(yours), "but should be", type(expected))
		return
	if expected == yours:
		print("CORRECT")
	else:
		print("INCORRECT: expected", expected, "but got", yours)

check(5, to_decimal('101', 2))
check(14, to_decimal('1110', 2))
check(418, to_decimal('642', 8))
check(738, to_decimal('1342', 8))
check(101, to_decimal('65', 16))
check(1402, to_decimal('57A', 16))


check('1111011', to_base(123, 2))
check('110010000', to_base(400, 2))
check('6540', to_base(3424, 8))
check('12134', to_base(5212, 8))
check('4027', to_base(16423, 16))
check('3E5F', to_base(15967, 16))
'''





