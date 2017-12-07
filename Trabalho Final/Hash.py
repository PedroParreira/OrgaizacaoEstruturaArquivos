#coding: utf-8

import struct
import hashlib
import os
import time

inicio = time.time()

fileName = "BolsaFamilia.dat"
indexName = "BolsaFamilia-hash.dat"
dataFormat = "2s30s14s50s6s2s"
hashFormat = "14sLL"
hashSize = 2000003
indexColumn = 2
totalAcessos = 0

fileStruct = struct.Struct(dataFormat)
hashStruct = struct.Struct(hashFormat)

f = open(fileName, "rb")
f2 = open(indexName, "wb")

def hash(x):
    return int(hashlib.sha1(x).hexdigest(), 16) % hashSize

emptyIndexRecord = hashStruct.pack("", 0, 0)

for i in range(0, hashSize):
    f2.write(emptyIndexRecord)
f2.close()

f2 = open(indexName, "rb+")

f2.seek(0, 2)
fileIndexSize = f2.tell()
print "\nIndexFileSize", fileIndexSize

recordNumber = 0

while True:
    line = f.read(fileStruct.size)
    if line == "":
        break
    var = fileStruct.unpack(line)
    i = hash(var[indexColumn])
    f2.seek(i * hashStruct.size)
    k = hashStruct.unpack(f2.read(hashStruct.size))
    if k[0][0] == "\0":
        f2.seek(0, 2)
        f2.write(hashStruct.pack(var[indexColumn], recordNumber, 0))
    else:
        nextPointer = k[2]
        f2.write(hashStruct.pack(k[0], k[1], fileIndexSize))
        f2.seek(0, 2)
        f2.write(hashStruct.pack(var[indexColumn], recordNumber, nextPointer))
    recordNumber = recordNumber + 1

f.close()
f2.close()

fim = time.time()
print "\nTempo de execucao da indexação Hash: ", fim - inicio, "segundos"

inicio = time.time()

f = open(fileName, "rb")
fi = open(indexName, "rb")

while True:
    line = f.read(fileStruct.size)

    if line == "":
        break

    data = fileStruct.unpack(line)
    p = hash(data[indexColumn])
    offset = p * hashStruct.size
    while True:
        totalAcessos += 1
        fi.seek(offset, os.SEEK_SET)
        indexRecord = hashStruct.unpack(fi.read(hashStruct.size))
        if indexRecord[0] == data[indexColumn]:
            break
        else:
            offset = indexRecord[2]
            if offset == 0:
                break
    line = f.read(fileStruct.size)

f.close()
fi.close()

print "\nMedia de acessos: ", totalAcessos / float(422498)
fim = time.time()
print "\nTempo de execucao da busca Hash: ", fim - inicio, "segundos"
