import serial
from serial.tools import list_ports

class Cgserial:
    """
    Serial communication tools
    """

    def __init__(self):
        pass
    
    def select_port_win(self):
        """
        WINDOWS ONLY --
        Display a list of available ports and prompt the user to
        select which to use. If only one port is available, that one
        will be used automatically, with no prompt.
        """
        while True:
            ports = list_ports.comports()
            if len(ports) == 0:
                print("There don't seem to be any available serial ports.")
                selection = input("Would you like to connect a serial device and try again? [y]/n ")
                if selection != "n":
                    input("Connect your device now, then press ENTER to continue...")
                else:
                    return None
            else:
                break

        if len(ports) == 1:
            return ports[0][0]
        while True:
            print("Available ports:")
            for n, port in enumerate(ports, 1):
                print("%d) %s" % (n, port))
            # Input testing -- input has to be a number.
            while True:
                try:
                    selection = int(input("Enter your selection: "))
                except ValueError:
                    print("Whoa! That's not a number.")
                    continue
                break

            # Input testing -- input has to be in list_ports range.
            try:
                return ports[selection-1][0]
            except IndexError:
                print("Whoa! That's not an available port.")


    def open_port(self, port, baudrate, t):
        """
        Open a serial connection.

        port - COM port or device to open
        baudrate - baud rate
        t - timeout value in seconds
        
        Returns a new connection.
        """
        print("Connecting to %s at %d baud..." % (port, baudrate))
        try:
            conn = serial.Serial(port, baudrate, timeout=t)
            print("Connected to %s." % port)
            return conn
        except Exception as exc:
            print(("Oops! Something happened: %s" % exc))
            return None

    def cmd_reply(self, conn, capfile, cmd):
        """
        Transmit a message over a serial connection,
        capture the received input and write the input to the capfile.

        conn - an open pySerial connection
        capfile - an open file
        cmd - message string to transmit

        Returns the received message string.
        """
        conn.reset_input_buffer()
        conn.write(cmd.encode('ascii')+b'\r\n')
        cap = conn.read(conn.in_waiting)
        while True:
            prev = cap
            cap += conn.read(1)
            if prev == cap:
                capfile.write(cap)
                return cap

            
