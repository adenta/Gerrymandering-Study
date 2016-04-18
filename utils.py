import csv, os
import copy
from itertools import izip

parties = ['D','R']

states = ['WA', 'DE', 'DC', 'WI', 'WV', 'HI', 'FL', 'WY', 'NH', 'NJ', 'NM', 'TX', 'LA', 'NC', 'ND', 'NE', 'TN', 'NY', 'PA',
 'CA', 'NV', 'VA', 'GU', 'CO', 'VI', 'AK', 'AL', 'AS', 'AR', 'VT', 'IL', 'GA', 'IN', 'IA', 'OK', 'AZ', 'ID', 'CT', 'ME',
 'MD', 'MA', 'OH', 'UT', 'MO', 'MN', 'MI', 'RI', 'KS', 'MT', 'MP', 'MS', 'SC', 'KY', 'OR', 'SD']

folder = "tables"

paths = [os.path.join(folder,fn) for fn in next(os.walk(folder))[2]]

years = [int(year[7:-4].replace("-flat","")) for year in paths]

def cleanNumber(numString):

    if "." in numString:
        return int(numString[:numString.index(".")])
    else:
        try:
            return int(numString)
        except ValueError:
            return numString

def castToInt(numString):
    cast = None
    try:

        cast = float(numString)
        return cast
    except ValueError:
        try:
            numList = [n for n in numString[1:-1] if n.isdigit() ]
            cast = int("".join(numList))
            return cast
        except ValueError:
            if numString == "":
                return -1
            else:
                return 0



    return cast


# for a given year and state, return a dictionary of all the districts, and what that district voted for.
def getDistricts( state, fnYear):
    districts = {};
    for i in range(100):
        district =  getDistrict(state,fnYear,i)
        if district == {} and i is not 0:
            break
        districts.update({"district " + str(i): district})

    return districts

def getColumnDistrict(state,fnYear,number):
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

            ogVotes = copy.deepcopy(votes)
            votes = castToInt(votes)
            partialDistrictNumber = cleanNumber(partialDistrict['DISTRICT'])
            isDataClean = partialDistrict['PARTY'] is not ""
            matchingConditions = stateKey.lower() == state.lower() and partialDistrictNumber == number

            if isDataClean and matchingConditions:

                try:
                    district[partialDistrict['PARTY'][:1]] = max(int(votes),district[partialDistrict['PARTY'][:1]])
                except KeyError:
                    district[partialDistrict['PARTY'][:1]] = int(votes)

                 # this conditional makes things run quicker, however; it also only lets us look at republican and democrats.
                if all(key in district for key in parties):
                    break


        return district


def getFlatDistrict(state,fnYear,number):
    return {}


# for a given state district, for a given year, return a dictionary that tells how many democratic votes were cast,
# and how many republican votes were cast, and how many other votes were cast.
def getDistrict(state,fnYear, number):
    if "flat" in fnYear:
        return getFlatDistrict(state,fnYear,number)
    else:
        return getColumnDistrict(state,fnYear,number)


def getDistrictHistory(state,number):
    district = {}
    for route, year in izip(paths,years):
        dist = getDistrict(state,route,number)
        if dist:
            district[year] = dist
    return district
