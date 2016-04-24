import utils, os, json,csv
from States import States



conversionTestCases = [("129063.0" ,129063),('[7,331]',7331),('',-1),('Unopposed',0)]

states = States()

def testValueWithin(value,lower,higher):
    return value >= lower and value <= higher

# Tests for converting string to int values for election dates.
for case in conversionTestCases:
    assert utils.castToInt(case[0]) == case[1], "failed on '" + case[0] + "'"

# Tests for getting a district
assert utils.getDistrict("AL","./tables/2010.csv",1)['R'] == 129063, "problem with rep count for AL 2010 dist 1:" + str(utils.getDistrict("AL","./tables/2010.csv",1))
assert utils.getDistrict("AZ","./tables/2010.csv",1)['D'] == 99233, "problem with dem count"
assert utils.getDistrict("AZ","./tables/2010.csv",101)== {}, "problem with edge cases"
assert utils.getDistrict("AZ","./tables/2002.csv",2)['R'] == 100359.0,"problem reading from 2002"
assert utils.getDistrict("AL","./tables/2000.csv",2)['D'] == 64958.0,"problem reading from 2000"

# Tests for getting a percentage ration dems to repubs.
assert testValueWithin(states.getDistrictRepub("WA",4,2000),0.62,0.63), "both numbers present test case fails."
assert states.getDistrictRepub("WA",5,2000) == 0, "republican -1 case fails."
assert states.getDistrictRepub("FL",7,2004) == 1, "republican Unopposed case fails."
assert states.getDistrictRepub("FL",2,2006) == 0, "Democratic Unopposed case fails."


# Extra printed content
states.printDistrictReport("NC",12)
print states.getStateVarianceHistory("KY")

print "all tests pass!"
