#Import MatPlotLib 

from matplotlib import pyplot as plt

#Import Numpy for data manipulation

import numpy as np

#Import SciPy

import scipy.stats as stats

#Import OS functions for checking if file directory exists
import os
import errno

class Graph:

	def __init__(self):
		self.numFigures = 1
		

	def plotSimpleLineChart(self, x, y, title, labelX, labelY):
		plt.figure(self.numFigures)

		plt.plot(x, y, linewidth=1.0)

		plt.title(title)

		plt.grid(True)

		self.numFigures = self.numFigures + 1

		self.save(title)

	def plotMultiLineChart(self, x, y, title, legend, labelX, labelY):
		plt.figure(self.numFigures)
		legendNum = 0

		for key in y:
			plt.plot(x, y[key], label=legend[legendNum], linewidth=1.0)
			legendNum = legendNum + 1

		plt.title(title)

		plt.ylabel(labelY)
		plt.xlabel(labelX)

		plt.legend()

		plt.grid(True)

		self.numFigures = self.numFigures + 1

		self.save(title)

	def plotHistogram(self, x, title, labelX, labelY):
		plt.figure(self.numFigures)

		x.sort()

		plt.hist(x)

		plt.title(title)

		plt.ylabel(labelY)
		plt.xlabel(labelX)
		plt.grid(True)

		self.save(title)

	def show(self):
		plt.show()

	def save(self, title):
		try:
			plt.savefig('./results/'+title + '.png')
		except FileNotFoundError:
			try: 
				os.makedirs('./results')
			except OSError:
				if not os.path.isdir(path):
					raise

	def close(self):
		plt.close()
		self.numFigures = 0