"""
Generic parser for SAMI hex records
"""
from datetime import datetime as dt
from datetime import timedelta as td

class SAMIRecord:
    """A SAMI data or control record"""

    origin = dt(1904, 1, 1)
    rectypes = {"04":"CO2 Measurement", "05":"CO2 Blank",
                "0A":"pH Measurement",
                "80":"Launch",
                "81":"Measurement Start",
                "83":"Good Shutdown",
                "85":"Handshake On"}

    def __init__(self, hexstring):
        self.sami = hexstring[1:3]
        self.hexlength = hexstring[3:5]
        self.hexrectype = hexstring[5:7]
        self.hextimestamp = hexstring[7:15]
        self.hexstringlen = len(hexstring)
        self.length = int(self.hexlength, 16) * 2 + 3
        self.rectype = SAMIRecord.rectypes.get(self.hexrectype)

        if self.hexrectype == "0A":
            PHSENRecord.__init__(self, hexstring[16:])

        if self.hexrectype == "04":
            PCO2WRecord.__init__(self)

    def telltime(self):
        """Return human-readable timestamp for this record"""
        delta = td(seconds=int(self.hextimestamp, 16))
        return dt.strftime((SAMIRecord.origin + delta), "%m/%d/%Y %H:%M:%S")
    
    def describe(self):
        """Return a lovely sentence telling about this record"""
        return "SAMI: %s Record Type: %s Record Length: %s Timestamp: %s" % (self.sami, self.rectype, self.length, self.telltime())

    def checklen(self):
        """Boolean. Test expected length of record against the actual length."""
        result = False
        if self.hexstringlen == self.length:
            result = True
        return result

class PHSENRecord:
    """A PHSEN data record"""

    def __init__(self, hexstring):
        self.name = "The PHSEN known as %s" % self.sami

class PCO2WRecord:
    """A PCO2W data record, not a blank"""

    pass


