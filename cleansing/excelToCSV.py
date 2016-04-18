import xlrd, csv, utils
files = ["2000","2002","2004","2006","2008","2010","2012","2014"]

def csv_from_excel(filename):

    wb = xlrd.open_workbook('./sheets/' + filename + '.xls')

    sheets = map(str, wb.sheet_names())
    sheet = ""
    ind = 0
    while True:
        sheet = sheets[ind].lower()

        if "house" in sheet:
            break
        ind +=1
    print "reading sheet number ",ind,":",sheets[ind]
    sh = wb.sheet_by_index(ind)

    your_csv_file = open('./tables/' + filename + '.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(sh.nrows):
        try:
            wr.writerow(sh.row_values(rownum))
        except UnicodeEncodeError:
            print "Dang, line",rownum,"didn't work, on",filename,"."
            continue

    your_csv_file.close()



for name in files:
    csv_from_excel(name)
