import csv

parties = ['D','R']

# for a given year and state, return a dictionary of all the districts, and what that district voted for.
def getDistricts( state, fnYear):
    for i in range(100):
        district =  getDistrict(state,fnYear,str(i).zfill(2))
        if district == {} and i is not 0:
            break
        print district


# for a given state district, for a given year, return a dictionary that tells how many democratic votes were cast,
# and how many republican votes were cast, and how many other votes were cast.
def getDistrict(state,fnYear, number):
    try:
         open(fnYear)
    except IOError:
        print "bad number:",number
        return {}
    with open(fnYear) as yearTable:
        district = {}
        districts = csv.DictReader(yearTable)
        for partialDistrict in districts:
            try:
                stateKey = partialDistrict['STATE ABBREVIATION']
            except KeyError:
                stateKey = partialDistrict['STATE']

            try:
                votes = partialDistrict['GENERAL ']
            except KeyError:
                votes = partialDistrict['GENERAL RESULTS']
            isDataClean = votes is not "" and partialDistrict['PARTY'] is not ""
            matchingConditions = stateKey.lower() == state.lower() and partialDistrict['DISTRICT'] == number

            if "2000" in fnYear:
                print isDataClean,":",matchingConditions
            if isDataClean and matchingConditions:

                district[partialDistrict['PARTY'][:1]] = votes

                 # this conditional makes things run quicker, however; it also only lets us look at republican and democrats.
                if all(key in district for key in parties):
                    break


        return district
