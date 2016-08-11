import ConfigParser
import LoadSweepData

config = ConfigParser.ConfigParser()
config.read('SweepSetup.cfg')

sweepDataFileName = config.get('Directories', 'SweepDataFileName')

LoadSweepData.LoadSweepData(sweepDataFileName)
