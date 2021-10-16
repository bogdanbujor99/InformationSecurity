## Requirement: ##
![tema_1_SI_2021_miercuri pdf - Google Chrome 10_15_2021 3_53_17 PM](https://user-images.githubusercontent.com/79144278/137490103-66dbf1fd-158e-431f-a19a-9a802ab661a4.png)
## Description of the working medium: ##
The programming language I used is python. <br />
I used the pyaes and pycryptodome libraries. <br />
The pycryptodome library was used for random generation. <br /> 
The pyaes library was used for AES algorithm.
```
pip install pycryptomode
pip install pyaes
```
## Description of solving the problem ##
The first step was to write algorithms for the ECB and OFB. The text has been split into 16 bytes pieces and then the pieces has been encrypted. The same thing with the decryption, I splitted the ciphertext into 16 bytes blocks and decrypted them. If after splitting the block has less than 16 bytes, I complete it as long as it has less than 16 bytes with null bytes. With the help of get_random_bytes() function I generate a IV. <br />
The second step was to write two classes, one for MC node and one for the A and B nodes. <br />
The nodeMC class is the manager and has a "k1" key for ECB mode and a "k2" key for OFB mode. The common "k" key is used by all classes. With the help of get_random_bytes() function I generate the "k1" and "k2" keys. The getk1 and getk2 send the desired key encrypted with AES and the "k" key. <br />
When "A" wants to start communicating with "B", I call the sendMode method where I set the desired mode, the B node and MC. In this method if I set the mode to "ECB" I request from MC the k1 else I request the k2. I call the getMode method for the B node where I request the specific key from MC. After node B obtains the key and decrypts it, it returns the message "start" to node A. The A node reads a content of a file and it encrypts the content in the chosen mode together with the "k" key from the MC. The B node receives the encrypted text and decrypts it with the k1/k2 key and the selected mode and finally displays the decrypted text.
