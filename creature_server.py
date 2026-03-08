import time
import zmq 
import json
import random

#set up communication
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:4444")

#loop for communication
while True:
    #get communication
    communication = socket.recv()

    #Get Positive message
    if len(communication) > 0:
        #quit on Q
        if communication.decode() == 'Q': 
            break
        index = random.randint(0, 9)
        #if not Q than choose creature
        with open('creatures.json', 'r') as file:
            data = json.load(file)
            #print(type(data))
            message = data[index]       
        
    time.sleep(0.5)
    #Prepare and send components
    name = message["name"]
    name = str(name)
    socket.send_string(name)
    time.sleep(0.5)
    
    ready = socket.recv()
    origin = message["origin"]
    origin = str(origin)
    socket.send_string(origin)
    time.sleep(0.5)

    ready = socket.recv()
    file_name = message["image"]
    file_name = str(file_name)
    socket.send_string(file_name)

#end communication
context.destroy()
