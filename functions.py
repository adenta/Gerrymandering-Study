import csv

parties = ['D','R']

def cleanNumber(numString):

    if "." in numString:
        return int(numString[:numString.index(".")])
    else:
        try:
            return int(numString)
        except ValueError:
            return -1

# for a given year and state, return a dictionary of all the districts, and what that district voted for.
def getDistricts( state, fnYear):
    for i in range(100):
        district =  getDistrict(state,fnYear,i)
        if district == {} and i is not 0:
            break
        print district


# for a given state district, for a given year, return a dictionary that tells how many democratic votes were cast,
# and how many republican votes were cast, and how many other votes were cast.
def getDistrict(state,fnYear, number):
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

            partialDistrictNumber = cleanNumber(partialDistrict['DISTRICT'])
            isDataClean = votes is not "" and partialDistrict['PARTY'] is not ""
            matchingConditions = stateKey.lower() == state.lower() and partialDistrictNumber == number

            if isDataClean and matchingConditions:

                district[partialDistrict['PARTY'][:1]] = votes

                 # this conditional makes things run quicker, however; it also only lets us look at republican and democrats.
                if all(key in district for key in parties):
                    break


        return district
