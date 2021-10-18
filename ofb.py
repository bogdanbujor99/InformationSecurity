import pyaes
from Crypto.Random import get_random_bytes
array_encrypt = []
array_decrypt = []
iv = get_random_bytes(16)

def ofb_encrypted(plaintext,key):
    global array_encrypt
    global array_decrypt
    array_decrypt = []
    aes = pyaes.AES(key)
    if(len(array_encrypt)==0):
        array_encrypt = aes.encrypt(iv)
    else:
        array_encrypt = aes.encrypt(array_encrypt)
    plaintext_bytes = plaintext.encode()
    if(len(plaintext_bytes)<16):
            for j in range(len(plaintext_bytes),16):
                plaintext_bytes +=  b'\x00'
    ciphertext = [x ^ y for (x, y) in zip(array_encrypt, plaintext_bytes)]
    return ciphertext

def ofb_decrypted(ciphertext,key):
    global array_decrypt
    global array_encrypt
    array_encrypt = []
    aes = pyaes.AES(key)
    if(len(array_decrypt)==0):
        array_decrypt = aes.encrypt(iv)
    else:
        array_decrypt = aes.encrypt(array_decrypt)

    decrypted = [x ^ y for (x, y) in zip(array_decrypt, ciphertext)]
    return bytes(decrypted).decode()


def Bytes_16_encrypted(plaintext,key):
    cipherText = []
    for i in range(0,len(plaintext),16):
        bytes_16 = plaintext[i:i+16]
        cipherText = cipherText + ofb_encrypted(bytes_16,key)
    return cipherText

def Bytes_16_decrypted_OFB(cipherText,key):
    finalMessage = ""
    for i in range(0,len(cipherText),16):
        bytes_16 = cipherText[i:i+16]
        finalMessage += ofb_decrypted(bytes_16,key)
    return finalMessage

