import cgserial as ser
from datetime import datetime

def run_test(buoy_port, adcp_port):
    """Send samples to adcp. Get samples from buoy. Repeat"""

    #Establish contact with virtual adcp...
    adcp_log = open(("adcp-%s.log" % datetime.today().strftime("%Y%m%d")), "w")
    adcp = ser.open_port(adcp_port, 9600)
    if not adcp:
        return "Error! Unable to connect to ADCP."

    # Establish contact with virtual buoy...
    buoy_log = open(("buoy-%s.log" % datetime.today().strftime("%Y%m%d")), "w")
    buoy = ser.open_port(buoy_port, 9600)
    if not buoy:
        return "Error! Unable to connect to Buoy."

    # Talk to the adcp for a bit...
    print("Identifying the ADCP...")
    ser.cmd_and_reply(adcp, adcp_log, "gethd")
    ser.cmd_and_reply(adcp, adcp_log, "getcd")

    print("Erasing the buffer...")
    ser.cmd_and_reply(adcp, adcp_log, "sampleeraseall")

    # START A LOOP HERE!
    #
    #
    #
    #
    
# ### Main Program Loop ###
time_to_quit = False
buoy_port = False
adcp_port = False
iid = "10"

while not time_to_quit:
    print("\r\nADCP Inductive Stress Test")
    print("MAIN MENU")
    print("---------")
    print("1) Begin Test")
    print("2) Exit")
    selection = input("Enter your selection: ")
    if selection == '1':
        if not buoy_port:
            input("Select COM port for the virtual Buoy. (Press ENTER to continue)")
            buoy_port = ser.select_port_win()
            if not buoy_port:
                continue
        if not adcp_port:
            input("Select COM port for the virtual ADCP. (Press ENTER to continue)")
            adcp_port = ser.select_port_win()
            if not adcp_port:
                continue
        while True:
            print(run_test(buoy_port, adcp_port))
            again = input("Would you like to test again? y/[n] ")
            if again != "y":
                break
            input("Type ENTER to begin the next test...")
    elif selection == '2':
        time_to_quit = True
        print("Good bye!")
    else: print("Error! Invalid entry.\r\n")
