import os

from cryptography.fernet import Fernet


files=[]


for file in os.listdir():
    if file=="encrypter.py" or file== "key.key" or file == "decrypter.py" or file=="imagebinary.py" or file == "division.py" or file == "dividedbynandk.bat":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Decryption done for: ", files)



with open("key.key", "rb") as keykey:
    sem = keykey.read()


for file in files:
    with open(file, "rb") as x:
        y = x.read()
    z = Fernet(sem).decrypt(y)
    with open(file, "wb") as x:
        x.write(z)



        
        
    
    
