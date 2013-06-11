import csv
import os
from datetime import datetime
"""
Command line:
    getting data or putting data?
    file name or all? (confirm all)
    only work with orc files right now

"""
MISSING = '-999'
dir = os.path.dirname(__file__)
#os.path.join(dir,nfile)
filename = 'ntdrain.orc'
outfile = 'ntdrain.csv'

def parseargs():
    """
    parse arguments
    convert -999s?

    """

def parse_warmf_file(filename):
    alldata_list=[]

    f = open(os.path.join(dir,filename),'r')
    f_lines = f.readlines()
    f.close()
    outhead = f_lines[:2]
    alldata_list.append([outhead])
    outid = f_lines[2][:13]
    alldata_list.append([outid])
    alldata_list.append(['========DO NOT EDIT ABOVE THIS LINE========='])
    headline = f_lines[2]

    #Get headers and column count
    print "it started"
    headline_list = []
    pointer = 13
    for i, col in enumerate(headline):
        if i <= pointer:
            pass
        else:
            start = pointer
            end = pointer+8
            headline_list.append(headline[start:end].strip())
            pointer = pointer + 8
    alldata_list.append(headline_list)

    #process the data

    for row in f_lines[3:]:
        datarow_list=[]
        ndate = datetime.strptime(row[:8],'%d%m%Y')
        datarow_list.append(ndate)
        pointer = 13
        #Assumes time = 0000
        for col in headline_list:
            start = pointer
            end = pointer+8
            datarow_list.append(row[start:end].strip())
            pointer = pointer + 8
        datarow_list.append(row[pointer:].strip())
        alldata_list.append(datarow_list)
        datarow_list = []
    return alldata_list

def writeWARMFtoCSV(datalist):
    f = open(os.path.join(dir,outfile),'wb')
    csvwriter = csv.writer(f)
    #write to csv
    for row in datalist:
        csvwriter.writerow(row)
    f.close()
    print "it's done?"

def main():
    alldata_list = parse_warmf_file(filename)
    writeWARMFtoCSV(alldata_list)
    
if __name__ == '__main__':
    main()
