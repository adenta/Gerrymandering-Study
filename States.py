import json, yaml, io
from collections import Counter

class States:
    stateFile = open('states.json','r')
    states = yaml.safe_load(stateFile.read())
    stateStrings = states.keys()
    errors = Counter()


    def getState(self,strState):
        assert strState in self.stateStrings, "Not a valid US state."
        return self.states[strState]


    def printState(self,strState):
        assert strState in self.stateStrings, "Not a valid US state."
        print json.dumps(self.states[strState], indent = 2)

    def getDistrict(self,strState,distNum,year):
        if isinstance(distNum,basestring):
            sanatizedDistNum = distNum
        else:
            sanatizedDistNum = "district " + str(distNum)

        if isinstance(year,basestring):
            sanatizedYear = year
        else:
            sanatizedYear = str(year)
        return self.states[strState][sanatizedDistNum][sanatizedYear]

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
            self.errors.update({strState:1})
            return 0
        if district['D']<=1:
            if district['D'] == -1:
                print "Warning! missing election- Demo:",strState,distNum,year

            self.errors.update({strState:1})
            return 1
        return district['R']/float(district['R'] + district['D'])

    def getDistrictDemo(self,strState,distNum,year):
        return 1.0-getDistrictRepub(self,strState,distNum,year)

    def printAllDistricts(self):
        for strState in self.states.keys():
            for district in self.getState(strState):
                for year in self.states[strState][district].keys():
                    print "REP %",self.getDistrictRepub(strState,district,year)

        print self.errors
        print sum(self.errors.values()),"total errors."

    """def statesIterator(self):
        for strState in self.states.keys():
            for district in self.getState(strState):
                for year in self.states[strState][district].keys():
"""
