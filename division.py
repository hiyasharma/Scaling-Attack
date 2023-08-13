import os

files=[]


for file in os.listdir():
    if file=="encrypter.py" or file== "key.key" or file == "decrypter.py" or file == "imagebinary.py" or file == "dividedbynandk.bat" or file == "division.py":
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as x:
        y = x.read()
        with open("dividedbynandk.bat", "w+") as nandk:
            n=int(input("Enter the value for N: "))
            max_len=n
            empty_str=''
            for i in y:
                empty_str+=str(i)
                if len(empty_str) == max_len:
                    print(empty_str)
                    nandk.write(empty_str)
                    empty_str=''
