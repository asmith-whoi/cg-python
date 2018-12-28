from cgserial import Cgserial

class Qct:
    """A QCT test procedure"""

    def __init__(self):
        pass

    def run_test(self, test_name, test_version):
        # ---- Main program loop ----
        while not time_to_quit:
            print("\r\n%s QCT v%s" % (test_name, test_version)
            print("MAIN MENU")
            print("---------")
            print("1) Test an instrument")
            print("2) Configure serial port")
            print("3) Exit")
            selection = input("Enter your selection: ")
            if selection == '1':
                if not port:
                    port = select_port()
                    if not port:
                        continue
                username = input("What is your name?: ")
                while True:
                    formnumber = set_formnumber(formnumber)
                    print(ctdmo_qct_test(port, username, formnumber))
                    again = input("Would you like to test another instrument? y/[n] ")
                    if again != "y":
                        formnumber = None
                        break
                    input("Type ENTER to begin the next test...")
            elif selection == '2':
                port = select_port()
                print("Selected port is %s." % port)
            elif selection == '3':
                time_to_quit = True
                print("Good bye!")
            else: print("Error! Invalid entry.\r\n")
