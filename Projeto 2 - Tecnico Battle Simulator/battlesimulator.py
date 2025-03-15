#Projeto realizado por Tomas Pereira n95682

# ============= TAD da Posicao ============= 
#Posicoes neste projeto sao tuplos de 2 elementos

#Construtores

def cria_posicao(x,y): #N^2 -> posicao (Recebe dois naturais e devolve uma posicao)
    
    """Funcao construtora que permite a criacao de um TAD posicao a partir
    de dois numeros naturais. Uma posicao e um tuplo de dois inteiros maiores
    ou iguais a zero."""
    
    if not (isinstance(x, int) and  isinstance(y, int) and  x >= 0 and  y >= 0):        
        raise ValueError('cria_posicao: argumentos invalidos')
    
    else:
        return (x,y)
        
        
def cria_copia_posicao(p): #posicao -> posicao (Recebe uma posicao e devolve um posicao)
    
    """Funcao construtora que devolve uma copia da posicao dada."""
    
    return cria_posicao(p[0],p[1])
    

#Seletores

def obter_pos_x(p): #posicao -> N (Recebe uma posicao e devolve um inteiro natural)
    
    """Funcao seletora que devolve a coordenada x da posicao dada."""
    
    return p[0]


def obter_pos_y(p): #posicao -> N (Recebe uma posicao e devolve um inteiro natural)
    
    """Funcao seletora que devolve a coordenada y da posicao dada."""
    
    return p[1]
    

#Reconhecedores

def eh_posicao(arg): #universal -> booleano (Recebe um argumento qualquer e devolve um valor booleano)
    
    """Funcao reconhecedora que avalia a validade do argumento dado,
    verificando se este e um TAD posicao ou nao."""
    
    if not (isinstance(arg, tuple) and len(arg) == 2 and isinstance(obter_pos_x(arg), int) \
            and isinstance(obter_pos_y(arg), int) and obter_pos_x(arg) >= 0 and obter_pos_y(arg) >= 0):
        
        return False
    
    else:
        return True
  
    
#Testes

def posicoes_iguais(p1,p2): #posicao x posicao -> booleano (Recebe duas posicoes e devolve um valor booleano)
    
    """Funcao que compara duas posicoes e avalia se estas sao iguais ou nao."""
    
    if eh_posicao(p1) and eh_posicao(p2):
        return (obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2))
    else:
        return False
    

#Transformadores

def posicao_para_str(p): #posicao -> string (Recebe uma posicao e devolve uma string)
    
    """Funcao transformadora que converte a posicao dada numa cadeia de caracteres."""
    
    return str(p)
    

#Funcoes de alto nivel

def obter_posicoes_adjacentes(p): #posicao -> tuplo de posicoes (Recebe uma posicao e devolve um tuplo de posicoes)
    
    """Esta funcao devolve todas as posicoes adjacentes e validas
    a posicao dada como argumento de entrada."""
    
    adjacentes = ()
    if eh_posicao(p):
        #O tuplo de adjacentes tem que ter a ordem de leitura correta:
        if eh_posicao((obter_pos_x(p), obter_pos_y(p) - 1)):
            #Cima 
            adjacentes += (obter_pos_x(p), obter_pos_y(p) - 1),
        
        if eh_posicao((obter_pos_x(p) - 1, obter_pos_y(p))):
            #Esquerda
            adjacentes += (obter_pos_x(p) - 1, obter_pos_y(p)),
            
        if eh_posicao((obter_pos_x(p) + 1, obter_pos_y(p))):
            #Direita
            adjacentes += (obter_pos_x(p) + 1, obter_pos_y(p)),
            
        if eh_posicao((obter_pos_x(p),  obter_pos_y(p) + 1)):
            #Baixo
            adjacentes += (obter_pos_x(p),  obter_pos_y(p) + 1),
                
    return adjacentes
            
        

# ============= TAD da Unidade ============= 
#Unidades neste projeto sao listas de 4 elementos

#Construtores

def cria_unidade(p,v,f,str): #posicao x N x N x string -> unidade (Recebe uma posicao, dois naturais e uma string e devolve uma unidade)
    
    """Funcao construtora que cria um TAD unidade, representada por uma lista,
    a partir de uma posicao, de dois inteiros que representam a vida e a forca 
    da unidade respetivamente, e de uma string com o nome da equipa."""
    
    if not (eh_posicao(p) and isinstance(v, int) and v > 0 and isinstance(f, int) \
            and f > 0 and type(str) == type('a') and str != ''):
        
        raise ValueError('cria_unidade: argumentos invalidos')
    
    else:
        return [p,v,f,str]
    

def cria_copia_unidade(u): #unidade -> unidade (Recebe uma unidade e devolve uma unidade)
    
    """Funcao construtora que cria uma copia da unidade dada."""
    
    return cria_unidade(u[0],u[1],u[2],u[3])
    


#Seletores

def obter_posicao(u): #unidade -> posicao (Recebe uma unidade e devolve uma posicao)
    
    """Funcao seletora que devolve a posicao da unidade dada."""
    
    return u[0]
    
    
def obter_exercito(u): #unidade -> string (Recebe uma unidade e devolve uma string)
    
    """Funcao seletora que devolve o exercito da unidade dada."""
    
    return u[3]


def obter_forca(u): #unidade -> natural (Recebe uma unidade e devolve um inteiro positivo)
    
    """Funcao seletora que devolve o valor da forca da unidade dada."""
    
    return u[2]


def obter_vida(u): #unidade -> natural (Recebe uma unidade e devolve um inteiro positivo)
    
    """Funcao seletora que devolve o valor da vida da unidade dada."""
    
    return u[1]


#Modificadores

def muda_posicao(u,p): #unidade x posicao -> unidade (Recebe uma unidade e uma posicao e devolve uma unidade)
    
    """Funcao modificadora que altera a posicao da unidade dada 
    pela posicao dada."""
    
    u[0] = p
    return u
    
    
def remove_vida(u,v): #unidade x natural -> unidade (Recebe uma unidade e um natural e devolve uma unidade)
    
    """Funcao modificadora que subtrai a unidade dada o valor do 
    segundo parametro dado a funcao."""
    
    u[1] = obter_vida(u) - v
    return u


#Reconhecedor

def eh_unidade(arg): #unidade -> booleano (Recebe uma unidade e devolve um valor booleano)
    
    """Funcao reconhecedora que avalia o argumento dado, verificando se este
    e um TAD unidade ou nao."""
    
    if not (isinstance(arg,list) and len(arg) == 4 and eh_posicao(obter_posicao(arg)) \
            and isinstance(obter_vida(arg),int) and isinstance(obter_forca(arg), int) \
            and obter_vida(arg) > 0 and obter_forca(arg) > 0 and isinstance(obter_exercito(arg), str) \
            and obter_exercito(arg) != ''):
        
        return False
    else:
        return True
    

#Testes

def unidades_iguais(u1,u2): #unidade x unidade -> booleano (Recebe duas unidades e devolve um valor booleano)
    
    """Funcao que compara as duas unidades dados, devolvendo True 
    se ambas forem iguais e falso caso contrario"""
    
    if eh_unidade(u1) and eh_unidade(u2):
        return (obter_posicao(u1) == obter_posicao(u2) and obter_vida(u1) == obter_vida(u2) \
                and obter_forca(u1) == obter_forca(u2) and obter_exercito(u1) == obter_exercito(u2))
    else:
        return False
    
    
#Transformadores

def unidade_para_char(u): #unidade -> string (Recebe uma unidade e devolve uma string)
    
    """Funcao transformadora que devolve o primeiro caracter do exercito 
    como uma string de uma letra maiuscula."""
    
    return obter_exercito(u)[0].upper()


def unidade_para_str(u): #unidade -> string (Recebe uma unidade e devolve uma string)
    
    """Funcao transformadora que devolve a unidade dada como uma 
    cadeia de caracteres no formato 'Exercito[vida,forca]@posicao'."""
        
    unistr = unidade_para_char(u) + str( [obter_vida(u), obter_forca(u)]) \
        + '@' + posicao_para_str(obter_posicao(u))
    
    return unistr


#Funcoes de alto nivel

def unidade_ataca(u1,u2): #unidade x unidade -> booleano (Recebe duas unidades e devolve um valor booleano)
    
    """Esta funcao retira da vida da segunda unidade o valor da forca da 
    primeira unidade, devolvendo o valor booleano True se esta unidade 
    "morrer", isto e, se o valor da vida da segunda unidade apos a funcao 
    for <= 0, e False caso contrario"""
    
    u2 = remove_vida(u2, obter_forca(u1))
    
    #Se a unidade "morrer", esta ja nao e considerada uma unidade pois vida <= 0
    return not eh_unidade(u2)
    
    
def ordenar_unidades(t): #tuplo unidades -> tuplo unidades (Recebe um tuplo de unidades e devolve um tuplo de unidades)
    
    """Esta funcao ordena o tuplo de unidades dado de acordo com a ordem de
    leitura de labirinto: da esquerda para a direita e de cima para baixo."""
    
    lista_pos = []
    t_ordenado = ()
    
    for uni in t:
        #Coloca todas as posicoes numa lista
        lista_pos += (obter_posicao(uni)),

    def key_y(item):
        return item[1] 
    
    #list_pos e uma lista diferente de lst_pos_x 
    #Ordena a lista de posicoes baseado no x
    lst_pos_x = sorted(list(lista_pos))
    
    #lst_pos_x e uma lista diferente de lst_pos_ord
    #Ordena a lista de posicoes (ordenada a x) agora a y
    lst_pos_ord = sorted(list(lst_pos_x), key = key_y)
    
    for pos in lst_pos_ord:
        for uni in t:
            #Faz a relacao entre as posicoes ordenadas com as respetivas unidades
            if pos == obter_posicao(uni):            
                t_ordenado += (uni),
       
    return t_ordenado
    
    
# ============= TAD do Mapa =============
#Mapas neste projeto sao listas de listas
    
#Construtores

def cria_mapa(d,w,e1,e2): # tuplo x tuplo x tuplo x tuplo -> mapa (Recebe quatro tuplos e devolve um mapa)
    
    """Funcao construtora que cria um TAD mapa a partir de um tuplo de dimensoes
    Nx por Ny, um tuplo contendo as posicoes das paredes nao exteriores e dois
    tuplos contendo unidades de um exercito, sendo estes tuplos exercitos distintos.
    
    Um mapa acaba por ser uma lista de listas, sendo 0 uma posicao livre, 1 uma
    posicao ocupada e unidades representadas diretamente dentro da lista."""
    
    #Verif geral
    if not (isinstance(d,tuple) and isinstance(w, tuple) and isinstance(e1,tuple) \
            and isinstance(e2, tuple)):
        
        raise ValueError('cria_mapa: argumentos invalidos')
    
    #Dimensao minima do labirinto e 3x3 
    if not (len(d) == 2 and isinstance(d[0], int) and isinstance(d[1],int) and \
            d[0] >= 3 and d[1] >= 3):
        
        raise ValueError('cria_mapa: argumentos invalidos')
    
    #Paredes extra
    if len(w) > 0:
        #Se existerem paredes:
        for par in w:
            #e um tuplo de posicoes
            if not eh_posicao(par):
                raise ValueError('cria_mapa: argumentos invalidos')
        
            #nao podem coincidir com as extremidades do mapa nem estar fora do mapa
            elif (obter_pos_x(par) == 0 or obter_pos_y(par) == 0 \
                  or obter_pos_x(par) >= d[0] - 1 or obter_pos_y(par) >= d[1] - 1):
                
                raise ValueError('cria_mapa: argumentos invalidos')
            
    
    #Exercitos
    #Pode-se assumir que todas as unidades se encontram dentro do mapa, numa
    #posicao livre e distinta e que e1 e e2 representam exercitos diferentes
    
    if len(e1) == 0 or len(e2) == 0:
        #Tem que ter pelo menos uma unidade cada
        raise ValueError('cria_mapa: argumentos invalidos')
    
    for uni1 in e1:

        #Tem que conter unidades validas
        if not eh_unidade(uni1):
            raise ValueError('cria_mapa: argumentos invalidos')
        
        for uni2 in e1:
            #Segunda unidade tem que ser valida
            if not eh_unidade(uni2):
                raise ValueError('cria_mapa: argumentos invalidos')            
            #Tem que ser unidades do mesmo exercito
            if obter_exercito(uni1) != obter_exercito(uni2):
                raise ValueError('cria_mapa: argumentos invalidos')
    
    
    for uni1 in e2:
        
        #Tem que conter unidades validas
        if not eh_unidade(uni1):
            raise ValueError('cria_mapa: argumentos invalidos')
        
        for uni2 in e2:
            #Segunda unidade tem que ser valida
            if not eh_unidade(uni2):
                raise ValueError('cria_mapa: argumentos invalidos')
            #Tem que ser unidades do mesmo exercito
            if obter_exercito(uni1) != obter_exercito(uni2):
                raise ValueError('cria_mapa: argumentos invalidos')
            
            
    #Representacao interna
    mapa = []
    col_mapa = []
    nx = d[0]
    ny = d[1]
    
    #Adiciona tamanho as colunas
    while ny != 0:
        col_mapa += [0]
        ny -= 1
        
    #Extremidades verticais sao iguais a 1
    col_mapa[0], col_mapa[len(col_mapa)-1] = 1, 1 
    
    #Adiciona tamanho as linhas
    while nx != 0:
        #Cada coluna e uma lista nova
        mapa.append(list(col_mapa))
        nx -= 1
        
    for e in range(d[1]-1):
        #Extremidades laterais sao iguais a 1
        mapa[0][e], mapa[d[0]-1][e] = 1, 1
    
    
    if len(w) > 0:
        #Se existerem paredes:    
        for parede in w:
            #Adiciona as paredes extra
            mapa[parede[0]][parede[1]] = 1
        
    for uni in e1:
        #Adiciona as unidades do primeiro exercito
        p = obter_posicao(uni)
        mapa[p[0]][p[1]] = uni
        
    for uni in e2:
        #Adiciona as unidades do segundo exercito
        p = obter_posicao(uni)
        mapa[p[0]][p[1]] = uni    
        
    return mapa

    
def cria_copia_mapa(m): #mapa -> mapa (Recebe um mapa e devolve um mapa)
    
    """Funcao construtora que cria uma copia do mapa dado."""
    
    mapa_novo = []
    
    for i in m:
        #Cada coluna do mapa novo e uma lista diferente do mapa orig
        mapa_novo.append(list(i))
        
    nx = len(m)
    ny = len(m[0])
        
    #Unidades tem que ser independentes das originais    
    for c in range(nx):
        for e in range(ny):
            
            if eh_unidade(m[c][e]):
                
                mapa_novo[c][e] = cria_copia_unidade(m[c][e])
        
    return mapa_novo


#Seletores

def obter_tamanho(m): #mapa -> tuplo (Recebe um mapa e devolve um tuplo)
    
    """Funcao seletora que devolve um tuplo com as dimensoes Nx por Ny do
    mapa dado."""
    
    return (len(m), len(m[0]))


def obter_nome_exercitos(m): #mapa -> tuplo (Recebe um mapa e devolve um tuplo)
    
    """Funcao seletora que devolve um tuplo contendo os nomes dos exercitos do
    mapa, por ordem alfabetica (ordenado)."""
    
    armies = ()
    comp = len(m)
    
    for c in range(comp):
        
        for elem in m[c]:
            #Segunda cond evita repeticoes do mesmo exercito
            if eh_unidade(elem) and (obter_exercito(elem) not in armies):
                
                armies += (obter_exercito(elem)),
                
    #Sorted devolve uma lista, tem que ser tuplo
    return tuple(sorted(armies))


def obter_unidades_exercito(m,e): #mapa x string -> tuplo unidades (Recebe um mapa e uma string e devolve um tuplo)
    
    """Funcao seletora que devolve um tuplo contendo todas as unidades do
    exercito dado pertencentes ao mapa dado, de acordo com a ordem de leitura
    do mapa."""
    
    comp = len(m)
    unidades = ()
    
    for c in range(comp):
        
        for elem in m[c]:
            #So sao adicionadas as unidades do exercito e
            if eh_unidade(elem) and obter_exercito(elem) == e:
                
                unidades += (elem),
    
    return ordenar_unidades(unidades)
    
    
def obter_todas_unidades(m): #mapa -> tuplo (Recebe um mapa e devolve um tuplo)
    
    """Funcao seletora que devolve um tuplo contendo todas as unidades presentes
    no mapa dado, de acordo com a ordem de leitura do mapa."""
    
    dim = obter_tamanho(m)
    unidades = ()
    
    #Tem-se que verif o primeiro elemento de cada col, depois o segundo, etc
    #Para ser coerente com a ordem de leitura    
    
    for e in range(dim[1]): #Elemento
        
        for c in range(dim[0]): #Coluna
            
            if eh_unidade(m[c][e]):
                
                unidades += (m[c][e]),
    
    return unidades


def obter_unidade(m,p): #mapa x posicao -> unidade (Recebe um mapa e uma posicao e devolve uma unidade)
    
    """Funcao seletora que devolve a unidade presente na posicao dada do 
    mapa dado."""
        
    return m[obter_pos_x(p)][obter_pos_y(p)]
    

#Modificadores

def eliminar_unidade(m,u): #mapa x unidade -> mapa (Recebe um mapa e uma unidade e devolve um mapa)
    
    """Funcao que modifica o mapa dado, eliminando a unidade u no mapa e
    substituindo esta por uma posicao livre."""
    
    p = obter_posicao(u)
    
    m[obter_pos_x(p)][obter_pos_y(p)] = 0
    
    return m


def mover_unidade(m,u,p): #mapa x unidade x posicao -> mapa (Recebe um mapa, uma unidade e uma posicao e devolve um mapa)
    
    """Funcao que altera a posicao da unidade dada do mapa dado para a nova
    posicao dada, deixando a sua posicao antiga como uma posicao livre."""
    
    uni_old = list(u) #Unidade antiga tem que ser uma lista diferente que u
    
    #Unidade nova tem que ter a sua posicao atualizada
    m[obter_pos_x(p)][obter_pos_y(p)] = muda_posicao(u,p) 
    
    eliminar_unidade(m,uni_old)
    
    return m


#Reconhecedores

def eh_posicao_unidade(m,p): #mapa x posicao -> booleano (Recebe um mapa e uma posicao e devolve um valor booleano)
    
    """Funcao reconhecedora que avalia se a posicao dada corresponde a uma
    posicao de uma unidade no mapa dado, retornando um valor booleano."""
    
    return eh_unidade(m[obter_pos_x(p)][obter_pos_y(p)]) 


def eh_posicao_corredor(m,p): #mapa x posicao -> booleano (Recebe um mapa e uma posicao e devolve um valor booleano)
    
    """Funcao reconhecedora que avalia se a posicao dada corresponde a um
    corredor, ou seja, posicao livre no mapa dado. Retorna um valor booleano,
    considerando um corredor ocupado com um unidade como True tambem."""
    
    return m[obter_pos_x(p)][obter_pos_y(p)] == 0 or eh_posicao_unidade(m,p)


def eh_posicao_parede(m,p): #mapa x posicao -> booleano (Recebe um mapa e uma posicao e devolve um valor booleano)
    
    """Funcao reconhecedora que avalia se a posicao dada corresponde a uma
    parede no labirinto dado, retornando um valor booleano."""
    
    return m[obter_pos_x(p)][obter_pos_y(p)] == 1


#Testes

def mapas_iguais(m1,m2): #mapa x mapa -> booleano (Recebe dois mapas e devolve um valor booleano)
    
    """Funcao que compara dois mapas dados, retornando True caso estes sejam
    iguais."""
    
    if obter_tamanho(m1) != obter_tamanho(m2):
        
        return False
    
    dim = obter_tamanho(m1)
    
    for c in range(dim[0]):
        for e in range(dim[1]):
            
            if m1[c][e] != m2[c][e]:
                
                return False
    
    return True


#Transformador

def mapa_para_str(m): #mapa -> string (Recebe um mapa e devolve uma string)
    
    """Funcao transformadora que converte o mapa dado numa string, seguindo 
    as convencoes de representacao: paredes sao #, espacos livres sao . e
    unidades sao representadas pela sua representacao externa."""
    
    dim = obter_tamanho(m)
    mapa = ''
    
    for e in range(dim[1]): #Elementos
        for c in range(dim[0]): #Colunas
            
            if eh_unidade(m[c][e]):
                mapa = mapa + unidade_para_char(m[c][e]) #Coloca unidades
            
            elif m[c][e] == 1:
                mapa = mapa + '#' #Coloca paredes            
            
            else:
                mapa = mapa + '.' #Coloca espacos vazios
                
        mapa = mapa + '\n'
    
    return mapa[:len(mapa)-1]
    

#Funcoes de alto nivel

def obter_inimigos_adjacentes(m,u): #mapa x unidade -> tuplo de unidades (Recebe um mapa e uma unidade e devolve um tuplo de undiades)
    
    """Esta funcao devolve um tuplo contendo todas as unidades inimigas da
    unidade u dada, pertencente ao mapa m, que se encontram adjacentes 
    a esta mesma."""
    
    army = obter_exercito(u)
    p = obter_posicao(u)
    adjacentes = obter_posicoes_adjacentes(p)
    inimigos = ()
    #Tuplo com todas as unidades do mapa ordenadas
    unidades = ordenar_unidades(obter_todas_unidades(m))
    
    
    for uni in unidades:
        
        if obter_posicao(uni) in adjacentes and obter_exercito(uni) != army:
            #Ja sao adicionadas pela ordem de leitura do mapa
            inimigos += (uni),
    
    return inimigos


#Funcao dada pelo enunciado
def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)
            
            
#Funcoes Adicionais

def calcula_pontos(m,s): #mapa x str -> int (Recebe um mapa e uma string e devolve um inteiro)
    
    """Funcao que calcula a pontuacao do exercito dado pertencente ao mapa dado.
    A pontuacao e igual a soma da vida de todas as unidades do exercito atual."""
        
    unidades = obter_todas_unidades(m)
    score = 0
    
    
    for uni in unidades:
        #Unidade tem que pertencer ao exercito
        if obter_exercito(uni) == s:
            
            score += obter_vida(uni)
            
    return score
            
            
def simula_turno(m): #mapa -> mapa (Recebe um mapa e devolve um mapa)
    
    """Funcao que modifica o mapa dado, de modo a que cada unidade presente
    efetue um movimento seguindo as regras dadas. Portanto, em cada turno de
    batalha, uma unidade pode mover, atacar, mover e atacar ou nao realizar
    movimento nenhum."""
    
    #Ja se encontram ordenadas com a ordem de leitura correta
    unidades = obter_todas_unidades(m)
 
    for uni in unidades:    
        
        #So existe turno de a unidade estiver "viva"
        if eh_unidade(uni):
            
            #Existem inimigos ao lado da unidade?
            if obter_inimigos_adjacentes(m,uni) != ():
                
                #Primeiro inimigo da ordem de leitura
                ini = obter_inimigos_adjacentes(m,uni)[0]
                
                #Ataque matou inimigo?
                if unidade_ataca(uni,ini):
                    
                    eliminar_unidade(m,ini) #Retira do mapa
            
            #Acaba turno se exercitos inimigos foram destruidos antes dos movimentos        
            elif len(obter_nome_exercitos(m)) < 2:
                break
                    
            #Caso nao haja inimigos adjacentes, mover se possivel
            elif obter_movimento(m,uni) != obter_posicao(uni):
                
                mover_unidade(m, uni, obter_movimento(m,uni))
                
                #Existem inimigos ao lado da unidade?
                if obter_inimigos_adjacentes(m,uni) != ():
                    
                    #Primeiro inimigo da ordem de leitura
                    ini = obter_inimigos_adjacentes(m,uni)[0]                
                    
                    #Ataque matou inimigo?
                    if unidade_ataca(uni,ini):
                        
                        eliminar_unidade(m,ini) #Retira do mapa               
                   
            
    return m


def simula_batalha(file,verboso): #str x booleano -> str (Recebe uma string e um valor booleano e retorna uma string)
    
    """Funcao que simula a batalha inteira do mapa a partir das condicoes dadas,
    fornecidas por um ficheiro. O ficheiro e constituido por 6 tuplos em 6 linhas
    correspondentes a: dimensao do mapa, dados do primeiro exercito, dados do
    segundo exercito, posicoes das paredes interiores do mapa, posicoes das 
    unidades do primeiro exercito, posicoes das unidades do segundo exercito,
    respetivamente.
    
    A funcao tambem recebe um valor booleano. Se True, esta retorna a batalha 
    completa, se False, esta so retorna o mapa inicial e o resultado da batalha."""
    
    file = open(str(file), 'r')
    
    #Interpretacao do ficheiro
    dim = eval(file.readline()) # Nx, Ny
    exer1 = eval(file.readline()) #Nome, vida, forca
    exer2 = eval(file.readline()) #Nome, vida, forca
    w = eval(file.readline()) #Posicoes
    posicoes1 = eval(file.readline()) #Posicoes
    posicoes2 = eval(file.readline()) #Posicoes
    
    file.close()
    
    #Criacao dos exercitos
    e1, e2 = (), ()
    
    #Exercito 1
    for p in posicoes1:
        #Posicao, vida, forca, nome
        e1 += cria_unidade(p, exer1[1], exer1[2], exer1[0]),
   
    #Exercito 2
    for p in posicoes2:
        #Posicao, vida, forca, nome
        e2 += cria_unidade(p, exer2[1], exer2[2], exer2[0]),    
        
    #Criacao do mapa
    m = cria_mapa(dim, w, e1, e2)
     
    #Simulacao de batalha
    
    #Nomes dos exercitos
    armies = obter_nome_exercitos(m)
    army1 = armies[0]
    army2 = armies[1]

    
    if verboso: #Verboso if True
        
        #Representacao do mapa no estado inicial 
        print(mapa_para_str(m))
        print('[',army1 + ':' + str(calcula_pontos(m,army1)), \
              army2 + ':' + str(calcula_pontos(m,army2)),']')   

        while True:
            
            mc = cria_copia_mapa(m)
            
            #Mapa vai se repetir?
            if mapas_iguais(m,simula_turno(mc)):
                #Se sim, sair do ciclo
                break
            
            #Representacao do turno novo
            print(mapa_para_str(simula_turno(m)))
            print('[',army1 + ':' + str(calcula_pontos(m,army1)), \
              army2 + ':' + str(calcula_pontos(m,army2)),']')   
            
        
    else: #Quiet if False
        
        #Representacao do mapa no estado inicial 
        print(mapa_para_str(m))
        print('[',army1 + ':' + str(calcula_pontos(m,army1)), \
              army2 + ':' + str(calcula_pontos(m,army2)),']')    
        
        while True:
            
            mc = cria_copia_mapa(m) 
            
            #Mapa vai se repetir?
            if mapas_iguais(m,simula_turno(mc)):
                #Se sim, sair do ciclo
                break
            
            m = simula_turno(m)
                        
            
        #Representacao do mapa no estado final 
        print(mapa_para_str(m))
        print('[',army1 + ':' + str(calcula_pontos(m,army1)), \
              army2 + ':' + str(calcula_pontos(m,army2)),']')        
        
              
    #Resultado:
    if calcula_pontos(m,army1) == 0:
        #Exercito 1 perdeu
        return army2
    
    elif calcula_pontos(m,army2) == 0:
        #Exercito 2 perdeu
        return army1
    
    else:
        #Nao existe vencedor
        return('EMPATE')    
    