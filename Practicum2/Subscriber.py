from mosquitto import *
from serial import *
from random import *

# FULL DEVICE NAME can be found by running: python PortScanner.py
# SPEED is usually 115200 for Microbit and 9600 for Arduino

port = Serial("COM5",9600,timeout=2) 

randomID = random()
client = Mosquitto("Wendy" + str(randomID))
client.connect("127.0.0.1")

# The rest of your code goes in here !!!
 
client.subscribe("/lights")

def messageReceived(broker, obj, msg):
    global client
    payload = msg.payload.decode() + "\n"
    print("Message " + msg.topic + " containing: " + payload)
    port.write(payload.encode())

client.on_message = messageReceived

while (client != None): client.loop()
    
port.readall()

