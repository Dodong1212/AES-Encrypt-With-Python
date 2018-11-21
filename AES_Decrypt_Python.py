import sys
import os
import struct, hashlib, time
import binascii
from Crypto.Cipher import AES

def decrypt_file(key, in_filename, out_filename, chunksize=24 * 1024):

    #Open Input-File read & binary mode
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        #Open Input-File Write & binary mode
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)

def make_pass():
    timekey = int(time.time())
    return str(timekey)

def main():
    # Get PATH
    PATH = sys.argv[1]
    
    file_list = []

    #password = make_pass()

    #Make custom Password - Encryption must match password.
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

            original_file_name = os.path.splitext(in_file)[0]
            
            if extension == '.enTEST':
                decrypt_file(key,in_filename=in_file, out_filename=original_file_name)
                os.remove(in_file)
                print(in_file+" Decryption!!")
            else:
                pass

if  __name__ == '__main__':
   main()
