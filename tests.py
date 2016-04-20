import utils, os, json,csv
from States import States



conversionTestCases = [("129063.0" ,129063),('[7,331]',7331),('',-1),('Unopposed',0)]


for case in conversionTestCases:
    assert utils.castToInt(case[0]) == case[1], "failed on '" + case[0] + "'"

assert utils.getDistrict("AL","./tables/2010.csv",1)['R'] == 129063, "problem with rep count for AL 2010 dist 1:" + str(utils.getDistrict("AL","./tables/2010.csv",1))
assert utils.getDistrict("AZ","./tables/2010.csv",1)['D'] == 99233, "problem with dem count"
assert utils.getDistrict("AZ","./tables/2010.csv",101)== {}, "problem with edge cases"
assert utils.getDistrict("AZ","./tables/2002.csv",2)['R'] == 100359.0,"problem reading from 2002"
assert utils.getDistrict("AL","./tables/2000.csv",2)['D'] == 64958.0,"problem reading from 2000"

states = States()

def testValueWithin(value,lower,higher):
    return value > lower and value < higher

assert testValueWithin(states.getDistrictRepub("WA",04,2000),0.62,0.63), "both numbers present test case fails."
assert testValueWithin(states.getDistrictRepub("WA",05,2000),x,y), "republican -1 case fails."


print "all tests pass!"
