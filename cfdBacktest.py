# Author: Matthew Mills
# Copyright 2016

# Purpose of this python file is to simulate the operations of a CFD as if it were written as a smart contract
# Note network difficulty, block times, and gas/transaction costs are not taken into account

class CFD:
	def __init__(self):
		self.marginLong = 10000
		self.marginShort = 10000
		self.price = 0
		self.isTerminated = False

	def __init__(self, marginLong, marginShort, currPrice):
		self.marginLong = marginLong
		self.marginShort = marginShort
		self.price = currPrice

	def mark(self, currPrice): # Mark the margin accounts based on new price information
		priceDiff = (currPrice - self.price)

		if (self.marginShort <= priceDiff):
			liquidateShort(self)

		else if (self.marginLong <= priceDiff):
			liquidateLong(self)

		else:
			self.marginShort = self.marginShort - priceDiff
			self.marginLong = self.marginLong + priceDiff
			self.price = currPrice

	def liquidateShort(self):
		self.marginLong = self.marginLong + self.marginShort
		self.marginShort = 0
		self.isTerminated = True
	
	def liquidateLong(self):
		self.marginShort = self.marginShort + self.marginLong
		self.marginLong = 0
		self.isTerminated = True
	
