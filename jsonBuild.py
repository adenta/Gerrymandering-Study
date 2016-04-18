import utils, csv, os, json

folder = "tables"

paths = [os.path.join(folder,fn) for fn in next(os.walk(folder))[2]]
data = {}
states = {}
for state in utils.states:
    districts = {};
    for i in range(100):
        district =  utils.getDistrictHistory(state,i)
        if district:
            districts.update({"district " + str(i): district})
    states[state] = districts



alabama = {"bama":states}
out =  open("states.json","w")
out.write( json.dumps(alabama,indent=2))
