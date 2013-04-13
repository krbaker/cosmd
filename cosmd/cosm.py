#!/usr/bin/python
# based on http://www.netfluvia.org/layer8/?p=175
 
import urllib2
import json
 
class Cosm:
 
  _url_base = "http://api.cosm.com/v2/feeds/"
  _feed_id = None
  _version = None
  ## the substance of our update - list of dictionaries with keys 'id' and 'current_value'
  _data = None
  ## the actual object we'll JSONify and send to the API endpoint
  _payload = None
  _opener = None
 
  def __init__(self, feed_id, apikey):
    self._version = "1.0.0"
    self._feed_id = feed_id
    self._opener = urllib2.build_opener()
    self._opener.addheaders = [('X-PachubeApiKey',apikey)]
    self._data = []
    self._payload = {}
 
  def addDatapoint(self,dp_id,dp_value):
    self._data.append({'id':dp_id, 'current_value':dp_value})
 
  def buildUpdate(self):
    self._payload['version'] = self._version
    self._payload['id'] = self._feed_id
    self._payload['datastreams'] = self._data
 
  def sendUpdate(self):
    url = self._url_base + self._feed_id + "?_method=put"
    self._opener.open(url,json.dumps(self._payload)).read()
    self._data = []
