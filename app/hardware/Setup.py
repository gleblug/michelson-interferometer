from re import error
import numpy as np

from time import sleep
from datetime import datetime

from Gpib import Gpib

class Setup:
	def __init__(self) -> None:
		self.amp = Gpib("amperm")
		self.ps = Gpib("ps")
		self.configureAmp()
		self.configurePs()

		self.data = []

	def __del__(self):
		self.amp.write("*RST")
		self.ps.write("VSET 0")

	def configureAmp(self, int_time = 0.1):
		buffer = f"""
			configure:current:dc
    		format:elements reading
    		display:digits 7
    		current:dc:nplcycles {int_time * 50.0}
			"""
		self.amp.write(buffer)

	def configurePs(self):
		self.ps.write("VSET 0")

	def setVoltage(self, voltage):
		self.ps.write(f"VSET {voltage}")

	def getCurrent(self):
		self.amp.write("READ?")
		try:
			value = str(self.amp.read())[2:-3]
			return float(value)
		except error as e:
			print(f"Error {e.msg}")
		return None

	def getVoltage(self):
		self.ps.write("VSET?")
		try:
			value = str(self.ps.read())[3:-5]
			return float(value)
		except error as e:
			print(f"Error {e.msg}")
		return None

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