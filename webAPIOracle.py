# Author: Matthew Mills
# Copyright 2016

# The purpose of this class is to provide the pricing oracle required to feed market data
# We write this in a similar fashion to how it would operate in Ethereum
# Hence the constructor initiates the oracle, which then refreshes when told

# ---

# This is the oracle to interface with Poloniex's API

# Imports for JSON

import json

# Imports for API Response

import urllib.request as ur

import time

class WebAPIOracle:
	'The pricing oracle class used to pull live market data'

	def __init__(self, url):
		try:
			response = ur.urlopen(url).read()
			self.data = json.loads(response.decode('utf-8'))
			print("JSON data loaded")
			self.processJSON(self.data)
			print("JSON processed")

		except Exception as e:
			print(str(e))

	def processJSON(self, data):
		for item in data:
			item['date'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['date']))
			item['rate'] = item['weightedAverage']
		
	
	def updateURL(self, url):

		try:
			response = urllib2.urlopen(url)
			self.data = json.load(response)
			print("JSON data loaded")

		except Exception as e:
			print(str(e))
	
	def getDocumentsByDate(self, db, collection, date):
		
		trades = []
		for item in self.data:
			if (date in item['date']):
				trades.append(item)

		return trades

	def getOneDocumentByDate(self, db, collection, date):
		for item in self.data:
			if (date in item['date']):
				return item

		return 