import csv

files = ["2000","2002","2010"]
selectedState = "Ohio"

for filename in files:
    print "opening",filename
    with open('./tables/'+ filename + '.csv') as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
             if election['STATE'] is 'Ohio':
                 try:
                     votes = row['GENERAL ']
                 except KeyError:
                     votes = row['GENERAL RESULTS']
                     continue
                 if votes is not "" and row['PARTY'] is not "" and row['STATE'] == selectedState:
                     state = row['STATE'].replace(' ','_')
                     print filename,state,row['DISTRICT'] + ":",row['PARTY'],votes
