from flask import Flask

from hardware import SetupSimulation as Setup
# from hardware import Setup


app = Flask(__name__)

@app.route('/')
def mainpage_handler():
	return '<p>Main page</p>'
