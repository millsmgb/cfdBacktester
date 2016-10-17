# Author: Matthew Mills
# Copyright 2016

# This is the CFD specific test class, where all tests are conducted on the CFD object
# Separated out from the main method for clarity and ability to call multiple types of tests
# also separate as may want to run different tests for different financial products down the line

# Import date and time
from datetime import datetime, timedelta as td

# Import for oracle
from marketPriceOracle import PriceOracle

# Import CFD
from cfd import CFD

# Import Graphs
from graph import Graph

class CFDTests:


	def __init__(self):
		pass

	# Backtest cfd
	def backTest(self, oracle, cfd, db, collection, date):
		trades = oracle.getDocumentsByDate(db, collection, date)
		numTrades = trades.len()
		for trade in trades:
			if (cfd.isTerminated == False):
				cfd.mark(float(trade['rate']))
				return numTrades
			else:
				print("Contract terminated")
				break

	# Performance test for a single pass of a CFD backtested between two dates
	def cfdPerformanceTest(self, startDate, endDate, oracle, 
							db, collection, initialShortMargin, initialLongMargin, currency):
		# Time line for dates
		timeline = []
		
		# Track profits for each position
		shortProfit = []
		longProfit = []

		# Track total margins for each position
		shortMargin = []
		longMargin = []

		# Track price of underlying asset
		ethPrice = []

		# Track returns of underlying asset
		ethReturns = []

		numTransactions = 0

		# Set up CFD
		firstTrade = oracle.getOneDocumentByDate(db, collection, startDate)

		testCFD = CFD(initialLongMargin, initialShortMargin, float(firstTrade['rate']))

		# Set initial price
		initialPrice = testCFD.price
		prevPrice = initialPrice
		print("Initial price: " + str(testCFD.price))
		print("Initial long margin: " + str(testCFD.marginLong))
		print("Initial short margin: " + str(testCFD.marginShort))

		# Set start and end dates in YYYY-
		d1 = datetime.strptime(startDate, '%Y-%m-%d').date()
		d2 = datetime.strptime(endDate, '%Y-%m-%d').date()

		delta = d2 - d1

		# Perform backtest between dates
		for i in range(delta.days + 1):
			# Check if contract has terminated, if so break early
			if (testCFD.isTerminated == True):
				print("Final day: " + str((d1 + td(days = i))))
				break

			numTransactions += self.backTest(oracle, testCFD, db, collection, str((d1 + td(days = i))))

			# Gather results
			timeline.append(d1 + td(days = i))

			# Profit Results
			shortProfit.append(initialPrice - testCFD.price)
			longProfit.append(testCFD.price - initialPrice)

			# Current Margin
			shortMargin.append(testCFD.marginShort)
			longMargin.append(testCFD.marginLong)

			# Current ETH Price
			ethPrice.append(testCFD.price)

			# Current return
			ethReturns.append((testCFD.price - prevPrice) -1)

			# Set previous price
			prevPrice = testCFD.price

		# Final margins
		print("Final long margin: " + str(testCFD.marginLong))
		print("Final short margin: " + str(testCFD.marginShort))
		print("Final number of Transactions: " + str(numTransactions))

		# Set multiline chart dicts
		profits = []
		profits.append(shortProfit)
		profits.append(longProfit)

		margins = []
		margins.append(shortMargin)
		margins.append(longMargin)


		# Set legends
		profitsLegend = ['Short Profit', 'Long Profit']
		marginsLegend = ['Short Margin', 'Long Margin']


		# Generate Graphs
		results = Graph()

		results.plotSimpleLineChart(timeline, ethPrice, 'Price of ' + currency + ' over Time',
											'Time (date)', 'Price ($USD)')

		results.plotMultiLineChart(timeline, profits, 'Profits over Time',
									profitsLegend, 'Time (date)', 'Profit ($USD)')

		results.plotMultiLineChart(timeline, margins, 'Margins over Time',
									marginsLegend, 'Time (date)', 'Margin Amount ($USD)')

		results.plotSimpleLineChart(timeline, ethReturns, currency + ' Returns over Time',
									'Time (date)', 'Returns (decimal return)')

		#results.plotHistogram(ethReturns, 'Frequency of ' + currency + ' Returns', 
		#						'Returns', 'Frequency')

		results.plotPDFHistogram(ethReturns, 'Probability Density Function of ' + currency + ' Returns', 
								'Returns', 'Probability Density')

		results.close()

	# Find optimal margin 
	def findOptimalMargin(self, startDate, endDate, oracle, db, collection, currency, startingMargin):
		margin = []
		days = []

		marginAmount = startingMargin

		while (marginAmount > 0):
			print("Margin amount: " + str(marginAmount))
			# Set up CFD
			firstTrade = oracle.getOneDocumentByDate(db, collection, startDate)

			testCFD = CFD(marginAmount, marginAmount, float(firstTrade['rate']))

			# Set initial price
			initialPrice = testCFD.price
			

			# Set start and end dates in YYYY-
			d1 = datetime.strptime(startDate, '%Y-%m-%d').date()
			d2 = datetime.strptime(endDate, '%Y-%m-%d').date()

			delta = d2 - d1

			totalDays = 0

			# Perform backtest between dates
			for i in range(delta.days + 1):
				# Check if contract has terminated, if so break early
				if (testCFD.isTerminated == True):
					print("Final day: " + str((d1 + td(days = i))))
					break

				self.backTest(oracle, testCFD, db, collection, str((d1 + td(days = i))))
				totalDays = totalDays + 1

			margin.append(marginAmount)
			days.append(totalDays)
			marginAmount = marginAmount - 0.1

		result = Graph()

		result.plotSimpleLineChart(margin, days, 'Time to liquidation for ' + currency,
									'Margin Amounts ($USD)', 'Days to liquidation')

		result.show()

		result.close()


		