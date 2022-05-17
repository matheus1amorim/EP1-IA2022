#####################################
#Algoritmo Genetico Modificado      #
#EP 1 - Inteligencia Artificial     #
#Matheus Amorim                     #
#Vinícius Brito nUSP10783198        #
#####################################

#importe de bibliotecas e arquivos relevantes
import funcoes as f
import graphsandtxts as gt

#Definicao de parametros
tamPop = 500 #tamanho da populacao
pc = 0.8 #probabilidade de crossover
pm = 0.2 #probabilidade de mutacao
nGera = 2000 #numero de geracoes
nBits = 64 #numero de bits para cada variavel
nVar = 2 #numero de variaveis
gera = 0 #contador de geracoes
func = 1 #determina a funcao
mInd = "" #melhor individuo
media = 0 #media
xmin = 0 #x minimo
xmax = 0 #x maximo

#Gera a Populacao Inicial
pop = f.pop_inicial(tamPop,nBits,nVar)

#Calcula o Fitness
fit = f.calc_fitness(pop,func)
if not fit:
    exit()

#Calcula Estatisticas: Melhor Individuo e Media dos individuos
[mInd, media] = f.calc_estatisticas(fit)

#Execução do AGM#

#while gera=<Ngera
#gera=gera+1
#pop1 = f.rossover(pop)
#pop1 = f.mutacao(pop1)
#pop2 = f.crossover(pop)
#pop3 = f.mutacao(pop)
#pop4 = f.aleatoria(chama mesma função da pop inicial)
#pop_aux = f.concat(mInd,pop1,pop2,pop3,pop4)
#fit = f.calc_fitness()
#fit = f.ordena(fit)

#[fmelhor,fmed]= f.calc_estatisticas(fit)

#Gerar Saidas TXT E Graficos#
#status = gt.txtPop(pop)
#status = gt.graphs(pop)

###<<<Fim do Documento>>>###