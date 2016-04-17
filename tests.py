import functions

assert functions.getDistrict("AL","./tables/2010.csv","01")['R'] == '129063.0', "problem with rep count"
assert functions.getDistrict("AZ","./tables/2010.csv","01")['D'] == '99233.0', "problem with dem count"
assert functions.getDistrict("AZ","./tables/2010.csv","101")== {}, "problem with edge cases"
assert functions.getDistrict("AZ","./tables/2002.csv","02")['R'] == '100359.0',"problem reading from 2002"

print  functions.getDistrict("AL","./tables/2000.csv","02")
# assert functions.getDistrict("AL","./tables/2000.csv","02")['D'] == '64958.0',"problem reading from 2000"
