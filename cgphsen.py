import cgutil
from cgsami import SAMIRecord

def load_log_file(infile):
    lines = cgutil.dlog_scrub_logfile_asc(infile)

    phsamples = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("*") and lines[i][5:7] == "0A":
            sample = ""
            while True:
                try:
                    sample = sample + lines[i]
                except IndexError:
                    break
                i = i+1
                if  len(sample) == 465:
                    phsamples.append(sample)
                    break
                
        else:
            i = i + 1

    return phsamples

def load_phsamples(samples):
    phrecords = []
    for sample in samples:
        phrecord = SAMIRecord(sample)
        phrecords.append(phrecord)
    return phrecords
