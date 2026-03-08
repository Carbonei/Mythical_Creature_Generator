import zmq 
import time
from PIL import Image
context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect("tcp://localhost:4444")


socket.send_string("1")

name = socket.recv()
print(name.decode())
socket.send_string("ready for origin")
time.sleep(0.6)

origin = socket.recv()
print(origin.decode())

time.sleep(0.6)

socket.send_string("ready for file name")
file = socket.recv()
file_path = file.decode()

img = Image.open(file_path, mode = 'r')
img.show()
time.sleep(5)

socket.send_string("Q") 
