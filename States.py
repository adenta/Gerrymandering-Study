import json, yaml, io, sys, random
import numpy as np
from collections import Counter

class States:
    stateFile = open('states.json','r')
    states = yaml.safe_load(stateFile.read())
    stateStrings = states.keys()
    stateDatasetFolder = './stateDatasets/'
    years = range(2000,2016,2)


    def getState(self,strState):
        assert strState in self.stateStrings, "Not a valid US state."
        return self.states[strState]

    def getStateVariance(self,strState,year):# returns the variance for a state for 2004
        stateSet = self.getState(strState)
        stateSetKeys = stateSet.keys();

        repubToDemRatios = []
        for districtName in stateSetKeys:
            try:
                ratio = self.getDistrictRepub(strState,districtName,year)
            except KeyError:
                continue
            repubToDemRatios.append(ratio)
        return np.var(repubToDemRatios)


    def getStateVarianceHistory(self,state):
        stateVariances = []
        for year in self.years:
            variance = {}
            variance['line'] = state
            variance['value'] = self.getStateVariance(state,year)
            variance['year'] = year
            if variance['value'] is not None and variance['value'] > 0:
                stateVariances.append(variance)

        return stateVariances

    def getStatesVarianceHistory(self,listOfStates):
        if listOfStates == None:
            listOfStates = self.stateStrings
        stateVariances = []
        for state in listOfStates:
            stateVariances += self.getStateVarianceHistory(state)

        return stateVariances


    def printAllDistrictErrors(self):
        errors = Counter()
        for strState in self.states.keys():
            for district in self.getState(strState):
                for year in self.states[strState][district].keys():
                    for party in self.states[strState][district][year].keys():
                        if self.states[strState][district][year][party] == -1:
                            errors.update({strState:1})

        difference = set(self.states.keys()).difference(set(errors.keys()))
        print errors
        print "good states",difference

    def printDistrictReport(self,strState,distNum):
        print json.dumps(self.getDistrictReport(strState,distNum), indent = 2, sort_keys = True)

    def printState(self,strState):
        assert strState in self.stateStrings, "Not a valid US state."
        print json.dumps(self.states[strState], indent = 2)

    def printStateVarianceReport(self,strState):
        print strState + ":"
        print json.dumps(self.getStateVarianceHistory(strState), indent = 2, sort_keys = True)

    def printVarianceReport(self):
        print json.dumps(self.getStatesVarianceHistory(), indent = 2, sort_keys = True)

    def writeStateDistrictReport(self,state):
        f = open(self.stateDatasetFolder + 'dist-' + state  + '.json','w')
        f.write( json.dumps(self.getStateDistrictHistory(state), indent = 2, sort_keys = True))

    def writeStateVarianceReport(self,state):
        f = open(self.stateDatasetFolder + 'var-' + state + '.json','w')
        f.write( json.dumps(self.getStateVarianceHistory(state), indent = 2, sort_keys = True))

    def writeVarianceReport(self,listOfStates):
        f = open('variances.json','w')

        f.write( json.dumps(self.getStatesVarianceHistory(listOfStates), indent = 2, sort_keys = True))

    def sanatizeInputs(self,distNum,year):
        if isinstance(distNum,basestring):
            sanatizedDistNum = distNum
        else:
            sanatizedDistNum = "district " + str(distNum)

        if isinstance(year,basestring):
            sanatizedYear = year
        else:
            sanatizedYear = str(year)
        return [sanatizedDistNum,sanatizedYear]

    def getDistrict(self,strState,distNum,year):
        sanatizedDistNum, sanatizedYear = self.sanatizeInputs(distNum,year)
        return self.states[strState][sanatizedDistNum][sanatizedYear]

    def getDistrictHistory(self,strState,distNum):
        sanatizedDistNum = self.sanatizeInputs(distNum,-1)[0] # how can I improve this so I only sanatize one input at a time?
        return self.states[strState][sanatizedDistNum]

    #returns the percentage of republican votes to democratic votes
    def getDistrictRepub(self,strState,distNum,year):

        district =  self.getDistrict(strState,distNum,year)

        if 'R' not in district.keys():
            return 0
        if 'D' not in district.keys():
            return 1

        if district['R']<=1: # Republican party election is either uncontested, or missing.
            if district['R'] ==-1: # election was missing.
                print "Warning! missing election- Repub:",strState,distNum,year
            return 0

        if district['D']<=1:
            if district['D'] == -1:
                print "Warning! missing election- Demo:",strState,distNum,year
            return 1

        return district['R']/float(district['R'] + district['D'])

    def getDistrictDemo(self,strState,distNum,year): # returns percentage of democrats against total votes for a given district- state- year
        return 1.0-getDistrictRepub(self,strState,distNum,year)

    # returns dictionary of the  percentage change between how many people voted republican each district over time.
    def getDistrictChanges(self,strState,distNum):
        districtHistory = self.getDistrictHistory(strState,distNum)
        yearsActive = sorted([int(k) for k in districtHistory.keys()])
        districtDelta = {}

        for i in range(1,len(yearsActive)):
            currentYear = str(yearsActive[i])
            prevYear = str(yearsActive[i-1])

            currentPercent = self.getDistrictRepub(strState,distNum,currentYear)
            prevPercent = self.getDistrictRepub(strState,distNum,prevYear)

            reportObject = {}
            reportObject['delta'] = (currentPercent - prevPercent)
            reportObject['to'] = currentPercent
            reportObject['from'] = prevPercent


            districtDelta[prevYear + "-" + currentYear] = reportObject

        return districtDelta

    def getDistrictReport(self,strState,distNum):
        return {"historic results":self.getDistrictHistory(strState,distNum),
        "delta per year":self.getDistrictChanges(strState,distNum)}

    def getStateDistrictHistory(self,state):
        stateHistory = []
        for year in self.years:
            for district in self.states[state].keys():
                try:
                    dataPoint = {}
                    dataPoint['line'] = district.replace(" ","")
                    dataPoint['value'] = self.getDistrictRepub(state,district,year)
                    dataPoint['year'] = year
                    stateHistory.append(dataPoint)
                except KeyError:
                    print "missing year" , str(year)
        return stateHistory
