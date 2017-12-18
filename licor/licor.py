'''
Created on 01.06.2017
@author: oliver
'''
import serial
import time
import xml.etree.ElementTree as et
from xml.etree.ElementTree import ParseError
from serial import SerialException
import sys
import logging

log = logging.getLogger(__name__)

class Li820():
    def __init__(self, port):
        """
        @param port: Port name like COM1 on Windows or /dev/ttyUSB0 on Linux      
        """ 
        self.port = port
        
    def connect(self):
        log.debug("Connect port:{}".format(self.port))
        self.com = serial.Serial(port=self.port, baudrate=9600,parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)

    def disconnect(self):
        log.debug("Disonnect port:{}".format(self.port))
        try:
            self.com.close()
        except SerialException as e:
           log.error(str(e)) 
    
    def readData(self):
        """Reads data in blocking mode. Returns a dictionary containing channel name,value pairs."""
        res = {}
        try:    
            res = XMLParser.parse(self.__read(),'data')     
        except SerialException as e:
            log.error(str(e))
        return res
        
    # Private methods
    def __read(self):
        """Reads in blocking mode, returns a string"""
        buf = ''     
        while True:
            c = self.com.read()            
            if c == '\n':               
                if buf.startswith("<li820>") and buf.endswith("</li820>\r"):
                    return buf
                else:
                    buf = ''
            else:
                buf += c     

class XMLParser():
    @staticmethod
    def parse(xml,tag):
        resp = {}
        try:
            root = et.fromstring(xml)
            for obs in root.find(tag):
                if obs.tag == "raw":
                    resp[obs.tag] = obs.text
                else:
                    resp[obs.tag] = float(obs.text)                        
        except ParseError as e:            
            log.error("Code:" + str(e.code) + " pos:" + str(e.position) + " xml:" + str(xml))
        return resp

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    li = Li820("/dev/ttyUSB0")
    try:
        li.connect()
        while True:
            print(li.readData())    
    except KeyboardInterrupt:
        li.disconnect()
    
    
