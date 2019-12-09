#================================
# Author: dreguera@mondragon.edu
# version: 0.1
#================================
# -*- coding: utf-8 -*-

import csv
import datetime
import time
import os
import argparse
import random
from csv import reader
from influxdb import client as influxdb

from datetime import datetime
from dateutil.parser import parse
import pandas as pd

def read_data():
    with open(filename) as f:
        return [x.split(';') for x in f.readlines()[1:]]


database = "macc_db" #nombre de tu database de InlfuxDB
host = "localhost"
filename = "data2.csv" #nombre del csv (Cambia a punto el separador decimal)

a = read_data() 


for metric in a:

	influx_metric = [{
		'measurement' : 'macc_measurement', # aqui le metes el nombre a la tabla
        'time' :  pd.to_datetime(datetime.now()),  #formato datetime para grafana
        'fields' : {
        'theta': metric [0], # creas el campo y le metes el valor
        'id' : metric [1],
        'iq' : metric[2],
        'f' : metric[3]
        }
    }]
    db = influxdb.InfluxDBClient(host=host, port=8086, database=database)
    db.create_database(database)
    db.write_points(influx_metric)

