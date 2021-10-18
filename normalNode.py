from ecb import Bytes_16_decrypted_ECB, ecb_encrypted
from ofb import Bytes_16_decrypted_OFB, ofb_encrypted
import pyaes

class normalNode:
    def __init__(self):
        self.k = "abcdefg123456789".encode()
        self.ciphertext = []
        self.finalMessage = ""

    def criptoECB(self,node):
        f = open("file.txt", "r")
        plaintext = f.read()
        cipherText = []
        for i in range(0,len(plaintext),16):
            bytes_16 = plaintext[i:i+16]
            cipherText = ecb_encrypted(bytes_16,self.k_mode)
            self.sendCripto(node,cipherText)
        node.decripto()

    def sendCripto(self,node,ciphertext):
        node.getCripto(ciphertext)

    def getCripto(self,ciphertext):
        self.ciphertext = self.ciphertext + ciphertext

    def criptoOFB(self,node):
        f = open("file.txt", "r")
        plaintext = f.read()
        ciphertext = []
        for i in range(0,len(plaintext),16):
            bytes_16 = plaintext[i:i+16]
            ciphertext = ofb_encrypted(bytes_16,self.k_mode)
            self.sendCripto(node,ciphertext)
        node.decripto()    


    def decripto(self):
        print(self.ciphertext)
        if(self.mode=="ECB"):
            self.finalMessage = Bytes_16_decrypted_ECB(self.ciphertext,self.k_mode)
            print(self.finalMessage)
        else:
            self.finalMessage = Bytes_16_decrypted_OFB(self.ciphertext,self.k_mode)
            print(self.finalMessage)

    def getMode(self,mode,MC):
        self.mode=mode
        k_mode = 0
        if(self.mode=="ECB"):
            k_mode = MC.getK1()
        else:
            k_mode = MC.getK2()
        aes = pyaes.AES(self.k)
        self.k_mode = bytes(aes.decrypt(k_mode))
        return "start"

    def sendMode(self,mode,node,MC):
        self.mode=mode
        k_mode = 0
        if(self.mode=="ECB"):
            k_mode = MC.getK1()
        else:
            k_mode = MC.getK2()
        aes = pyaes.AES(self.k)
        self.k_mode = bytes(aes.decrypt(k_mode))
        if(node.getMode(mode,MC)=="start"):
            if(self.mode=="ECB"):
                self.criptoECB(node)
            else:
                self.criptoOFB(node)