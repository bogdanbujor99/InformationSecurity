import pyaes

def ecb_encrypted(plaintext,key):
    plaintext_bytes = plaintext.encode()
    if(len(plaintext_bytes)<16):
            for j in range(len(plaintext_bytes),16):
                plaintext_bytes +=  b'\x00'
    aes = pyaes.AES(key)
    return aes.encrypt(plaintext_bytes)

def Bytes_16_encrypted(plaintext,key):
    cipherText = []
    for i in range(0,len(plaintext),16):
        bytes_16 = plaintext[i:i+16]
        cipherText = cipherText + ecb_encrypted(bytes_16,key)
    return cipherText

def ecb_decrypted(cipherText,key):
    aes = pyaes.AES(key)
    decrypted = aes.decrypt(cipherText)
    return bytes(decrypted).decode()

def Bytes_16_decrypted_ECB(cipherText,key):
    finalMessage = ""
    for i in range(0,len(cipherText),16):
        bytes_16 = cipherText[i:i+16]
        finalMessage += ecb_decrypted(bytes_16,key)
    return finalMessage