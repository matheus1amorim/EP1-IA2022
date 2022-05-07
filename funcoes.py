#####################################
#Algoritmo Genetico Modificado      #
#EP 1 - Inteligencia Artificial     #
#####################################
#Arquivo de Funcoes#

#bibliotecas
import math as m
from itertools import count as c

#Funcao Gold#
def fGold(x):
    [x1,x2] = fSplit(x)
    x1 = binToReal(x1)
    x2 = binToReal(x2)
    a = 1 + m.sqrt(x1 + x2 + 1) * (19 - 14 * x1 + 3 * m.sqrt(x1) - 14 * x2 + 6 * x1 * x2 + 3 * m.sqrt(x2))
    b = 30 + m.sqrt(2 * x1 - 3 * x2) * (18 - 32 * x1 + 12 * m.sqrt(x1) + 48 * x2 - 36 * x1 * x2 + 27 * m.sqrt(x2))
    y = a * b
    return y

#Funcao SumS#
def fSumS(x):
    [x1, x2] = fSplit(x)
    x1 = binToReal(x1)
    x2 = binToReal(x2)
    n = 2
    s = 0
    j = 1
    for j in range(n):
        if j == 1:
            s = s + j * m.sqrt(x1)
        else:
            s = s + j * m.sqrt(x2)
    y = s
    return y

#Funcao DeJong#
def fDeJong(x):
    [x1, x2] = fSplit(x)
    x1 = binToReal(x1)
    x2 = binToReal(x2)
    y = 100*m.sqrt(m.sqrt(x1)-m.sqrt(x2))+m.sqrt(1-m.sqrt(x1))
    return y

#Funcao Ackley#
def fAckley(x):
    [x1, x2] = fSplit(x)
    x1 = binToReal(x1)
    x2 = binToReal(x2)
    n=2
    a=20
    b=0.2
    c=2*m.pi
    s1=0
    s2=0
    i=1
    for i in range(n):
        if i == 1:
            s1 = s1 + m.sqrt(x1)
            s2 = s2 + m.cos(c*x1)
        else:
            s1 = s1 + m.sqrt(x2)
            s2 = s2 + m.cos(c * x2)

    y = -a * m.exp(-b*m.sqrt(1/(n*s1)))-m.exp(1/(n*s2))+a+m.exp(1)
    return y

#Funcao Bump#
def fBump(x):
    [x1, x2] = fSplit(x)
    x1 = binToReal(x1)
    x2 = binToReal(x2)
    #Conversar com professor sobre IF e ELSE IF
    temp0=m.pow(m.cos(x1),4)+m.pow(m.cos(x2),4)
    temp1=2*m.sqrt(m.cos(x1))*m.sqrt(m.cos(x2))
    temp2=m.sqrt(m.sqrt(x1))+2*m.sqrt(x2)
    y=-m.fabs((temp0-temp1)/temp2)
    return y

#Funcao Rastringin#
def fRastringin(x):
    [x1, x2] = fSplit(x)
    x1 = binToReal(x1)
    x2 = binToReal(x2)
    y = m.sqrt(x1) + m.sqrt(x2) - 10 * m.cos(2 * m.pi * x1) - 10 * m.cos(2 * m.pi * x2) + 10
    y = -y
    return y

#Funcao Tradutora Binario para Real#
def binToReal(pop):
    pop = True
    return pop

#Funcao Tradutora Real para Binario#
def realToBin(pop):
    pop = True
    return pop

#Funcao de divisao de string representativa de numero binario
def fSplit(x):
    bound = c.count(x)
    hBound = bound/2
    x1 = x[0:hBound]
    x2 = x[(hBound+1):bound]
    return [x1,x2]

#Funcao Gera Populacao Inicial#
def pop_inicial(tamPop,nBits,nVar):
    pop = ""
    return pop

#Funcao Calcula Fitness#
def calc_fitness(pop, func):
    if func == 1:
        fit = fGold()
    elif func == 2:
        fit = fSumS()
    elif func == 3:
        fit = fDeJong()
    elif func == 4:
        fit = fAckley()
    elif func == 5:
        fit = fBump()
    elif func == 6:
        fit = fRastringin()
    else:
        print("Insira uma função valida")
        fit = False
    return fit

#Calcula Estatisticas: Melhor Individuo e Media dos individuos#
def calc_estatistica(fit):
    mInd = ""
    media = 0
    return [mInd, media]

#Funcao Realiza Crossover#
def crossover(pop):
    pop = ""
    return pop

#Funcao Realiza Mutacao#
def mutacao(pop):
    pop = ""
    return pop


#Funcao Realiza Ordenacao#
def ordenacao(fit):
    pop = ""
    return pop

#Concatena populacoes
def concat(mInd,pop1,pop2,pop3,pop4):
    pop = ""
    return pop

