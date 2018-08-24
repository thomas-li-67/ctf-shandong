#coding=utf8

from __future__ import  print_function, unicode_literals
import zipfile
import binascii
import string



fn = 'qgwj.zip'

def getZipfile(file):
   zfile = zipfile.ZipFile(file,'r')
   for i in zfile.infolist():
       print(i.file_size,i.name)
   #print(file.getinfo())

getZipfile(fn)   