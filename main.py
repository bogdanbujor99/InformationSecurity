from nodeMC import nodeMC
from normalNode import normalNode

MC = nodeMC()
A = normalNode()
B = normalNode()
#A.sendMode("OFB",B,MC)
A.sendMode("ECB",B,MC)