from flask import Flask
from flask_cors import CORS
from markupsafe import escape
import plotly.express as px
import plotly
import json
import pandas as pd

from multiprocessing import Manager, Process

from hardware import setup
# from hardware import Setup


app = Flask(__name__)
CORS(app)
mgr = Manager()
data = mgr.list()
status = mgr.Value('b', False)


@app.route('/data', methods=['GET'])
def get_data():
	df = pd.DataFrame(list(data), columns=['Voltage', 'Current'])
	fig = px.line(df, x='Voltage', y='Current')

	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

@app.route('/run', methods=['GET'])
@app.route('/run_from:<from_v>_to:<to_v>_count:<count_v>', methods=['GET'])
def run_setup(from_v=0, to_v=5, count_v=10):
	if not status.value:
		while data:
			data.pop()
		p = Process(target=setup.run, args=(
			float(escape(from_v)),
			float(escape(to_v)),
			int(escape(count_v)),
			data, 
			status))
		p.daemon = True
		p.start()

	return str(status.value)