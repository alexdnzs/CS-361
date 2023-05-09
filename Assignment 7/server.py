# Alexander Salgado

#  Server in Python
#   
# IN ORDER TO SEND DATA, EXECUTE SERVER FILE FIRST TO TURN "SERVER" ON

import time
import zmq
from get_user_year import import_birthyear

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print(message)
    
    #if request was received from client
    if message:
        print(f"Received Data request from client!")

        #  Do some 'work'
        time.sleep(1)

        birth_year = import_birthyear()

        #  Send reply back to client
        socket.send_string(birth_year)
        print(f"Message sent back to client!")

    
    