from time import sleep
from Gpib import *

v = Gpib('amperm')

v.clear()

v.write('*IDN?')

sleep(1)

for i in range(0,10):
	print(v.read())