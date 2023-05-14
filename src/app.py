from flask import Flask, render_template
import plotly.express as px
import plotly
import json
import pandas as pd

from hardware import SetupSimulation as Setup
# from hardware import Setup


app = Flask(__name__)
setup = Setup()

@app.route('/')
def runpage_handler():
	df = pd.DataFrame({
		"Voltage": [1, 2, 3, 4, 5, 6],
		"Current": [10, 15, 8, 5, 14, 25],
	})
	
	fig = px.line(df, x="Voltage", y="Current")

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	header="Dependence"

	return render_template('index.html', graphJSON=graphJSON, header=header)
