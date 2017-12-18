'''
Created on 01.06.2017
@author: oliver
'''
import unittest
from licor import Li820


class LicorReadTest(unittest.TestCase):    
    
    def setUp(self):
        self.dev = Li820("COM23")
        self.dev.connect()
        
    def tearDown(self):
        self.dev.disconnect()

    def testReadData(self):        
        while True:
            print self.dev.readData()


            
if __name__ == "__main__":
    unittest.main()
