from ctypes import sizeof
import time

# import python socket library to host sensor server
import socket
import json

# init server
HOST = "192.168.8.1"
PORT = 8092
try:    # keep running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Control Service Connected by {addr}")
            while True:
                # Loop
                data = s.recv(4)
                print(data[0:2])
                print(data[2:4])
                print()
                    
except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\nControl Service Exitting!")