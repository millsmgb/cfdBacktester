# Author: Matthew Mills
# Copyright 2016

# The purpose of this class is to provide the pricing oracle required to feed market data
# We write this in a similar fashion to how it would operate in Ethereum
# Hence the constructor initiates the oracle, which then refreshes when told

# ---

# Imports for JSON

import json

# Imports for MongoDB

from pymongo import MongoClient

class PriceOracle:
	'The pricing oracle class used to pull live market data'

	def __init__(self, client, port):
		try:
			self.client = MongoClient(client + ":" + port)
			print("MongoDB client connected")

		except Exception as e:
			print(str(e))
	
	def updateClient(self, client, port):

		try:
			self.client = MongoClient(client + ":" + port)
			print("MongoDB client updated")
		except Exception as e:
			print(str(e))
	
	def getDocumentsByDate(self, db, collection, date):
		db = self.client[db]
		collection = db[collection]

		trades = collection.find(
				{
					'date': {'$regex' : str(date) + ".*"}
				}
			)

		return trades

	def getOneDocumentByDate(self, db, collection, date):
		db = self.client[db]
		collection = db[collection]

		trades = collection.find_one(
				{
					'date': {'$regex' : str(date) + ".*"}
				}
			)

		return trades	

