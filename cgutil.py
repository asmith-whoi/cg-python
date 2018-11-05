"""
Helper modules for CGSN python scripts.
"""

def prompt_integer(user_prompt, bounds=None):
    """ 
    Prompts for user input, then validates that input is
    an integer and is in bounds. If bounds is not specified,
    then any integer will be valid.

    Params:
        user_prompt - Text to display to user
        bounds - list or range
    Returns:
        int
    """
    while True:
        try:
            user_response = int(input("%s " % user_prompt))
        except ValueError:
            print("Whoa! That's not a number.")
            continue
        if bounds is None:
            break
        if not user_response in bounds:
            print("Whoa! That's out of range.")
            continue
        break
    return user_response

def dlog_scrub_logfile_asc(infile):
    """
    Takes a dcl ascii data log file and removes timestamp and other
    messages added by the datalogger, hopefully leaving only instrument
    output. Returns a list of lines.
    """
    newlines = []
    with open(infile, "r") as lines:
        for line in lines:
            line = line[24:].strip()
            if line.startswith("["):
                continue            
            newlines.append(line)
        return newlines
    
def write_scrubbed_logfile(infile):
    newlines = dlog_scrub_logfile_asc(infile)
    
    outfile = "%s_asc.txt" % infile[:-4]
    with open(outfile, "w") as newfile:
        for line in newlines:
            newfile.write(line)
