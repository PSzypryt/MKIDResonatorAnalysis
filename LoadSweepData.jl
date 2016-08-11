"""
Paul Szypryt
April 6, 2016
"""

function LoadSweepData(sweepDataFileName)

    # Open sweep data file
    sweepDataFile = open(sweepDataFileName, "r")

    # Put sweep data into large matrix, separate out header from the rest of the data
    rawSweepData = readdlm(sweepDataFile)
    sweepHeader = rawSweepData[1:7,:]
    sweepData = rawSweepData[8:end,:]
    
    
    # Read in header data line by line
    # Center frequency in GHz, frequency span in MHz, number of frequency steps, attenuation used for both channels
    frequencyCenter1, frequencySpan1, frequencySteps1, attenuation = sweepHeader[1,1:4]
    # Same data, for 2nd channel.  Same attenuation used on both channels, as defined above.
    frequencyCenter2, frequencySpan2, frequencySteps2 = sweepHeader[2,1:3]
    # ADR start and end temperature values
    startTemperature, endTemperature = sweepHeader[3,1:2]
    # I1 center value and standard deviation
    I1SweepOrigin, I1SweepOriginSTD = sweepHeader[4,1:2]
    # Q1 center value and standard deviation
    Q1SweepOrigin, Q1SweepOriginSTD = sweepHeader[5,1:2]
    # I2 center value and standard deviation
    I2SweepOrigin, I2SweepOriginSTD = sweepHeader[6,1:2]
    # Q2 center value and standard deviation
    Q2SweepOrigin, Q2SweepOriginSTD = sweepHeader[7,1:2]

    frequencySteps1 = convert(Int64, frequencySteps1)
    frequencySteps2 = convert(Int64, frequencySteps2)

    
    # Separate out sweep data into more manageable arrays, both channels
    # Sweep frequencies
    sweepFrequencies1 = convert(Array{Float64,1},sweepData[1:frequencySteps1, 1])
    sweepFrequencies2 = convert(Array{Float64,1},sweepData[frequencySteps1+1:frequencySteps1+frequencySteps2, 1])
    # I values
    I1SweepValues = convert(Array{Float64,1},sweepData[1:frequencySteps1, 2])
    I2SweepValues = convert(Array{Float64,1},sweepData[frequencySteps1+1:frequencySteps1+frequencySteps2, 2])
    # I standard deviations
    I1SweepValuesSTD = convert(Array{Float64,1},sweepData[1:frequencySteps1, 3])
    I2SweepValuesSTD = convert(Array{Float64,1},sweepData[frequencySteps1+1:frequencySteps1+frequencySteps2, 3])
    # Q values
    Q1SweepValues = convert(Array{Float64,1},sweepData[1:frequencySteps1, 4])
    Q2SweepValues = convert(Array{Float64,1},sweepData[frequencySteps1+1:frequencySteps1+frequencySteps2, 4])
    # Q standard deviations
    Q1SweepValuesSTD = convert(Array{Float64,1},sweepData[1:frequencySteps1, 5])
    Q2SweepValuesSTD = convert(Array{Float64,1},sweepData[frequencySteps1+1:frequencySteps1+frequencySteps2, 5])

    # Close sweep data file
    close(sweepDataFile)
    println("Finished loading sweep data file:  $sweepDataFileName")
    
    sweepHeaderDictionary = Dict(
        "frequencyCenter1" => frequencyCenter1,
        "frequencySpan1" => frequencySpan1,
        "frequencySteps1" => frequencySteps1,
        "I1SweepOrigin" => I1SweepOrigin,
        "I1SweepOriginSTD" => I1SweepOriginSTD,
        "Q1SweepOrigin" => Q1SweepOrigin,
        "Q1SweepOriginSTD" => Q1SweepOriginSTD,
        "frequencyCenter2" => frequencyCenter2,
        "frequencySpan2" => frequencySpan2,
        "frequencySteps2" => frequencySteps2,
        "I2SweepOrigin" => I2SweepOrigin,
        "I2SweepOriginSTD" => I2SweepOriginSTD,
        "Q2SweepOrigin" => Q2SweepOrigin,
        "Q2SweepOriginSTD" => Q2SweepOriginSTD,
        "attenuation" => attenuation,
        "startTemperature" => startTemperature,
        "endTemperature" => endTemperature
    )
    
    # Create a dictionary for the data output, can be referenced by keywords
    sweepDataDictionary = Dict(
        "sweepFrequencies1" => sweepFrequencies1,
        "I1SweepValues" => I1SweepValues,
        "I1SweepValuesSTD" => I1SweepValuesSTD,
        "Q1SweepValues" => Q1SweepValues,
        "Q1SweepValuesSTD" => Q1SweepValuesSTD,    
        "sweepFrequencies2" => sweepFrequencies2,
        "I2SweepValues" => I2SweepValues,
        "I2SweepValuesSTD" => I2SweepValuesSTD,
        "Q2SweepValues" => Q2SweepValues,
        "Q2SweepValuesSTD" => Q2SweepValuesSTD,
    )
    
    return sweepHeaderDictionary, sweepDataDictionary
    
end