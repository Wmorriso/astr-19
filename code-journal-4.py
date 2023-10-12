import json

class Jaguar:

	facts = {"Arm length" : 28.15, "Leg length" : 28.15, "Number of Eyes" : 2,}

	print(json.dumps(facts, indent = 2))

	t = 1
	l = 1

	print("Does it have a tail", t==l)
	print("Is it's tail fluffy", t==l)


