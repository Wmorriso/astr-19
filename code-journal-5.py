import numpy as np
import sys



class jaguar:

	def __init__(self, arms, legs, eyes, tail, furry):
		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.furry = furry

	def discribe(self):
		print("My favorite animal is a Jaguar")
		print(f"It's arm length is = {self.arms}")
		print(f"It's leg legth is = {self.legs}")
		print(f"It's amount of eyes is = {self.eyes}")
		if self.tail:
			print("Does it have a tail?: Yes")
		else:
			print("Does it have a tail?: No")
		if self.furry:
			print("Is the tail furry?: Yes")
		else:
			print("Is the tail furry?: No")


	#arms = 28.15
	#legs = 28.15
	#eyes = 2
	#tail = True
	#furry = True

Animal = jaguar(28.15, 28.15, 2, True, True)

Animal.discribe()