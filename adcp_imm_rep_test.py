import cgserial as ser
from datetime import datetime
import time

def run_test(buoy_port, adcp_port):
    """Send samples to adcp. Get samples from buoy. Repeat"""

    #Establish contact with virtual adcp...
    adcp_log = open(("adcp-%s.log" % datetime.today().strftime("%Y%m%d")), "wb")
    adcp = ser.open_port(adcp_port, 9600, 3)
    if not adcp:
        return "Error! Unable to connect to ADCP."

    # Establish contact with virtual buoy...
    buoy_log = open(("buoy-%s.log" % datetime.today().strftime("%Y%m%d")), "wb")
    buoy = ser.open_port(buoy_port, 9600, 3)
    if not buoy:
        return "Error! Unable to connect to Buoy."

    # Talk to the adcp for a bit...
    print("Identifying the ADCP...")
    ser.cmd_and_reply(adcp, adcp_log, "pwron")
    ser.cmd_and_reply(adcp, adcp_log, "gethd")
    ser.cmd_and_reply(adcp, adcp_log, "getcd")

    print("Erasing the buffer...")
    ser.cmd_and_reply(adcp, adcp_log, "sampleeraseall")

    # START A LOOP HERE!
    #
    test_in_progress = True
    while test_in_progress:
        ser.cmd_and_reply(adcp,adcp_log, "pwron")
        # Example ADCP data sample...
        print("Making a sample now...")
        ser.cmd_and_reply(adcp,adcp_log, "sampleadd")
        ser.cmd_and_reply(adcp,adcp_log, """2016/01/29 21:26:12.97 00001
Hdg: 352.3 Pitch: -1.2 Roll: -3.1
Temp: 23.4 SoS: 1530 BIT: 00
Bin    Dir    Mag     E/W     N/S    Vert     Err   Echo1  Echo2  Echo3  Echo4
  1   88.3  104.0     104       3       0     103    111    109    103     99
  2     --     --  -32768  -32768  -32768  -32768     72     72     88     89
  3     --     --  -32768  -32768  -32768  -32768     69     68     74     73
  4     --     --  -32768  -32768  -32768  -32768     69     67     72     70
  5     --     --  -32768  -32768  -32768  -32768     69     66     71     70
  6     --     --  -32768  -32768  -32768  -32768     69     67     71     69
  7     --     --  -32768  -32768  -32768  -32768     69     67     71     69
  8     --     --  -32768  -32768  -32768  -32768     69     67     71     69
  9     --     --  -32768  -32768  -32768  -32768     69     67     71     69
 10     --     --  -32768  -32768  -32768  -32768     68     68     71     68
 11     --     --  -32768  -32768  -32768  -32768     68     67     72     69
 12     --     --  -32768  -32768  -32768  -32768     69     67     70     69
 13     --     --  -32768  -32768  -32768  -32768     68     66     70     68
 14     --     --  -32768  -32768  -32768  -32768     69     67     71     69
 15     --     --  -32768  -32768  -32768  -32768     70     67     70     69
 16     --     --  -32768  -32768  -32768  -32768     69     67     71     69
 17     --     --  -32768  -32768  -32768  -32768     69     67     70     70
 18     --     --  -32768  -32768  -32768  -32768     70     67     71     69
 19     --     --  -32768  -32768  -32768  -32768     69     67     71     69
 20     --     --  -32768  -32768  -32768  -32768     69     67     71     70
 21     --     --  -32768  -32768  -32768  -32768     68     67     72     69
 22     --     --  -32768  -32768  -32768  -32768     68     67     71     69
 23     --     --  -32768  -32768  -32768  -32768     69     67     70     69
 24     --     --  -32768  -32768  -32768  -32768     69     67     71     69
 25     --     --  -32768  -32768  -32768  -32768     69     67     70     69
 26     --     --  -32768  -32768  -32768  -32768     68     66     71     69
 27     --     --  -32768  -32768  -32768  -32768     69     68     72     69
 28     --     --  -32768  -32768  -32768  -32768     69     66     71     69
 29     --     --  -32768  -32768  -32768  -32768     68     68     71     69
 30     --     --  -32768  -32768  -32768  -32768     69     67     72     69""")
        ser.cmd_and_reply(adcp,adcp_log, "pwroff")
        print("Sampling complete, back to sleep...")
        # Wait a few seconds, then wake up the buoy...
        time.sleep(5)

        ser.cmd_and_reply(buoy, buoy_log, "pwron")
        print("Begin buoy communication...")
        # Contact the adcp over inductive line, get sample...
        ser.cmd_and_reply(buoy, buoy_log, "fcl")
        print("Capturing inductive line...")
        ser.cmd_and_reply(buoy, buoy_log, "sendwakeuptone")
        ser.cmd_and_reply(buoy, buoy_log, ("!%sgethd" % iid))
        ser.cmd_and_reply(buoy, buoy_log, ("!%ssamplegetsummary" % iid))
        print("Requesting sample from ADCP...")
        ser.cmd_and_reply(buoy, buoy_log, ("!%ssamplegetlast" % iid))
        ser.cmd_and_reply(buoy, buoy_log, ("!%ssampleeraseall" % iid))
        ser.cmd_and_reply(buoy, buoy_log, "pwroff")
        print("Powering off...")
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
