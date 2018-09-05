import imm
from datetime import datetime

import cg_util as cu
#import cgserial as ser

#port = ser.select_port_win()
#conn = ser.open_port(port, "9600")

input("Are all id's set consecutively starting with 01? Press 'Enter' to continue...")

validated_input = cu.prompt_integer("How many UIMM have you?",range(1,100))
iids = [*range(1,validated_input+1)]
imm.num_to_id(iids)

# Let's make log files for each id...
logdir = datetime.today().strftime("%Y%m%d")

for iid in iids:
    print("Opening ID%s_logfile.txt..." % iid)
