import imm
import cgserial as ser

#port = ser.select_port_win()
#conn = ser.open_port(port, "9600")

user_response = raw_input("How many UIMMs have you?")

raw_input("Are all id's set consecutively starting with 01? Press 'Enter' to continue...")
iids = [*range(1, user_response+1)]
imm.num_to_id(iids)

for iid in iids
    print("Looking for UIMM id%s..." % iid)
