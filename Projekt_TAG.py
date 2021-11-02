# Codigo feito por: Isaque Augusto da Silva Santos, Matricula: 190089245
# Projeto 3 de Teoria e Aplicação de Grafos, Turma A, 2021/1
# Prof. Dibio
import random
import copy


def find_blank(matrix):     # acha um espaço vazio
    for k in range(9):
        for y in range(9):
            if getkeys(matrix[k][y]) == 0:
                i = k
                j = y
                return i, j
    return -1, -1


def ispossible(i, j, valor, matriz):    # checa se um valor é possível para determinado espaço vazio do sudoku
    print(f"Analisando linha I: {i} e coluna J: {j}")
    for k in range(20):     # numero de vizinhos de um vertice
        if matriz[i][j][getkeys(matriz[i][j])][k] == valor:
            return False
    return True


def getkeys(dictionary):    # pega a key (valor do vértice)
    for key in dictionary.items():
        return key[0]


def sudoku_print(matriz):
    contador = 0
    for i in range(9):
        for j in range(9):
            if contador == 8:
                print(str(getkeys(matriz[i][j])) + "\n")
                contador = -1
            else:
                getkeys(matriz[i][j])
                print(str(getkeys(matriz[i][j])) + "    ", end="")
            contador += 1


def criar_vetor():
    vetor_de_valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return vetor_de_valores


def sudoku_initiate(matriz_sudoku=None):
    if matriz_sudoku is None:
        matriz_sudoku = [
            [{0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}],
            [{0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}],
            [{0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}],
            [{0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}],
            [{0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}],
            [{0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}],
            [{0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}],
            [{0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}],
            [{0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}, {0: []}]
        ]
    vertex = []
    for i in range(9):
        vertex.append([])
    for a in range(9):
        for b in range(9):
            vertex[a].append(graph_neighbors_block(matriz_sudoku[a][b], a, b, matriz_sudoku))
    return vertex


def solvesudoku(matrix, i=0, j=0):
    # adaptação do código que pode ser encontrado no endereço
    # https://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku
    # foi usado como base o algoritmo de Welsh Powell para coloração de grafos
    # mas com adaptações e com o uso de backtracking para definir a solução única do sudoku
    global new_matrix
    new_matrix = []
    for r in range(9):
        new_matrix.append([])
    i, j = find_blank(matrix)
    if i == -1 and j == -1:
        return True
    ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(ll)
    for e in ll:
        if ispossible(i, j, e, matrix):
            old_key = getkeys(matrix[i][j])
            matrix[i][j][e] = matrix[i][j].pop(old_key)
            new_matrix = []
            for r in range(9):
                new_matrix.append([])
            for a in range(9):
                for b in range(9):
                    new_matrix[a].append(graph_neighbors_block(matrix[a][b], a, b, matrix))
            print("--------------PASSO DA SOLUÇÃO--------------\n\n")
            sudoku_print(new_matrix)
            i, j = find_blank(matrix)
            if i == -1 and j == -1:     # significa que não existe espaço para ser preenchido
                return True
            if solvesudoku(new_matrix, i, j):
                return True
            old_key = getkeys(matrix[i][j])
            matrix[i][j][0] = matrix[i][j].pop(old_key)
            new_matrix = []
            for r in range(9):
                new_matrix.append([])
            for a in range(9):
                for b in range(9):
                    new_matrix[a].append(graph_neighbors_block(matrix[a][b], a, b, matrix))
            matrix = copy.deepcopy(new_matrix)
    return False


def create_sudoku(matrix, i=0, j=0):
    # o método para criar um sudoku válido foi: solucionar um sudoku de tabuleiro vazio (todos números = 0)
    # e apagar randômicamente algumas posições do sudoku, nesse caso 15 posições aleatórias
    global new_matrix
    new_matrix = []
    for r in range(9):
        new_matrix.append([])
    i, j = find_blank(matrix)
    if i == -1 and j == -1:
        return True
    ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(ll)
    for e in ll:
        if ispossible(i, j, e, matrix):
            old_key = getkeys(matrix[i][j])
            matrix[i][j][e] = matrix[i][j].pop(old_key)
            new_matrix = []
            for r in range(9):
                new_matrix.append([])
            for a in range(9):
                for b in range(9):
                    new_matrix[a].append(graph_neighbors_block(matrix[a][b], a, b, matrix))
            i, j = find_blank(matrix)
            if i == -1 and j == -1:
                ll.remove(9)
                ll.append(0)
                for i in range(15):     # apaga 15 posições aleatórias do sudoku
                    w = random.choice(ll)
                    x = random.choice(ll)
                    odd_k = getkeys(new_matrix[w][x])
                    new_matrix[w][x][0] = new_matrix[w][x].pop(odd_k)
                sudoku_print(new_matrix)
                return True
            if create_sudoku(new_matrix, i, j):
                return True
            old_key = getkeys(matrix[i][j])
            matrix[i][j][0] = matrix[i][j].pop(old_key)
            new_matrix = []
            for r in range(9):
                new_matrix.append([])
            for a in range(9):
                for b in range(9):
                    new_matrix[a].append(graph_neighbors_block(matrix[a][b], a, b, matrix))
            matrix = copy.deepcopy(new_matrix)
    return False


def graph_neighbors_block(vertice, i, j, matrix):    # acha os vizinhos de um vértice no grafo
    find = False
    matrix2 = copy.deepcopy(matrix)
    matrix2[i].pop(j)
    vertice[getkeys(vertice)] = []
    for k in matrix2[i][:]:  # todos os elementos na mesma linha
        vertice[getkeys(vertice)].append(getkeys(k))
    for k in range(9):
        if k == i:
            continue
        else:
            vertice[getkeys(vertice)].append(getkeys(matrix2[k][j]))
    for o in range(0, 7, 3):
        if find:
            break
        for p in range(0, 7, 3):
            if i == 0 + o and j == 0 + p:
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j + 1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+2][j + 2]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j + 2]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+2][j + 1]))
                find = True
                break
            if i == 0 + o and j == 1 + p:
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+2][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i + 1][j + 1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i + 2][j + 1]))
                find = True
                break
            if i == 0 + o and j == 2 + p:
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+2][j-2]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j-2]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+2][j-1]))
                find = True
                break
            if i == 1 + o and j == 0 + p:
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j+1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j+2]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j+1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j+2]))
                find = True
                break
            if i == 1 + o and j == 1 + p:
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j+1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j+1]))
                find = True
                break
            if i == 1 + o and j == 2 + p:
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j-2]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j-2]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i+1][j-1]))
                find = True
                break
            if i == 2 + o and j == 0 + p:
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j+1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j+2]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-2][j+1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-2][j+2]))
                find = True
                break
            if i == 2 + o and j == 1 + p:
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-2][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j+1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-2][j+1]))
                find = True
                break
            if i == 2 + o and j == 2 + p:
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-1][j-2]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-2][j-1]))
                vertice[getkeys(vertice)].append(getkeys(matrix2[i-2][j-2]))
                find = True
                break
    return vertice


sudoku = sudoku_initiate()
create_sudoku(sudoku)
print("\n**Sudoku randômico gerado com sucesso**")
new_matrix = sudoku_initiate(new_matrix)
input("\n\n"
      "**Pressione qualquer tecla e aperte ENTER para ver a solução do Sudoku passo a passo**"
      "\n\n")
solvesudoku(new_matrix)
print("\n**Essa é a solução passo a passo do Sudoku**\n\n")

