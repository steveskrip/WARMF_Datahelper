import csv
import os
from datetime import datetime
from dateutil.parser import parse

dir = os.path.dirname(__file__)

filename = 'ntdrain.csv'
outfile = 'ntdrain.CHG'

def parse_csv_file(filename):
    f = open(os.path.join(dir,filename),'rb')
    reader = csv.reader(f,delimiter=',')
    o = open(os.path.join(dir,outfile),'w')
    
    for i,line in enumerate(reader):
        print i
        if i == 0:   
            print "case 0"
            #write Version line
            o.write(line[0]+"\n")
        elif i==1:
            print "case 1"
        #write Lat long line
            o.write(line[0]+"\n")
        elif i==2:
            print "case 2"
            #write header row
            o.write(line[0].rjust(13))
        elif i==3:
            print "case 3"
            #skip next row 
            pass
        elif i==4:
            print "case 4"
            #Write header row
            head = line
            for k, col in enumerate(head):
                if k == 0:
                    pass
                else:
                    o.write((col).ljust(8))
            o.write('\n')
        else:
            for j, col in enumerate(line):
                #parse date
                if j==0:
                    print col
                    datefmt = parse(col)
                    o.write(datetime.strftime(datefmt,"%d%m%Y").ljust(8))
                    o.write('0000'.rjust(5))
                #write notes colums
                elif j==(len(line)-1):
                    o.write((col))
                #write everything else
                else:
                    o.write((col).rjust(8))
            o.write('\n')
    f.close()
    o.close()
def main():
    parse_csv_file(filename)

if __name__ == "__main__":
    main()
