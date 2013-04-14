#!/usr/bin/python
# Quick Library to Fetch Data from TED

from pysnmp.entity.rfc3413.oneliner import cmdgen
import time

class DataSource:
    def __init__(self, config):
        self.oids = []
        self.host = config["host"]
        self.community = config["community"]
        for oid in config["oids"]:
            self.oids.append(Oid(oid,
                                 self.host,
                                 self.community,
                                 config["oids"][oid]["name"],
                                 config["oids"][oid]["type"]))

    def update(self, cosm):
        for oid in self.oids:
            oid.update()
            if oid.value:
                cosm.addDatapoint(oid.name,oid.value)

class Oid:
    def __init__(self, oid, host, community, name, measure_type):
        self.host = host
        if oid.startswith("."):
            oid = oid[1:]
        self.oid = tuple([ int(i) for i in oid.split(".") ])
        self.community = community
        self.name = name
        self.type = measure_type
        self.data = None
        self.time = None
        self.last_data = None
        self.last_time = None
        self.value = None
        if self.type == "counter":
            self.update()

    def update(self):
        if self.type == "counter":
            self.time = time.time()
            self.data = self.getData()
            if self.last_time and self.last_data:
                self.value = (self.data - self.last_data) / (self.time - self.last_time) 
            self.last_time = self.time
            self.last_data = self.data
        else:
            self.value = self.getData()
        
    def getData(self):
        errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().getCmd(
            cmdgen.CommunityData('cosmd', self.community, 1),
            cmdgen.UdpTransportTarget((self.host, 161)),
            (self.oid)
            )
        return varBinds[0][1]._value
    
