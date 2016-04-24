import json, yaml, io
from collections import Counter

class States:
    stateFile = open('states.json','r')
    states = yaml.safe_load(stateFile.read())
    stateStrings = states.keys()


    def getState(self,strState):
        assert strState in self.stateStrings, "Not a valid US state."
        return self.states[strState]


    def printState(self,strState):
        assert strState in self.stateStrings, "Not a valid US state."
        print json.dumps(self.states[strState], indent = 2)

    def printAllDistricts(self):
        for strState in self.states.keys():
            for district in self.getState(strState):
                for year in self.states[strState][district].keys():
                    print "REP %",self.getDistrictRepub(strState,district,year)

    def printDistrictReport(self,strState,distNum):
        print json.dumps(self.getDistrictReport(strState,distNum), indent = 2, sort_keys = True)


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

        if district['R']<=1:
            if district['R'] ==-1:
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
