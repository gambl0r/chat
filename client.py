import zmq
import sys

print("libzmq version: %s" % zmq.zmq_version())
print("pyzmq version:  %s" % zmq.__version__)

port = "55666"

# Client is created with a socket type "zmq.REQ"
# You should notice that the same socket can connect to two different servers.

context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:%s" % port)

# You have to send a request and then wait for reply.

#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print "Sending request ", request,"..."
    socket.send_json({"msg": "HELO"})
    
    # sockets have send, send_json, send_pyobj
    #         +    recv, recv_json, recv_pyobj
    # Compression done manually w. compression libs
    
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"

