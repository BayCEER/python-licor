'''
Created on 01.06.2017
@author: oliver
'''
import unittest
from licor import XMLParser

class ParserTest(unittest.TestCase):
    
    def setUp(self):
       pass
    
    def tearDown(self):
       pass                

    def testParseDataValid(self):        
        data = XMLParser.parse("<li820><data><celltemp>5.1147003e1</celltemp><cellpres>9.7489833e1</cellpres><co2>5.1393213e2</co2><co2abs>7.6735558e-2</co2abs><ivolt>1.1903686e1</ivolt><raw>3453690,3438292</raw></data></li820>",'data')
        print(data)

    def testParseDataInvalid(self):        
        data = XMLParser.parse("<li820X><data><celltemp>5.1147003e1</celltemp><cellpres>9.7489833e1</cellpres><co2>5.1393213e2</co2><co2abs>7.6735558e-2</co2abs><ivolt>1.1903686e1</ivolt><raw>3453690,3438292</raw></data></li820>",'data')
        print(data)
    

            
if __name__ == "__main__":
    unittest.main()
