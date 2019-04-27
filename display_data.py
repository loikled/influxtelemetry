#!/usr/bin/python3

from influxdb import InfluxDBClient
import numpy as np
import time
import pyqtgraph as pg
from PyQt5 import QtGui

S2NS=1000000000
DBNAME = 'telemetry'

def get_data():
	client = InfluxDBClient('localhost', 8086, 'root', 'root', DBNAME)
	client.switch_database(DBNAME)
	query = 'SELECT kneePosition FROM motor_positions'
	print("Querying data: " + query)
	result = client.query(query, database=DBNAME)
	points = list(result.get_points())
	y = []
	for p in points:
		y.append(p['kneePosition'])
	return y

def main():
	app = QtGui.QApplication([])
	data = get_data()
	plot = pg.PlotWidget()
	plot.plot(data)
	plot.show()

	app.exec_()

if __name__ == '__main__':
	main()

