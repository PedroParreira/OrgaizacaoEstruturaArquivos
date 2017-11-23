import struct
import time
# import sys

# if len(sys.argv) != 2:
#    print "USO %s [CEP]" % sys.argv[0]
#    quit()

cep = input("Digite o cep a ser buscado\n\n")

inicio = time.time()

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print "Tamanho da Estrutura: %d" % registroCEP.size
f = open("cep_ordenado.dat", "r")
line = f.read(registroCEP.size)

esq = 0
f.seek(0,2)
dir = f.tell() / registroCEP.size

while esq <= dir:
    valorMeio = esq + ((dir - esq) / 2)
    f.seek(valorMeio * registroCEP.size)
    line = f.read(registroCEP.size)
    record = registroCEP.unpack(line)
#   if int(record[cepColumn]) == int(sys.argv[1]):
    if int(record[cepColumn]) == int(cep):
        for i in range(0, len(record) - 1):
            print record[i]  # .decode('latin1')
        break
    elif int(record[cepColumn]) < int(cep):
        esq = valorMeio + 1
    elif int(record[cepColumn]) > int(cep):
        dir = valorMeio - 1

if esq > dir:
    print "Cep nao encontrado"

fim = time.time()

print "\nTempo de execucao da Busca Binaria: ", fim-inicio, "segundos"