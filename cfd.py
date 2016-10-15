# Author: Matthew Mills
# Copyright 2016

# Purpose of this python file is to simulate the operations of a CFD as if it were written as a smart contract
# Note network difficulty, block times, and gas/transaction costs are not taken into account

class CFD: # CFD Class handles all the contract requirements

	def __init__(self): # Base constructor
		self.marginLong = 10000
		self.marginShort = 10000
		self.price = 0
		self.isTerminated = False

	def __init__(self, marginLong, marginShort, currPrice): # Constructor for a new contract
		self.marginLong = marginLong
		self.marginShort = marginShort
		self.price = currPrice
		self.isTerminated = False

	def liquidateShort(self): # If the short position is insufficient, liquidate it
		self.marginLong = self.marginLong + self.marginShort
		self.marginShort = 0
		self.isTerminated = True
	
	def liquidateLong(self): # If the long position is insufficient, liquidate it
		self.marginShort = self.marginShort + self.marginLong
		self.marginLong = 0
		self.isTerminated = True
	
	def mark(self, currPrice): # Mark the margin accounts based on new price information
		priceDiff = (currPrice - self.price) # Calculate change in price to mark

		if (self.marginShort <= priceDiff): # Liquidate contract if insufficient margin
			print("Liquidating short position")
			self.liquidateShort()

		elif (self.marginLong <= priceDiff): # As above
			print("Liquidating long position")
			self.liquidateLong()

		else: # Sufficient margin in the account, therefore mark to market
			self.marginShort = self.marginShort - priceDiff
			self.marginLong = self.marginLong + priceDiff
			self.price = currPrice
