import os
import sys
import struct, hashlib, time
import binascii

def allfiles(path):
    res = []

    for root, dirs, files in os.walk(path):
        rootpath = os.path.join(os.path.abspath(path), root)

        for file in dirs:
            filepath = os.path.join(rootpath, file)
            res.append(filepath)

    return res

def main():

    #Set DIR PATH
    PATH = '/home/block/Server'
    command_start_list=[]
    file_list=[]

    # Get list of files
    file_list=allfiles(PATH)
    
    for i in range(len(file_list)):
        in_dir = file_list[i]
        command = './server_auto '+ "\"" + in_dir + "\""
        command_start_list.append(command)

    start_command = '&'.join(command_start_list)
    
    os.system(start_command)    

if  __name__ == '__main__':
   main()
