import json, yaml, io

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

    def getDistrict(self,strState,distNum,year):
        return self.states[strState]["district " + str(distNum)][str(year)]

    #returns the percentage of republican votes to democratic votes
    def getDistrictRepub(self,strState,distNum,year):
        district =  self.getDistrict(strState,distNum,year)
        return district['R']/float(district['R'] + district['D'])

    def getDistrictDemo(self,strState,distNum,year):
        return 1.0-getDistrictRepub(self,strState,distNum,year)
