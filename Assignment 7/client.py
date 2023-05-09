# Alexander Salgado

#   Client in Python
#   Connects REQ socket to tcp://localhost:5555
#   
# In order to make a call, import client.py file and return_year function
# returns birthyear in form of a string - recommend converting to int, if you need to 
# function was implemented to allow for return of value easily, if not allowed, writing
# to a text file could be an option to return the data.


import zmq

def return_year():
    context = zmq.Context()

#  Socket to talk to server
    print("Connecting to server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")


    print(f"Sending Data Request to Server!")
    socket.send(b"Hello")

    #  Get the reply.
    birthyear = socket.recv()

    #convert the received message from type BYTE to STR
    birthyear = str(birthyear, 'utf-8')
    print(f"Received birthyear Data - {birthyear}")


    return birthyear

#testing
user_input = input('Request birth year? (Y or N) - ')

if user_input == "Y":
   return_year()
