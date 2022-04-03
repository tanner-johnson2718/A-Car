# import python socket library to host sensor server
import socket

# init server
HOST = "192.168.8.1"
PORT = 8092
try:    # keep running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Control Service Connected by " + str(addr))
            while True:
                # Loop
                data = conn.recv(4)

                id = data[0]
                val = data[2] + (data[3] << 8)

                # signed short
                if (val >> 15) & 1:
                    val = val - (1<<16)

                # normalize
                val = float(val + (1 << 15)) / float(1<<16)
                
                
                print("ID="+str(id)+" VAL="+str(val))
                    
except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\nControl Service Exitting!")