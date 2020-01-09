#We need import the Python socket library
import socket

#What is my local hostname ?
myHostName = socket.gethostname()
print("Name of  {}" .format(myHostName))

#What is my ip address of local host ?
MyHostIP = socket.gethostbyname(myHostName)
print("IP of the local host {}" .format(MyHostIP))
