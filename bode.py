import matplotlib.pyplot as plt
from math import log10, ceil

zeroes=list() #list that contains the zeroes
poles=list() #list that contains the poles
constants=list() #list that contains the constants

"""
num: a float number to be added to the 'zeroes' list
"""
def addZero(num):
    zeroes.append(num) #appends 'num' (float) to the 'zeroes' list

"""
num: a float number to be added to the 'poles' list
"""
def addPole(num):
    poles.append(num) #appends 'num' (float) to the 'poles' list

"""
num: a float number to be added to the 'constants' list
"""
def addConstant(num):
    constants.append(num) #appends 'num' (float) to the 'constants' list

"""
num: a float number to be removed from the 'zeroes' list
"""
def removeZero(num):
    try:
        zeroes.remove(num) #removes 'num' (float) from the 'zeroes' list
    except ValueError: #if 'num' doesn't exist a ValueError is raisen 
        print(num, "is not a zero")

"""
num: a float number to be removed from the 'poles' list
"""
def removePole(num):
    try:
        poles.remove(num) #removes 'num' (float) from the 'poles' list
    except ValueError:  #if 'num' doesn't exist a ValueError is raisen 
        print(num, "is not a pole")

"""
num: a float number to be removed from the 'constants' list
"""
def removeConstant(num):
    try:
        constants.remove(num) #removes 'num' (float) from the 'constants' list
    except ValueError: #if 'num' doesn't exist a ValueError is raisen 
        print(num, "is not a constant")

def removeAllZeroes():
    zeroes.clear() #removes all elements from the 'zeroes' list

def removeAllPoles():
    poles.clear() #removes all elements from the 'poles' list

def removeAllConstants():
    constants.clear() #removes all elements from the 'constants' list

def removeAll():
    #removes all elements from every list
    removeAllZeroes()
    removeAllPoles()
    removeAllConstants()

def showZeroes():
    print("Zeroes:", zeroes) #prints the 'zeroes' list

def showPoles():
    print("Poles:", poles) #prints the 'poles' list

def showConstants():
    print("Constants:", constants) #prints the 'constants' list

def showAll():
    #prints every list
    showZeroes()
    showPoles()
    showConstants()

"""
constant: the k value 
values: the values of the x-axis
"""
def getConstantYAmpValues(constant, values):
    constant=20*log10(abs(constant))
    return [constant for i in values] #for each x value
                                      #the constant has the same value

def getZeroYAmpValues(zero, values):
    yvalues=list()
    if zero == 0:
        return [20*log10(i) for i in values]
    else:
        for i in values:
            if(i<zero):
                yvalues.append(0)
            else:
                yvalues.append(20*log10(i)-20*log10(zero))
    return yvalues

def getPoleYAmpValues(pole, values):
    yvalues=list()
    if pole == 0:
        return [-20*log10(i) for i in values]
    else:
        for i in values:
            if(i<pole):
                yvalues.append(0)
            else:
                yvalues.append(-20*log10(i)+20*log10(pole))
    return yvalues

def getConstantYPhaseValues(constant, values):
    if constant>0:
        return [0 for i in values]
    else:
        return [180 for i in values]

def getZeroYPhaseValues(zero, values):
    if zero == 0:
        return [90 for i in values]
    else:
        yvalues=list()
        for i in values:
            if i<zero/10:
                yvalues.append(0)
            elif i>zero*10:
                yvalues.append(90)
            else:
                yvalues.append(45*log10(i)-45*log10(zero/10))
    return yvalues

def getPoleYPhaseValues(pole, values):
    if pole == 0:
        return [-90 for i in values]
    else:
        yvalues=list()
        for i in values:
            if i<pole/10:
                yvalues.append(0)
            elif i>pole*10:
                yvalues.append(-90)
            else:
                yvalues.append(-45*log10(i)+45*log10(pole/10))
    return yvalues

def adjustAngles(angles):
    for i in range(len(angles)):
        while(angles[i]>=360):
            angles[i]-=360
        while(angles[i]<=-360):
            angles[i]+=360

        if(angles[i]>180):
            angles[i]-=360
        if(i!=0 and angles[i-1]<0 and angles[i]==180):
            angles[i]-=360
        
        if(angles[i]<-180):
            angles[i]+=360
        if(i!=0 and angles[i-1]>0 and angles[i]==-180):
            angles[i]-=360
    return angles

def sumLists(list1, list2):
    for i in range(len(list1)):
        list1[i]+=list2[i]
    return list1

def plotAmplitudeDiagram(ampDiagram, xvalues):
    ampDiagram.set_xscale('log')
    ampDiagram.set_title("Amplitude Diagram")
    ampDiagram.set(xlabel="log ω", ylabel="AdB")
    
    constantYValues=[0 for i in range(len(xvalues))]
    zeroYValues=poleYValues=constantYValues
    gainYValues=zeroYValues
    for i in constants:
        constantYValues=getConstantYAmpValues(i, xvalues)
        ampDiagram.plot(xvalues, constantYValues, label="k = " + str(i))
        gainYValues=sumLists(gainYValues, constantYValues)

    for i in zeroes:
        zeroYValues=getZeroYAmpValues(i, xvalues)
        ampDiagram.plot(xvalues, zeroYValues, label="ω = " + str(i))
        gainYValues=sumLists(gainYValues, zeroYValues)

    for i in poles:
        poleYValues=getPoleYAmpValues(i, xvalues)
        ampDiagram.plot(xvalues, poleYValues, label="ω = " + str(i))
        gainYValues=sumLists(gainYValues, poleYValues)
    
    ampDiagram.plot(xvalues, gainYValues, linewidth=7.0, label="Amp")
    ampDiagram.legend(loc="upper right")

def plotPhaseDiagram(phDiagram, xvalues):
    phDiagram.set_xscale('log')
    phDiagram.set_title("Phase Diagram")
    phDiagram.set(xlabel="log ω", ylabel="φ")
    
    constantYValues=[0 for i in range(len(xvalues))]
    phaseYValues=zeroYValues=poleYValues=constantYValues

    for i in constants:
        constantYValues=getConstantYPhaseValues(i, xvalues)
        phDiagram.plot(xvalues, constantYValues, label="k = " + str(i))
        phaseYValues=sumLists(phaseYValues, constantYValues)

    for i in zeroes:
        zeroYValues=getZeroYPhaseValues(i, xvalues)
        phDiagram.plot(xvalues, zeroYValues, label="ω = " + str(i))
        phaseYValues=sumLists(phaseYValues, zeroYValues)

    for i in poles:
        poleYValues=getPoleYPhaseValues(i, xvalues)
        phDiagram.plot(xvalues, poleYValues, label="ω = " + str(i))
        phaseYValues=sumLists(phaseYValues, poleYValues)
    
    phaseYValues=adjustAngles(phaseYValues)
    phDiagram.plot(xvalues, phaseYValues, linewidth=7.0, label="Ph")
    phDiagram.legend(loc="upper right")

def bodePlot():
    fig, ax = plt.subplots(2)

    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5, hspace=0.5)

    abs_constants=[abs(i) for i in constants]
    xvalues=zeroes+poles+abs_constants
    if(len(xvalues)==0):
        print("There are missing parameters")
        return 0 

    try:
        while True:
            xvalues.remove(0)
    except ValueError:
        pass

    try:
        smallestNumber=min(xvalues)
        largestNumber=max(xvalues)
    except ValueError:
        smallestNumber=largestNumber=1

    smallestExponent=ceil(log10(smallestNumber))-4
    largestExponent=ceil(log10(largestNumber))+4
    
    xvalues+=[10**i for i in range(smallestExponent, largestExponent)]
    xvalues=list(set(xvalues))
    xvalues.sort() 
    yticksdB=[20*i for i in range(smallestExponent, largestExponent)]
    yticksDeg=[-180, -135, -90, -45, 0, 45, 90, 135, 180]

    ax[0].set_xticks(xvalues)
    ax[0].set_yticks(yticksdB)
    ax[1].set_xticks(xvalues)
    ax[1].set_yticks(yticksDeg)

    fig.suptitle("Bode Diagram")
    plotAmplitudeDiagram(ax[0], xvalues)
    plotPhaseDiagram(ax[1], xvalues)
    plt.show()

def showCommands():
    print("COMMANDS:\n")
    print("ADDZ n [add a zero]")
    print("ADDP n [add a pole]")
    print("ADDC n [add a constant]\n")
    print("REMZ n [remove a zero]")
    print("REMP n [remove a pole]")
    print("REMC n [remove a constant]")
    print("REMAZ [remove all zeros]")
    print("REMAP [remove all poles]")
    print("REMAC [remove all constants]")
    print("REMA [remove all]\n")
    print("SHWZ [show zeroes]")
    print("SHWP [show poles]")
    print("SHWC [show constants]")
    print("SHWA [show all]\n")
    print("BODE [print the bode diagram]\n")
    print("END [close the program]")
    print("CMDL [show the commands list]\n")

def commandStringConvert(string):
    string=string.split(" ")
    command=string[0].upper()
    number=0
    if(len(string)==2):
        number=eval(string[1])

    if command=="ADDZ":
        addZero(number)

    elif command=="ADDP":
        addPole(number)

    elif command=="ADDC":
        if number == 0:
            print("0 is not a valid constant")
            return 0
        addConstant(number)

    elif command=="REMZ":
        removeZero(number)

    elif command=="REMP":
        removePole(number)

    elif command=="REMC":
        removeConstant(number)

    elif command=="REMAZ":
        removeAllZeroes()

    elif command=="REMAP":
        removeAllPoles()

    elif command=="REMAC":
        removeAllConstants()

    elif command=="REMA":
        removeAll()

    elif command=="SHWZ":
        showZeroes()

    elif command=="SHWP":
        showPoles()

    elif command=="SHWC":
        showConstants()

    elif command=="SHWA":
        showAll()

    elif command=="BODE":      
        bodePlot()  
    
    elif command=="CMDL":
        showCommands()

    elif command=="END":
        quit()

    else:
        print("Command not found")

if __name__=="__main__":
    print("--- Bode Diagram Plotter ---")
    while True:
        commandStringConvert(input())