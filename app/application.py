from app.hardware import SetupSimulation as Setup
# from app.hardware import Setup
from app.web import Server

def mainpage():
	return '<p>Main page</p>'

class App():
	def __init__(self) -> None:
		self.setup = Setup()
		self.server = Server()
		self.configureServer()

	def configureServer(self):
		self.server.add_endpoint('/', 'mainpage', mainpage)

	def run(self):
		self.server.run()