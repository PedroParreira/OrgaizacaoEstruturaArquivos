import struct
import time
# import sys

# if len(sys.argv) != 2:
#    print "USO %s [CEP]" % sys.argv[0]
#    quit()

cep = open("cep.dat", "rb")

inicio = time.time()

registroCEP = struct.Struct("72s72s72s72s2s8s2s")
cepColumn = 5
print ("Tamanho da Estrutura: %d" % registroCEP.size)
f = open("cep_ordenado.dat", "rb")
line = f.read(registroCEP.size)
quantAcesso = 0

esq = 0
f.seek(0,2)
dir = f.tell() / registroCEP.size

while True:
	linhaCep = cep.read(registroCEP.size)

	if linhaCep=="":
		break

	dados = registroCEP.unpack(linhaCep)

	while esq <= dir:
	    quantAcesso += 1
	    valorMeio = esq + ((dir - esq) / 2)
	    f.seek(valorMeio * registroCEP.size)
	    line = f.read(registroCEP.size)
	    record = registroCEP.unpack(line)
	#   if int(record[cepColumn]) == int(sys.argv[1]):
	    if int(record[cepColumn]) == dados[cepColumn]:
	        continue
	    elif int(record[cepColumn]) < dados[cepColumn]:
	        esq = valorMeio + 1
	    elif int(record[cepColumn]) > dados[cepColumn]:
	        dir = valorMeio - 1

print ("%d" % quantAcesso/699307) #209792100/300 (699307)

fim = time.time()

print ("\nTempo de execucao da Busca Binaria: ", fim-inicio, "segundos")
