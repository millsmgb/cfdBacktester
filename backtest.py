# Author: Matthew Mills
# Copyright 2016

# Backtester

# Import date and time
from datetime import date, timedelta as td

# Import for oracle
from marketPriceOracle import PriceOracle

# Import CFD
from cfd import CFD

# Import Tests
from cfdTests import CFDTests

# Main method

def main():

	# Output to graph
	x = []
	shortResults= []
	longResults = []

	
	MongoClientAddress = "43.243.203.47"
	MongoPort = "12347"

	oracle = PriceOracle(MongoClientAddress, MongoPort)

	cfdTest = CFDTests()

	#Ethereum Tests
	cfdTest.cfdPerformanceTest('2016-09-15', '2016-10-15', oracle, 
								'poloniex_trade', 'ETH_USD', 3, 3, 'Ethereum')

	print("Tests completed")



	
if __name__ == "__main__": main()
