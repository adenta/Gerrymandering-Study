import utils, csv, os, json,time

folder = "tables"

paths = [os.path.join(folder,fn) for fn in next(os.walk(folder))[2]]
data = {}
states = {}

start = time.time()
for state in utils.states:
    districts = {};
    for i in range(100):
        district =  utils.getDistrictHistory(state,i)
        if district:
            districts.update({"district " + str(i): district})
    states[state] = districts



out =  open("states.json","w")
out.write( json.dumps(states,indent=2))

end =  time.time()
print (end-start)/60,"minutes elapsed."
