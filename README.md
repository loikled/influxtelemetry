# Influx Telemetry

This is a proof of concept of sending telemetry data to an influx database and
fetching it back using python client.

# Prerequisites

1. Having docker and docker-compose installed
   The recommended way is to install from docker ppa.

2. Downloading and run the influxDB sandbox from https://github.com/influxdata/sandbox

# Installing

This test works with python3.
You should have pip installed for python3.
On ubuntu 18.04:
`sudo apt-get install python3-pip`

Then install the python dependencies:
`pip3 install -r requirements.txt`


# Running the test

This test is in two parts:
* Sending some time series data to the database

`python3 send_data.py`

* Fetching and displaying the data from the database
`python3 displat_data.py`

You should see a plot of a sinus wave open if everything worked.

