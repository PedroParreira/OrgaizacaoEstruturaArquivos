import csv
import struct

primeiraLinha = True

estrutura = 'i2s30s3s70s'

s = struct.Struct(estrutura)

#Ler o arquivo csv
f = open('2015_Funcoes.csv', encoding = 'cp1252')

#Criar o arquivo dat
x = open('escritaArquivoNovo.dat', 'wb+')
r = csv.reader(f)

#Iniciar a variavel para o id
id = 1

for linha in r:
    if primeiraLinha:
        primeiraLinha = False
        continue

    info = linha[0].split('\t')

    x.write(s.pack(id,
    bytearray(info[0], encoding = 'cp1252'),
    bytearray(info[1], encoding = 'cp1252'),
    bytearray(info[2], encoding = 'cp1252'),
    bytearray(info[3], encoding = 'cp1252'),
    bytearray('\n', encoding = 'cp1252')))

    #Incrementar +1 a variavel do id
    id = id + 1

t.close()
