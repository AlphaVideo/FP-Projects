#Trabalho realizado por Tomas Pereira, numero 95682

#---------------Representacao do Labirinto e Unidades---------------

#Validade do labirinto apresentado
def eh_labirinto(tup):
    if not isinstance(tup,tuple):
        return False  
    comp = len(tup)
    
    #O tuplo nao pode conter listas
    for i in tup:
        if not isinstance(i,tuple):
            return False
    
    #Verif comp minimo de colunas e de linhas    
    if comp < 3:
        return False
    
    else:   
        if len(tup[0]) < 3:
            return False
            
    #Verif coerencia do tamanho das colunas    
    for i in range(comp-1):
        if len(tup[i]) != len(tup[i+1]):
            return False    
    
    #Verif das paredes essenciais        
    #Verif das extremidades de cima e de baixo    
    for i in (0,comp-1):
        for e in range(len(tup[i])):
            
            if tup[i][e] != 1:
                return False
    
    #Verif das extremidades laterais    
    for i in range(comp):
        for e in (0,len(tup[i])-1):
            
            if tup[i][e] != 1:
                return False
            
    #Verif da validade dos elementos do tuplo em geral
    for i in range(comp):
        for e in range(len(tup[i])):
            
            if not isinstance(tup[i][e],int):
                return False
            
            if not (tup[i][e] == 1 or tup[i][e] == 0):
                return False
        
    return True



#Validade de posicao apresentada
def eh_posicao(tup):
    if not isinstance(tup,tuple):
        return False  
    comp = len(tup)
    
    if comp != 2:
        return False
    
    elif not isinstance(tup[0],int):
        return False
    
    elif not isinstance(tup[1],int):
        return False
    
    elif tup[0] >= 0 and tup[1] >=0: #Nao existe posicoes com coordenadas negativas
        return True
    
    return False
 
        

#Validade de conjuntos de posicoes
def eh_conj_posicoes(tup):
    if not isinstance(tup,tuple):
        return False
    
    comp = len(tup)
      
    #Tem que ser posicoes validas
    for p in range(comp):
        if not eh_posicao(tup[p]):
            return False
    
    #Tem que ser posicoes unicas
    for i in range(comp):
            if tup[i] in tup[i+1:]:
                return False
    
    return True
    


#Tamanho do Labirinto
def tamanho_labirinto(tup):
    #Faz a validade dos parametros formais da funcao
    if not eh_labirinto(tup):
        raise ValueError('tamanho_labirinto: argumento invalido')
    
    tamanho = (len(tup),len(tup[0]))
    return tamanho
    


#Validade do mapa
def eh_mapa_valido(maze,posgroup):    
    if not eh_labirinto(maze):
        raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')
    elif not eh_conj_posicoes(posgroup):
        raise ValueError('eh_mapa_valido: algum dos argumentos e invalido')

    #Posicoes do conjunto nao podem ter indices maior que o mapa
    compconj = len(posgroup)
    dim = tamanho_labirinto(maze)
    
    for i in range(compconj):
        for e in range(2): #range(2) pois cada posicao tem duas coordenadas
            if posgroup[i][e] >= dim[e]:
                return False
            
    #Posicoes nao podem coincidir com paredes
    for i in range(compconj):
        if maze[posgroup[i][0]][posgroup[i][1]] == 1:
            return False
    
    return True



#Verif de posicao livre
def eh_posicao_livre(maze,unidades,pos):
    if not eh_labirinto(maze):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    elif not eh_conj_posicoes(unidades):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    elif not eh_mapa_valido(maze,unidades):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    elif not eh_posicao(pos):
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    
    #Posicao nao pode coincidir com uma unidade
    comp_unidades = len(unidades)
    for i in range(comp_unidades):
        if pos == unidades[i]:
            return False
    
    #Posicao encontra-se numa parede?
    if maze[pos[0]][pos[1]] == 1:
        return False

    return True



#Posicoes Adjacentes
def posicoes_adjacentes(pos):
    if not eh_posicao(pos):
        raise ValueError('posicoes_adjacentes: argumento invalido')
    
    adjacentes = ()
    
    #Esquerda, Cima, Baixo e Direita, por ordem:
    #E obrigatorio estarem nesta ordem.
    
    if pos[1]-1 >= 0:
        adjacentes += ((pos[0],pos[1]-1),)  
    if pos[0]-1 >= 0:
        adjacentes += ((pos[0]-1,pos[1]),)
    if pos[0]+1 >= 0:
        adjacentes += ((pos[0]+1,pos[1]),)
    if pos[1]+1 >= 0:
        adjacentes += ((pos[0],pos[1]+1),)
            
    return adjacentes



#Representacao 'grafica' do mapa
def mapa_str(maze,unidades):
    if not eh_labirinto(maze):
        raise ValueError('mapa_str: algum dos argumentos e invalido')
    elif not eh_conj_posicoes(unidades):
        raise ValueError('mapa_str: algum dos argumentos e invalido')
    elif not eh_mapa_valido(maze,unidades):
        raise ValueError('mapa_str: algum dos argumentos e invalido')
    
    dim = tamanho_labirinto(maze)
    mapa = ''
    
    for e in range(dim[1]): #Colunas
        for i in range(dim[0]): #Linhas
            
            if (i,e) in unidades:
                mapa = mapa + 'O' #Coloca unidades
            
            elif maze[i][e] == 0:
                mapa = mapa + '.' #Coloca espacos vazios
            
            else:
                mapa = mapa + '#' #Coloca paredes
                
        mapa = mapa + '\n'
    
    return mapa[:len(mapa)-1]



#---------------Funcoes de Movimento---------------

#Descobre Objetivos
def obter_objetivos(maze,unidades,selected):
    if not eh_labirinto(maze):
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    elif not eh_conj_posicoes(unidades):
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    elif not eh_mapa_valido(maze,unidades):
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    elif not eh_posicao(selected):
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    elif selected not in unidades:
        raise ValueError('obter_objetivos: algum dos argumentos e invalido')
    
    objetivos = ()
    adjacentes = ()
    
    for i in unidades:
        #Nao se retorna as posicoes adjacentes iguais a unidade selecionada
        if i != selected:
            adjacentes += posicoes_adjacentes(i)
            
            for i in adjacentes:
                #Evita adjacentes dentro de paredes, repeticoes e adjacentes iguais ao selecionado
                if maze[i[0]][i[1]] != 1 and i not in objetivos and i != selected and i not in unidades: 
                    objetivos += ((i),)
    
    return objetivos



#Obter Caminho
#Funcao que utiliza o Algoritmo de Lee
def obter_caminho(maze,unidades,start):
    if not eh_labirinto(maze):
        raise ValueError('obter_caminho: algum dos argumentos e invalido')
    elif not eh_conj_posicoes(unidades):
        raise ValueError('obter_caminho: algum dos argumentos e invalido')
    elif not eh_mapa_valido(maze,unidades):
        raise ValueError('obter_caminho: algum dos argumentos e invalido')
    elif not eh_posicao(start):
        raise ValueError('obter_caminho: algum dos argumentos e invalido')
    elif start not in unidades:
        raise ValueError('obter_caminho: algum dos argumentos e invalido') 
    
    #Variaveis uteis no algoritmo
    obj_possiveis = obter_objetivos(maze,unidades,start)
    lista_exploracao = [(start, ()),]
    visited = ()
    caminho_final = ()
    caminho_atual = (start,)
    
    while lista_exploracao != []:
        #A lista de exploracao e uma lista first in, first out
        #Em cada ciclo "utiliza-se" o primeiro elemento da lista, que depois e apagado e nao volta a ser adicionado gracas ao tuplo visited
        
        pos_atual = (lista_exploracao[0][0])
        caminho_atual = (lista_exploracao[0][1])
        del(lista_exploracao[0]) #Retira o primeiro elemento da lista de exploracao
        
        if pos_atual not in visited:
            visited += (pos_atual,) #Coloca a posicao atual em posicoes visitadas
            caminho_atual += (pos_atual,) #Coloca a posicao atual no caminho atual
            
            
            if pos_atual in obj_possiveis:   #Atingiu-se um dos objetivos
                caminho_final = caminho_atual
                break
            
            else:
                for p in posicoes_adjacentes(pos_atual):
                    if eh_posicao_livre(maze,unidades,p):
                        
                        #Adiciona-se um conjunto de (pos_atual, (tuplo de caminho),) a lista de exploracao
                        lista_exploracao += (p, (caminho_atual)),
                        
    return caminho_final  
        

        
#Funcao que move a unidade ate ao objetivo
def mover_unidade(maze,unidades,unidade):
    if not eh_labirinto(maze):
        raise ValueError('mover_unidade: algum dos argumentos e invalido')
    elif not eh_conj_posicoes(unidades):
        raise ValueError('mover_unidade: algum dos argumentos e invalido')
    elif not eh_mapa_valido(maze,unidades):
        raise ValueError('mover_unidade: algum dos argumentos e invalido')
    elif not eh_posicao(unidade):
        raise ValueError('mover_unidade: algum dos argumentos e invalido')
    elif unidade not in unidades:
        raise ValueError('mover_unidade: algum dos argumentos e invalido')
    
    caminho = obter_caminho(maze,unidades,unidade)
    qnt_unidades = len(unidades)
    unid_novas = ()
    p = 0
    
    #Descobre a posicao da unidade movida
    for e in range(qnt_unidades):
        
        if unidades[e] != unidade:
            p +=1
        else:
            break
        
    unid_esq = unidades[:p]
    unid_dir = unidades[p+1:]
    
    #Se a unidade ja se encontrar num dos objetivos possiveis, nao move
    for e in unidades:
        if unidade in posicoes_adjacentes(e):
            return unidades
        
    #Tambem, se nao existir um caminho possivel, nao move    
    if caminho == ():
        return unidades
    
    else:
        unid_novas += unid_esq + (caminho[1],) + unid_dir
        return unid_novas
    
    
    
    