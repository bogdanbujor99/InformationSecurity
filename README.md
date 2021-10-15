## Requirement: ##
![tema_1_SI_2021_miercuri pdf - Google Chrome 10_15_2021 3_53_17 PM](https://user-images.githubusercontent.com/79144278/137490103-66dbf1fd-158e-431f-a19a-9a802ab661a4.png)
## Description of the working medium: ##
The programming language I used is python. <br />
I used the pyaes and pycryptodome libraries. <br />
The pyaes library was used for random generation. <br /> 
The pycryptodome was used for AES algorithm.
```
pip install pycryptomode
pip install pyaes
```
## Descriptionof solving the problem ##
The first step was to write algorithms for the ECB and OFB. The text has been split into 16 bytes pieces and then the pieces has been encrypted. The same thing with the decryption, I splitted the ciphertext into 16 bytes blocks and decrypted them.
