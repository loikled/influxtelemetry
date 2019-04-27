#!/usr/bin/python3

from influxdb import InfluxDBClient
import numpy as np
import time
import datetime
import math

S2NS=1000000000
MS2NS=1000000
DBNAME = 'telemetry'

def create_point(field, timestamp, value):
	data = {}
	data["measurement"] = "motor_positions"
	data["tags"] = {"session_id": "12", "exo_version" : "v5-4"}
	data["time"] = timestamp
	data["fields"] = {field : value}
	return data

def create_curve(duration_hours=1.0):
	""" Generate a sin wave with a sampling of 1ms, for given duration.
	"""
	nb_points_ms = duration_hours*3600*1000
	max_val = 2.0 * math.pi
	interval = max_val / nb_points_ms
	y = np.sin(np.arange(0, max_val, interval))
	start_time = int(time.time() * S2NS) - len(y) * MS2NS
	x = np.arange(start_time, start_time + len(y) * MS2NS, MS2NS)
	return x, y

def main():
	# Parameters: InfluxDBClient(host, port, USER, PASSWORD, DBNAME)
	client = InfluxDBClient('localhost', 8086, 'root', 'root', DBNAME)
	print("Clear database: " + DBNAME)
	client.drop_database(DBNAME)
	client.create_database(DBNAME)
	client.switch_database(DBNAME)
	points = []
	x, y = create_curve(0.01)

	for xi,yi in zip(x,y):
		p = create_point("kneePosition", xi, yi)
		points.append(p)

	span = 10000
	for i in range(0, len(x), span):
		client.write_points(points[i:i+span])
		print("sending points from {} to {}".format(i, i + span))

if __name__ == '__main__':
	main()

