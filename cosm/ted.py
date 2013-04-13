#!/usr/bin/python
# Quick Library to Fetch Data from TED

from xml.dom.minidom import parseString
import urllib2

class DataSource:
    def __init__(self, config):
        self.names = config["names"]
        self.ted = Ted(config["host"])

    def update(self, cosm):
        self.ted.update()
        cosm.addDatapoint(self.names["Watts"], self.ted.getWatts())
        cosm.addDatapoint(self.names["Volts"], self.ted.getVolts())

class Ted:
    def __init__(self, host):
        self.host = host
        self.data = None

    def update(self):
        self.data = parseString(urllib2.urlopen("http://%s/api/LiveData.xml" % self.host,
                                                timeout = 10).read())

    def getData(self):
        return self.data

    def getWatts(self):
        for node in self.data.getElementsByTagName("Power")[0]\
            .getElementsByTagName("Total")[0]\
            .getElementsByTagName("PowerNow")[0].childNodes:
            if node.nodeType == node.TEXT_NODE:
                return float(node.data)

    def getVolts(self):
        for node in self.data.getElementsByTagName("Voltage")[0]\
            .getElementsByTagName("Total")[0]\
            .getElementsByTagName("VoltageNow")[0].childNodes:
            if node.nodeType == node.TEXT_NODE:
                return float(node.data)/10
    
