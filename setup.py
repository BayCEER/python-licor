try:
    from setuptools import setup
except ImportError:
	from distutils.core import setup 

setup(name='python-licor',
      version='1.0',
      description='Licor Analyzer API',
      url='http://github.com/BayCEER/python-licor',
      author='Oliver Archner',
      author_email='oliver.archner@uni-bayreuth.de',
      license='GPL2',
      packages=['licor'],
      install_requires=['pyserial'])


