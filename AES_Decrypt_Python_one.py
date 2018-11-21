import win32con, win32api,os
import struct, hashlib, time
import binascii
import sys
import tempfile
import Tkinter as tk
from Crypto.Cipher import AES
from tkFileDialog import askopenfilename

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
            
        #Change the file format to read mode
        win32api.SetFileAttributes(out_filename,1)
        
def make_pass():
    timekey = int(time.time())
    return str(timekey)

def main():   
    #password = make_pass()

    #Make custom Password
    password = "sdagdafdsafds"

    #Make Key With SHA256
    key = hashlib.sha256(password).digest()


    #Right-click on the mouse and set it as the drive letter in arv[1].
    Drive_name = sys.argv[1]
    Drive_name = Drive_name[0:2]

    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()

    #Select the file you want to be decrypted
    in_file = askopenfilename(initialdir = Drive_name,title = "Choose FIle",filetypes = (("Encrypt File","*.enTest"),("all file","*.*")))
    extension = os.path.splitext(in_file)[1]
    original_file = os.path.splitext(in_file)[0]
    original_file_extension = os.path.splitext(original_file)[1]

    #Creating in temporary file format
    temp_file = tempfile.mkstemp(suffix=original_file_extension)

    if extension == '.enTEST':
        decrypt_file(key,in_filename=in_file, out_filename=temp_file[1])
        os.startfile(temp_file[1])
main()
