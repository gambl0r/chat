import zmq
import time
import sys

print("Current libzmq version is %s" % zmq.zmq_version())
print("Current pyzmq version is %s" % zmq.__version__)

port = "55666"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)


while True:
    #  Wait for next request from client
    try:
        message = socket.recv_json(zmq.NOBLOCK)
        print "Received request: ", message
        socket.send_json({"msg": "World", "port":port})
    except zmq.ZMQError:
        pass
    time.sleep(0.2)  
    