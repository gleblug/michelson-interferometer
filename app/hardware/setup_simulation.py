import numpy as np
from time import sleep
from datetime import datetime
from random import random

class SetupSimulation:
	def __init__(self) -> None:
		self.data = []

	def setVoltage(self, voltage):
		pass

	def getCurrent(self):
		return random() * 1e-6

	def getVoltage(self):
		return random() * 5

	def run(self):
		for u in np.linspace(0, 5, 250):
			self.setVoltage(u)
			sleep(1)
			voltage = self.getVoltage()
			current = self.getCurrent()

			self.data.append((voltage, current))
			print(self.data[-1])

		filename = f"data_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
		np.savetxt(filename, self.data, delimiter=",", header="voltage,current", comments="")