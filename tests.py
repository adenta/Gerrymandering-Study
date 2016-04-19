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

print states.getState("AK")
states.printState("OH")

print "all tests pass!"
