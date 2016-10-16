#Import MatPlotLib 

from matplotlib import pyplot as plt

#Import Numpy for data manipulation

import numpy as np

class Graph:

	def __init__(self):
		pass
		

	def plotSimpleLineChart(self, x, y, title):
		
		plt.plot(x, y, linewidth=1.0)

		plt.title(title)

		plt.show()

	def plotMultiLineChart(self, x, y, title):
		
		plt.plot(x, y['shortResults'], label='short profit', linewidth=1.0)
		plt.plot(x, y['longResults'], label='long profit', linewidth=1.0)

		plt.title(title)

		plt.ylabel('Profit ($)')
		plt.xlabel('Day')

		plt.legend()

		plt.grid(True,color='k')

		plt.show()