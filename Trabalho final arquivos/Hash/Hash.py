#coding: utf-8

import struct
import hashlib
import os

inicio = time.time()

hashSize = 700001
structCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
hashFormat = "8sLL"
hashStruct = struct.Struct(hashFormat)

f = open("cep.dat", "rb")
f2 = open("cep-hash.dat", "wb")

def hash(x):
    return int(hashlib.sha1(x).hexdigest(),16)%hashSize

emptyIndexRecord = hashStruct.pack("",0,0)

for i in range (0, hashSize):
	f2.write(emptyIndexRecord)
f2.close()

f2 = open("cep-hash.dat", "rb+")

f2.seek(0,2)
fileIndexSize = f2.tell()
print "IndexFileSize", fileIndexSize

recordNumber = 0

while True:
    line = f.read(structCEP.size)
    if line == "":
        break
    var = structCEP.unpack(line)
    i = hash(var[cepColumn])
    #print i, hashStruct.size
    f2.seek(i*hashStruct.size)
    k = hashStruct.unpack(f2.read(hashStruct.size))                
    if k[0][0] == "\0":
        f2.write(hashStruct.pack(var[cepColumn], recordNumber, 0))                
    else:
        nextPointer = k[2]
        f2.write(hashStruct.pack(k[0], k[1], fileIndexSize))
        f2.seek(0,2)
        f2.write(hashStruct.pack(var[cepColumn], recordNumber, nextPointer))
        recordNumber = recordNumber + 1

f.close()
f2.close()

fim = time.time()
print "\nTempo de execucao da indexação Hash: ", fim-inicio, "segundos"
