#starting input for the program
g = input('Choose a task: ')

def main():
	#definitions for all the functions the program will end up running	
	def add(h, j):
		return h + j

	def subtract(h, j):
		return h - j

	def mult(h, j):
		return h * j

	#different formulas for the program
	if g == "one":
		h = float(input("enter a float number: "))
		fun = input("enter a funtion: ")
		j = float(input("enter another float number: "))	


	if g == "two":
		h = int(input("enter an integer: "))
		fun = input("enter a funtion: ")
		j = int(input("enter another integer: "))
	

	if g == "three":
		h = float(input("enter a float number: "))
		fun = input("enter a function: ")
		j = int(input("enter an integer: "))

	#tells the code what to output when a funtion is choosen for one of the formulas
	if fun == "*":
		print(mult(h, j))
		l = (h * j)
		print(type(l))
	
	if fun == "-": 
		print(subtract(h, j))
		l = (h - j)
		print(type(l))

	if fun == "+": 
		print(add(h, j))
		l = (h + j)
		print(type(l))

if __name__ == "__main__":
	main()



