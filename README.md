# Licor Library for Python
Library to access [Licor](http://www.licor.com) devices.
## Supported Devices 
[Li-820 gas analyzer](https://www.licor.com/env/products/gas_analysis/LI-820/) over a serial line 
## Installation
### Installing on Linux 
- Import the repository key  
`wget -O - http://www.bayceer.uni-bayreuth.de/repos/apt/conf/bayceer_repo.gpg.key |apt-key add -`
- Add the following repository to /etc/apt/sources.list  
`deb http://www.bayceer.uni-bayreuth.de/repos/apt/debian stretch main`
- Update your repository cache  
`apt-get update`
- Install the package  
`apt-get install python-licor`
### Installation on Windows
Install the package by a git clone request followed by a run of setup.py:
``` 
git clone git://github.com/BayCEER/python-licor.git
cd python-licor
python setup.py install
```
## Example Usage
### Read the data values of a Licor 820 gas analyzer
```python
from licor import Li820
li = Li820("/dev/ttyUSB0")
try:
    li.connect()
    while True:        
        data = li.readData()         
        print("co2:{0}".format(data['co2']))    
        print("co2abs:{0}".format(data['co2abs']))    
        print("celltemp:{0}".format(data['celltemp']))    
        print("cellpres:{0}".format(data['cellpres']))    
        print("ivolt:{0}".format(data['ivolt']))    
        print("raw:{0}".format(data['raw']))    
except KeyboardInterrupt:
    li.disconnect()
```
## Authors 
* **Oliver Archner** - *Programmer* - [BayCEER, University of Bayreuth](https://www.bayceer.uni-bayreuth.de)
## History
### Version 1.0.0, Dec 14, 2017
- Initial release
## License
GNU LESSER GENERAL PUBLIC LICENSE, Version 2.1, February 1999
