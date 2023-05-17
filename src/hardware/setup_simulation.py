import numpy as np
from time import sleep
from datetime import datetime
from random import random

class SetupSimulation:
	def run(self, from_v, to_v, count_v, data, status):
		print(f'run with {from_v} {to_v} {count_v} params')
		status.value = True
		for u in np.linspace(from_v, to_v, count_v):
			voltage = u
			current = random() * 1e-6

			data.append((voltage, current))
			print(data[-1])
			sleep(1)

		filename = rf"files/data_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
		np.savetxt(filename, data, delimiter=",", header="voltage,current", comments="")
		status.value = False