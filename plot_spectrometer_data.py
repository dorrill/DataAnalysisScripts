#Imported libraries below
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd

#   #   #   #   #   #   #   #   #   # Functions #   #   #   #   #   #   #   #   #   #

def plotEvents(dataFile):
    #grabbing data here
    lineNum = 0
    wavelengths=[] #x-axis
    percents=[] #y-axis
    for line in dataFile:
        if lineNum>14:
            line = line.split()  #split the file line's string into pieces
            wavelengths.append(float(line[0]))
            percents.append(float(line[1]))
        lineNum+=1

    #Plot Here:
    import seaborn as sns      #Seaborn adds plotting options, nicities
    plotTitle="Specular Refl, DF2000PE & Teonex Q65HA (PEN01)"
    #plotTitle="Transmittance, Teonex Q65HA (PEN01)"
    #plotTitle="Specular Refl, DF2000PE & Sigma Millipore PEN(03)"
    #Diffuse Refl, DF2000PE Reflector
    #Default axes (looks nicer)
    plt.plot(wavelengths,percents, marker='o', color='mediumvioletred',linestyle="")
    plt.title(plotTitle)
    plt.xlabel("Wavelength(nm)")
    plt.ylabel("Percent(%)")
    plt.xlim(290,901)
    #plt.ylim(0,105)
    plt.grid()
    #plt.show()
    pngfileName1=fileNameStr[0]+".png"
    plt.savefig(pngfileName1)

    #Preset axes (better for comparison)
    plt.plot(wavelengths,percents, marker='o', color='mediumvioletred',linestyle="")
    plt.title(plotTitle)
    plt.xlabel("Wavelength(nm)")
    plt.ylabel("Percent(%)")
    plt.xlim(290,901)
    plt.ylim(0,100)
    plt.grid()
    #plt.show() #Uncomment this to see the plot instead of saving it, comment next line
    pngfileName2=fileNameStr[0]+"_tall"+".png"
    plt.savefig(pngfileName2)

def plotTransmittanceDataTogether(dataFiles):
    #grabbing data here
    fileNum=0
    markers=['o','1','.','x']
    colors=['mediumvioletred','blue','crimson','orange']
    for dataFile in dataFiles:
        with open(dataFile) as f:
            lineNum = 0
            wavelengths=[] #x-axis
            percents=[] #y-axis
            for line in f:
                if lineNum>14 and lineNum%4==0:
                    line = line.split()  #split the file line's string into pieces
                    wavelengths.append(float(line[0]))
                    percents.append(float(line[1]))
                lineNum+=1
            #print(wavelengths)
            plt.plot(wavelengths,percents, marker=markers[fileNum], color=colors[fileNum],linestyle="")
            fileNum+=1

    #Plot Here:
    import seaborn as sns      #Seaborn adds plotting options, nicities
    plotTitle="Light Transmission of Samples"
    #Default axes (looks nicer)
    plt.title(plotTitle)
    plt.xlabel("Wavelength(nm)")
    plt.ylabel("Percent(%)")
    labels=["Teonex Q65FA(PEN01)","Teonex Q53(PEN03)"]
    plt.legend(labels)
    #plt.xlim(290,901)
    plt.xlim(390,610)
    plt.ylim(0,100)
    plt.grid()
    plt.show()

def plotSpecReflDataTogether(dataFiles):
    #grabbing data here
    fileNum=0
    markers=['o','1','.','x']
    colors=['mediumvioletred','blue','crimson','orange']
    for dataFile in dataFiles:
        with open(dataFile) as f:
            lineNum = 0
            wavelengths=[] #x-axis
            percents=[] #y-axis
            for line in f:
                if lineNum>14:
                    line = line.split()  #split the file line's string into pieces
                    wavelengths.append(float(line[0]))
                    percents.append(float(line[1]))
                lineNum+=1
            #print(wavelengths)
            plt.plot(wavelengths,percents, marker=markers[fileNum], color=colors[fileNum],linestyle="")
            fileNum+=1

    #Plot Here:
    import seaborn as sns      #Seaborn adds plotting options, nicities
    plotTitle="Specular Reflection from Samples"
    #Default axes (looks nicer)
    plt.title(plotTitle)
    plt.xlabel("Wavelength(nm)")
    plt.ylabel("Percent(%)")
    labels=["Teonex Q65FA(PEN01)","Teonex Q53(PEN03)","DF2000 Reflector"]
    plt.legend(labels)
    #plt.xlim(290,901)
    plt.xlim(390,610)
    plt.ylim(-6,119)
    plt.grid()
    plt.show()

def plotDiffuseReflDataTogether(dataFiles):
    #grabbing data here
    fileNum=0
    markers=['o','1','.','x']
    colors=['mediumvioletred','blue','crimson','orange']
    for dataFile in dataFiles:
        with open(dataFile) as f:
            lineNum = 0
            wavelengths=[] #x-axis
            percents=[] #y-axis
            for line in f:
                if lineNum>14 and lineNum%4==0:
                    line = line.split()  #split the file line's string into pieces
                    wavelengths.append(float(line[0]))
                    percents.append(float(line[1]))
                lineNum+=1
            #print(wavelengths)
            plt.plot(wavelengths,percents, marker=markers[fileNum], color=colors[fileNum],linestyle="")
            fileNum+=1

    #Plot Here:
    import seaborn as sns      #Seaborn adds plotting options, nicities
    plotTitle="Diffuse Reflection from Samples"
    #Default axes (looks nicer)
    plt.title(plotTitle)
    plt.xlabel("Wavelength(nm)")
    plt.ylabel("Percent(%)")
    labels=["Teonex Q65FA(PEN01)","Teonex Q53(PEN03)","DF2000 Reflector"]
    plt.legend(labels)
    #plt.xlim(290,901)
    plt.xlim(390,610)
    plt.ylim(0,100)
    plt.grid()
    plt.show()

#   #   #   #   #   #   #   #   #   # Main #   #   #   #   #   #   #   #   #   #
datFiles=[]
#file = sys.argv[1]   #name of file script runs on, entered on command line
numImputs=(len(sys.argv))
for i in range(len(sys.argv)):
    if i > 0:
        datFiles.append(sys.argv[i])
#plotTransmittanceDataTogether(datFiles)
plotDiffuseReflDataTogether(datFiles)
#plotSpecReflDataTogether(datFiles)
#fileNameStr = str(file).split('.') #use input file name to name output png's
#with open(file) as f:
    #cplotEvents(f)
