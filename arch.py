#!/usr/bin/env python3.5

from zipfile import ZipFile
from os import mkdir

line = '------------------------------------'

def generator(string):
    for word in string:
        passwd = word.replace('\n', '')
        archive.setpassword(passwd.encode())
        try:
            archive.extractall(directory)
        except:
            yield "[False]: " + passwd
        else:
            yield line + "\n[True]: " + passwd

directory = "ExtractArchive"
try: mkdir(directory)
except FileExistsError: pass

print(line)
with open(input("Directory: "), error='ignore') as dictonary:
    with ZipFile(input("Archive: ")) as archive:
        print(line)
        for password in generator(directory):
            print(password)
print(line)