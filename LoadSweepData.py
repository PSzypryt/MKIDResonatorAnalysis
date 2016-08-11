"""
Paul Szypryt
August 10, 2016
"""

import numpy as np

def LoadSweepData(sweepDataFileName):

    # Open sweep data file and extract data
    rawSweepFile = open(sweepDataFileName, "r")
    sweepFile = rawSweepFile.readlines()
    rawSweepFile.close()

    # Seperate file into header and data arrays
    sweepHeader = sweepFile[:7]
    sweepDataRaw = sweepFile[7:]
    
    # Read in header data line by line
    # Center frequency in GHz, frequency span in MHz, number of frequency steps, attenuation used for both channels
    frequencyCenter1, frequencySpan1, frequencySteps1, attenuation = sweepHeader[0].split()
    # Same data, for 2nd channel.  Same attenuation used on both channels, as defined above.
    frequencyCenter2, frequencySpan2, frequencySteps2 = np.array(sweepHeader[1].split()[0:3], dtype = float)
    # ADR start and end temperature values
    startTemperature, endTemperature = np.array(sweepHeader[2].split(), dtype = float)
    # I1 center value and standard deviation
    I1SweepOrigin, I1SweepOriginSTD = np.array(sweepHeader[3].split(), dtype = float)
    # Q1 center value and standard deviation
    Q1SweepOrigin, Q1SweepOriginSTD = np.array(sweepHeader[4].split(), dtype = float)
    # I2 center value and standard deviation
    I2SweepOrigin, I2SweepOriginSTD = np.array(sweepHeader[5].split(), dtype = float)
    # Q2 center value and standard deviation
    Q2SweepOrigin, Q2SweepOriginSTD = np.array(sweepHeader[6].split(), dtype = float) 

    frequencySteps1 = int(float(frequencySteps1))
    frequencySteps2 = int(float(frequencySteps2))

    # Separate out sweep data into more manageable arrays, both channels
    sweepData = np.loadtxt(sweepDataRaw)

    # Sweep frequencies
    sweepFrequencies1 = np.array(sweepData.T[0][:frequencySteps1])
    sweepFrequencies2 = np.array(sweepData.T[0][frequencySteps1:frequencySteps1+frequencySteps2])
    # I values
    I1SweepValues = np.array(sweepData.T[1][:frequencySteps1])
    I2SweepValues = np.array(sweepData.T[1][frequencySteps1:frequencySteps1+frequencySteps2])
    # I standard deviations
    I1SweepValuesSTD = np.array(sweepData.T[2][:frequencySteps1])
    I2SweepValuesSTD = np.array(sweepData.T[2][frequencySteps1:frequencySteps1+frequencySteps2])
    # Q values
    Q1SweepValues = np.array(sweepData.T[3][:frequencySteps1])
    Q2SweepValues = np.array(sweepData.T[3][frequencySteps1:frequencySteps1+frequencySteps2])
    # Q standard deviations
    Q1SweepValuesSTD = np.array(sweepData.T[4][:frequencySteps1])
    Q2SweepValuesSTD = np.array(sweepData.T[4][frequencySteps1:frequencySteps1+frequencySteps2])
    
    sweepHeaderDictionary = {
        'frequencyCenter1': frequencyCenter1,
        'frequencySpan1': frequencySpan1,
        'frequencySteps1': frequencySteps1,
        'I1SweepOrigin': I1SweepOrigin,
        'I1SweepOriginSTD': I1SweepOriginSTD,
        'Q1SweepOrigin': Q1SweepOrigin,
        'Q1SweepOriginSTD': Q1SweepOriginSTD,
        'frequencyCenter2': frequencyCenter2,
        'frequencySpan2': frequencySpan2,
        'frequencySteps2': frequencySteps2,
        'I2SweepOrigin': I2SweepOrigin,
        'I2SweepOriginSTD': I2SweepOriginSTD,
        'Q2SweepOrigin': Q2SweepOrigin,
        'Q2SweepOriginSTD': Q2SweepOriginSTD,
        'attenuation': attenuation,
        'startTemperature': startTemperature,
        'endTemperature': endTemperature
    }


    # Create a dictionary for the data output, can be referenced by keywords
    sweepDataDictionary = {
        'sweepFrequencies1': sweepFrequencies1,
        'I1SweepValues': I1SweepValues,
        'I1SweepValuesSTD': I1SweepValuesSTD,
        'Q1SweepValues': Q1SweepValues,
        'Q1SweepValuesSTD': Q1SweepValuesSTD,    
        'sweepFrequencies2': sweepFrequencies2,
        'I2SweepValues': I2SweepValues,
        'I2SweepValuesSTD': I2SweepValuesSTD,
        'Q2SweepValues': Q2SweepValues,
        'Q2SweepValuesSTD': Q2SweepValuesSTD
    }
    
    return sweepHeaderDictionary, sweepDataDictionary

