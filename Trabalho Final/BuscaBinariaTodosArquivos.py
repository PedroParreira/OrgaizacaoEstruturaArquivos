#coding: utf-8

import struct
import time

inicio = time.time()

fileName = "BolsaFamilia.dat"
indexName = "BolsaFamilia_ordenado.dat"
dataFormat = "2s30s14s50s6s2s"
indexColumn = 2
quantAcesso = 0
registroArquivo = struct.Struct(dataFormat)
arquivo = open(fileName, "rb")

print "\nTamanho da Estrutura: %d" % registroArquivo.size

f = open(indexName, "rb")
line = f.read(registroArquivo.size)

while True:
        
        esq = 0
        f.seek(0, 2)
        dir = f.tell() / registroArquivo.size
        
        linhaArquivo = arquivo.read(registroArquivo.size)
        
        if linhaArquivo == b'':
                break
        
        dados = registroArquivo.unpack(linhaArquivo)

        while esq <= dir:
                quantAcesso += 1
                valorMeio = int(esq + (dir - esq) / 2)
                f.seek(valorMeio * registroArquivo.size)
                line = f.read(registroArquivo.size)
                if line == b'':
                        break
                record = registroArquivo.unpack(line)
                if int(record[indexColumn]) == int(dados[indexColumn]):
                        break
                elif int(record[indexColumn]) < int(dados[indexColumn]):
                        esq = valorMeio + 1
                elif int(record[indexColumn]) > int(dados[indexColumn]):
                        dir = valorMeio - 1
                        
print "\nQuantidade de acessos: ", quantAcesso/2000000

fim = time.time()

print "\nTempo de execucao da Busca Binaria: ", fim-inicio, "segundos"
