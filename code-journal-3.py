#defining the fuction
def f(x):
	return x**3 + 8

#main function
def main():
	x = 9 # defining the x in the function
	i = f(x) #making i = to the answer of the function

	print(i) #print answer

	#printing yay because the answer will be more than 27
	if i>27:
		print("YAY")

if __name__=="__main__":
	main()
