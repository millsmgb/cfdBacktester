# Author: Matthew Mills
# Copyright 2016

# Backtester

# Import for oracle
from marketPriceOracle import PriceOracle

# Import CFD
from cfd import CFD

# Main method

def main():
	
	MongoClientAddress = "43.243.203.47"
	MongoPort = "12347"

	oracle = PriceOracle(MongoClientAddress, MongoPort)

	trades = oracle.getDocumentsByDate('poloniex_trade', 'ETH_USD', '2016-10-15')
	
	testCFD = CFD(2, 2, float(trades[0]['rate']))

	print("Margin - Long position: " + str(testCFD.marginLong))
	print("Margin - Short position: " + str(testCFD.marginShort))

	for trade in trades:
		if (testCFD.isTerminated == False):
			print("Current Price: $" + trade['rate'])
			testCFD.mark(float(trade['rate']))
			print("Margin - Long position: " + str(testCFD.marginLong))
			print("Margin - Short position: " + str(testCFD.marginShort))
		else:
			print("Contract terminated")
			break
	
	print("Final long margin: " + str(testCFD.marginLong))
	print("Final short margin: " + str(testCFD.marginShort)) 

	
if __name__ == "__main__": main()
