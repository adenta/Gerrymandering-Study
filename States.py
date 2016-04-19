import json, yaml, io

class States:
    stateFile = open('states.json','r')
    states = yaml.safe_load(stateFile.read())
    stateStrings = states.keys()

    def getState(self,strState):
        assert strState in self.stateStrings, "Not a valid state."
        return self.states[strState]


    def printState(self,strState):
        assert strState in self.stateStrings, "Not a valid state."
        print json.dumps(self.states[strState], indent = 2)

    
