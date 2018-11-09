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
            PHSENRecord.__init__(self, hexstring[15:])

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

class PHSENRecord(SAMIRecord):
    """A PHSEN data record"""

    def __init__(self, hexstring):
        self.name = "The PHSEN known as %s" % self.sami
        self.batt = int(hexstring[440:444], 16) / 4096 *15
        self.temp1 = int(hexstring[:4], 16)
        self.temp2 = int(hexstring[444:448], 16)

    def proc_temp(self):
        """Process temperature data to output mean T(deg C)"""
        Rt1 = (self.temp1 / (4096 - self.temp1)) * 17400
        invT1 = 0.0010183 + 0.000241 * (math.log(Rt1)) + 0.00000015 * (math.log(Rt1))^3
        tempK1 = 1 / invT1
        tempC1 = tempK1 - 273.15
        tempF1 = 1.8 * tempC1 +32
        tempFinal1 = tempC1

        Rt2 = (self.temp2 / (4096 - self.temp2)) * 17400
        invT2 = 0.0010183 + 0.000241 * (math.log(Rt2)) + 0.00000015 * (math.log(Rt2))^3
        tempK2 = 1 / invT2
        tempC2 = tempK2 - 273.15
        tempF2 = 1.8 * tempC2 +32
        tempFinal2 = tempC2

        temp = (tempFinal1 + tempFinal2) /2
        return temp
        
class PCO2WRecord:
    """A PCO2W data record, not a blank"""

    pass


