import io, json, os, csv

folder = "tables"
paths = [os.path.join(folder,fn) for fn in next(os.walk(folder))[2]]
states = {}
parties = ["DEM","REP"]

def buildPartialElection(packet):
    partialElection = {}
    partialElection['year'] = packet['year']

    for party in parties:
        if packet['party'] == party:
            partialElection[party] = packet['votes']
    return partialElection

def routePacket(packet):
    if packet['state'] not in states.keys():
        district = {}
        partialElection = {}
        partialElection['year'] = packet['year']

        for party in parties:
            if packet['party'] == party:
                partialElection[party] = packet['votes']

        district['years'] = [buildPartialElection(packet)]

        states[packet['state']] = {packet['district']:district}
    else:
        currentState = states[packet['state']]
        if packet['district'] not in currentState.keys():
            currentState[packet['district']] = [{'years':buildPartialElection(packet)}]
        else:
            print currentState[packet['district']]





for route in paths:
    with open(route) as data:
        year = csv.DictReader(data)
        votes = None
        district = {}
        for election in year:
            try:
                 votes = election['GENERAL ']
            except KeyError:
                 votes = election['GENERAL RESULTS']
                 continue
            if  election['PARTY'] is not "" and votes is not "":

                electionYear = route[7:-4]
                packet = {}
                packet['state'] = election['STATE']
                packet['year'] = electionYear
                packet['party'] = election['PARTY']
                packet['district'] = election['DISTRICT']
                packet['votes'] = votes # need to cast to integer
                routePacket(packet)
