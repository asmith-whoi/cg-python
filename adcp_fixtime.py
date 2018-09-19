"""
Applies time offsets (full hours) in BBConv ADCP files to correct
for instruments set to the wrong time, e.g. local time instead of
UTC.

Usage - call from the command line:
python adcp_fixtime.py OFFSET INFILE OUTFILE

OFFSET - int, offset to apply in number of hours
INFILE - csv file, created by BBConv utility
OUTFILE - name of file to be created containing corrected data, 
suited for conversion by BBMerge utility
"""
from datetime import datetime
from datetime import timedelta
import sys
import csv

offset = int(sys.argv[1])
infile = sys.argv[2]
outfile = sys.argv[3]

newdates = []
with open(infile, "r") as csv_in:
    reader = csv.reader(csv_in)
    for row in reader:
        row = [int(d) for d in row]
        rowdate = datetime(*row)

        newdate = rowdate + timedelta(hours=offset)


        newdates.append([newdate.year, newdate.month, newdate.day, newdate.hour, newdate.minute, newdate.second, newdate.microsecond])



with open(outfile, "w") as newfile:
    writer = csv.writer(newfile, quoting=csv.QUOTE_NONE)
    writer.writerows(newdates)
            
    
