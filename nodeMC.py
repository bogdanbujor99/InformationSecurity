from Crypto.Random import get_random_bytes
import pyaes

class nodeMC:
    def __init__(self):
        self.k = "abcdefg123456789".encode()
        self.k1 = get_random_bytes(16)
        self.k2 = get_random_bytes(16)

    def getK1(self):
        aes = pyaes.AES(self.k)
        return aes.encrypt(self.k1)
 
    def getK2(self):
        aes = pyaes.AES(self.k)
        return aes.encrypt(self.k2)