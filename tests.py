import utils, os, json

assert utils.getDistrict("AL","./tables/2010.csv",1)['R'] == '129063.0', "problem with rep count"
assert utils.getDistrict("AZ","./tables/2010.csv",1)['D'] == '99233.0', "problem with dem count"
assert utils.getDistrict("AZ","./tables/2010.csv",101)== {}, "problem with edge cases"
assert utils.getDistrict("AZ","./tables/2002.csv",2)['R'] == '100359.0',"problem reading from 2002"
assert utils.getDistrict("AL","./tables/2000.csv",2)['D'] == '64958.0',"problem reading from 2000"
