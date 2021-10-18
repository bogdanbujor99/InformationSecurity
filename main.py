from nodeMC import nodeMC
from normalNode import normalNode

MC = nodeMC()
A = normalNode()
B = normalNode()
A.sendMode("OFB",B,MC)
B.sendMode("ECB",A,MC)