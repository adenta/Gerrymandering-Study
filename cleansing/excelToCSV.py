import xlrd, csv
files = [str(year) for year in range(2000,2016,2)]
errors = 0
def csv_from_excel(filename):

    wb = xlrd.open_workbook('../sheets/' + filename + '.xls')

    sheets = map(str, wb.sheet_names())
    sheet = ""
    ind = 0
    print sheets
    while True:
        sheet = sheets[ind].lower()
        if ("house" in sheet and "senate" in sheet) or ( "house" in sheet and "master" in sheet) or ("house" in sheet and "results" in sheet and "state" in sheet) :
            break
        ind +=1
    print "reading sheet number ",ind,":",sheets[ind]
    sh = wb.sheet_by_index(ind)

    your_csv_file = open('../modified_tables/' + filename + '.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        try:
            wr.writerow(sh.row_values(rownum))
        except UnicodeEncodeError:
            global errors
            errors +=1
            print "Dang, line",rownum,"didn't work, on",filename,"."
            continue

    your_csv_file.close()



for name in files:
    csv_from_excel(name)

print errors,"errors."
