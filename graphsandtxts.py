#####################################
#Algoritmo Genetico Modificado      #
#EP 1 - Inteligencia Artificial     #
#####################################
#Arquivo de geracao de graficos e estatisticas#
#link funcoes python para manipulacao de txt: http://devfuria.com.br/python/receitas-para-manipular-arquivos-de-texto/

#imports e arquivos relevantes

#Cria um arquivo txt
def createTxt(nomeArquivo):
    arquivo = open(nomeArquivo +'.txt', 'w')
    arquivo.close()
    return arquivo

#Escreve (ou sobrescrever) em arquivo txt com populacao
def writeTxtPop(pop,upPop):
    createTxt(pop)
    arquivo = open(pop + '.txt', 'w')
    arquivo.write(upPop)
    arquivo.close
    return

#Adicionar texto em arquivo já preenchido
def writeExistTxt(pop,newEntry):
    arquivo = open(pop +'.txt', 'r')  # Abra o arquivo (leitura)
    conteudo = arquivo.readlines()
    conteudo.append(newEntry)  # insira seu conteúdo

    arquivo = open(pop +'.txt', 'w')  # Abre novamente o arquivo (escrita)
    arquivo.writelines(conteudo)  # escreva o conteúdo criado anteriormente nele.

    arquivo.close()
    return

#Le de arquivo txt com populacao
def readTxtPop(pop):
    arquivo = open(pop +'.txt', 'r')
    lista = arquivo.readline()
    return lista

#Gerador de graficos
def graphs(pop):
    return
