import cgserial as ser

port = ser.select_port_win()
conn = ser.open_port(port, "9600")

tot_uimm = raw_input("How many UIMMs have you?")
raw_input("Are all id's set consecutively starting with 01? Press enter to continue...")


