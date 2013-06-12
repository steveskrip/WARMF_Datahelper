import csv
import os
from datetime import datetime
import argparse
import sys

aparser = argparse.ArgumentParser()
aparser.add_argument("[WARMF .orc file]", help = "filename of the WARMF .orc file")
args = aparser.parse_args()
#print sys.argv
filename = sys.argv[1]
#print filename
outfile = filename.split('.')[0]+".csv" 


print "\n\n\n"
print "Summary:\n\nYou would like to convert {0} to a CSV file.".format(filename)
print "This will create {0} in this directory. Be sure it doesn't already exist".format(outfile)
print "Make sure the file you selected ends with .orc and it exists in this folder"
print "\nBe sure to save the edited .csv file as a .csv file in Microsoft Excel."
s = raw_input('\nWould you like to proceed? [Y?]: ')
if s.lower() == 'y':
    pass
else:
    sys.exit()



"""
Command line:
    getting data or putting data?
    file name or all? (confirm all)
    only work with orc files right now

"""
MISSING = '-999'
dir = os.path.dirname(__file__)
#os.path.join(dir,nfile)
#filename = 'ntdrain.orc'

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
    outhead1 = f_lines[0].rstrip('\n')
    outhead2 = f_lines[1].rstrip('\n')
    alldata_list.append([outhead1])
    alldata_list.append([outhead2])
    outid = f_lines[2][:13]
    alldata_list.append([outid])
    alldata_list.append(['========DO NOT EDIT ABOVE THIS LINE========='])
    headline = f_lines[2]

    #Get headers and column count
    #print "it started"
    headline_list = []
    headline_list.append("")
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
    print "Completed."

def main():
    alldata_list = parse_warmf_file(filename)
    writeWARMFtoCSV(alldata_list)
    
if __name__ == '__main__':
    main()
