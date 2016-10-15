# Author: Matthew Mills
# Copyright 2016

# Backtester

# Import date and time
from datetime import date, timedelta as td

# Import for oracle
from marketPriceOracle import PriceOracle

# Import CFD
from cfd import CFD

def backTest(oracle, cfd, db, collection, date):

	trades = oracle.getDocumentsByDate(db, collection, date)
	
	print("Margin - Long position: " + str(cfd.marginLong))
	print("Margin - Short position: " + str(cfd.marginShort))

	for trade in trades:
		if (cfd.isTerminated == False):
			print("Current Price: $" + trade['rate'])
			cfd.mark(float(trade['rate']))
			print("Margin - Long position: " + str(cfd.marginLong))
			print("Margin - Short position: " + str(cfd.marginShort))
		else:
			print("Contract terminated")
			break

# Main method

def main():
	
	MongoClientAddress = 
	MongoPort = 

	oracle = PriceOracle(MongoClientAddress, MongoPort)

	firstTrade = oracle.getOneDocumentByDate('poloniex_trade', 'ETH_USD', '2016-09-15')
	
	testCFD = CFD(2.475, 2.475, float(firstTrade['rate']))

	print("Initial price: " + str(testCFD.price))
	print("Initial long margin: " + str(testCFD.marginLong))
	print("Initial short margin: " + str(testCFD.marginShort)) 

	d1 = date(2016, 9, 15)
	d2 = date(2016, 10, 15)

	delta = d2 - d1

	for i in range(delta.days + 1):

		if (testCFD.isTerminated == True):
			print("Final day: " + str((d1 + td(days=i))))
			break

		backTest(oracle, testCFD, 'poloniex_trade', 'ETH_USD', str((d1 + td(days=i))))


	
	print("Final long margin: " + str(testCFD.marginLong))
	print("Final short margin: " + str(testCFD.marginShort)) 

	
if __name__ == "__main__": main()
