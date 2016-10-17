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

		plt.xticks(rotation='vertical')

		plt.title(title)

		plt.ylabel(labelY)
		plt.xlabel(labelX)

		plt.grid(True)

		self.numFigures = self.numFigures + 1

		self.save(title)

	def plotMultiLineChart(self, x, y, title, legend, labelX, labelY):
		plt.figure(self.numFigures)

		i = 0
		for index in y:
			plt.plot(x, y[i], label=legend[i], linewidth=1.0)
			i = i + 1

		plt.xticks(rotation='vertical')

		plt.title(title)

		plt.ylabel(labelY)
		plt.xlabel(labelX)


		plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

		plt.grid(True)

		self.numFigures = self.numFigures + 1

		self.save(title)

	def plotHistogram(self, x, title, labelX, labelY):
		plt.figure(self.numFigures)

		x.sort()

		plt.xticks(rotation='vertical')
		plt.hist(x)

		plt.title(title)

		plt.ylabel(labelY)
		plt.xlabel(labelX)
		plt.grid(True)



		self.save(title)

	def plotPDFHistogram(self, x, title, labelX, labelY):
		plt.figure(self.numFigures)

		x.sort()

		plt.xticks(rotation='vertical')

		fit = stats.norm.pdf(x, np.mean(x), np.std(x)) 

		print("mean is: " + str(np.mean(x)))
		print("Standard Deviation is: " + str(np.std(x)))
		plt.plot(x,fit,'-o')

		plt.hist(x, normed=True) 

		plt.title(title)

		plt.ylabel(labelY)
		plt.xlabel(labelX)
		plt.grid(True)

		self.save(title)

	def show(self):
		plt.show()

	def save(self, title):
		try:
			plt.savefig('./results/'+title + '.png', bbox_inches='tight')
		except FileNotFoundError:
			try: 
				os.makedirs('./results')
			except OSError:
				if not os.path.isdir(path):
					raise

	def close(self):
		plt.close()
		self.numFigures = 0