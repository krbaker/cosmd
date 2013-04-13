#!/usr/bin/python
# Quick Library to Fetch Data from wx200

from xml.dom.minidom import parseString
import urllib2
import subprocess

class DataSource:
    def __init__(self, config):
        self.names = config["names"]
        self.wx200 = Wx200(config["host"])

    def update(self, cosm):
        self.wx200.update()
        cosm.addDatapoint(self.names["IndoorTemp"], self.wx200.in_temp)
        cosm.addDatapoint(self.names["OutdoorTemp"], self.wx200.out_temp)
        cosm.addDatapoint(self.names["IndoorHumidity"], self.wx200.in_humidity)
        cosm.addDatapoint(self.names["OutdoorHumidity"], self.wx200.out_humidity)
        cosm.addDatapoint(self.names["IndoorDewpoint"], self.wx200.in_dew)
        cosm.addDatapoint(self.names["OutdoorDewpoint"], self.wx200.out_dew)
        cosm.addDatapoint(self.names["LocalBarometric"], self.wx200.local_baro)
        cosm.addDatapoint(self.names["SeaLevelBarometric"], self.wx200.sea_baro)
        cosm.addDatapoint(self.names["GustDirection"], self.wx200.gust_dir)
        cosm.addDatapoint(self.names["GustSpeed"], self.wx200.gust_speed)
        cosm.addDatapoint(self.names["WindDirection"], self.wx200.wind_dir)
        cosm.addDatapoint(self.names["WindSpeed"], self.wx200.wind_speed)
        cosm.addDatapoint(self.names["Windchill"], self.wx200.windchill)
        cosm.addDatapoint(self.names["Rainfall"], self.wx200.rainfall)

class Wx200:
    def __init__(self, host):
        self.host = host

    def update(self):
        self.time, self.in_temp, self.out_temp, self.in_humidity, self.out_humidity, \
            self.in_dew, self.out_dew, self.local_baro, self.sea_baro, self.gust_dir, self.gust_speed, \
            self.wind_dir, self.wind_speed, self.windchill, self.rainfall, self.cumrain = subprocess.check_output(["wx200","-t",self.host]).split("\t")


    
