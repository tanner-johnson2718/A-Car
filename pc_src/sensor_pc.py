# Read json data from car sensor stream. Display data on terminal as it becomes
# available.

# 

# import packages to read and parse data from sensor stream
import socket
import fcntl
import json

# import packages to display sensor data graphically
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# sensor stream IP and port
HOST = "192.168.8.1"
# HOST = "127.0.0.1"
PORT = 8091 

# set up
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

print("Press Ctrl-C to exit")

# header
print("   Accel XYZ (m/s^2) |"
      "    Gyro XYZ (deg/s) |", end='')
print("  Mag Field XYZ (uT) |", end='')
print(' Temp (C)')

try:    # keep running

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        def animate(i):
            data = json.loads(s.recv(1024))
            print(('\r{0[0]:6.2f} {0[1]:6.2f} {0[2]:6.2f} |'
                   '{1[0]:6.1f} {1[1]:6.1f} {1[2]:6.1f} |'
                   '{2[0]:6.1f} {2[1]:6.1f} {2[2]:6.1f} |'
                   '   {3:6.1f}').format(data['accel'],
                                         data['gyro'],
                                         data['mag'],
                                         -1),
                  end='')
            
            ax.clear()
            ax.set_xlim([-25, 25])
            ax.set_ylim([-25, 25])
            ax.set_zlim([-25, 25])
            ax.quiver([0,0], [0,0], [0,0],
                      [data['accel'][0], data['gyro'][0]], 
                      [data['accel'][1], data['gyro'][1]], 
                      [data['accel'][2], data['gyro'][2]])
            return ax,

        anim = animation.FuncAnimation(fig, animate, interval=5, blit=True)
        plt.show()


except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\nExiting...")