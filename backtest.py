# Author: Matthew Mills
# Copyright 2016

# Backtester

# Import date and time
from datetime import date, timedelta as td

# Import for oracle
from marketPriceOracle import PriceOracle
from webAPIOracle import WebAPIOracle

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

	
	MongoClientAddress = 
	MongoPort = 

	oracle = PriceOracle(MongoClientAddress, MongoPort)

	poloniexAPI = WebAPIOracle("https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start=1445061607&end=9999999999&period=7200")

	cfdTest = CFDTests()

	#Ethereum Tests
	cfdTest.cfdPerformanceTest('2016-09-17', '2016-10-17', oracle, 
								'poloniex_trade', 'ETH_USD', 2, 2, 'Ethereum')

	#cfdTest.findOptimalMargin('2016-09-17', '2016-10-17', oracle, 
								#'poloniex_trade', 'ETH_USD', 'Ethereum', 3.6)

	print("Tests completed")



	
if __name__ == "__main__": main()
