# Codigo feito por: Isaque Augusto da Silva Santos, Matricula: 190089245
# Projeto 3 de Teoria e Aplicação de Grafos, Turma A, 2021/1
# Prof. Dibio
import random
import copy


def find_blank(matrix):
    for k in range(9):
        for y in range(9):
            if getkeys(matrix[k][y]) == 0:
                i = k
                j = y
                return i, j
    return -1, -1


def ispossible(i, j, valor, matriz):
    print(f"I: {i}, J: {j}")
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


# def graph_neighbors_block(matriz_de_vertices):    # define quais são os vizinhos por meio do conceito de linha e coluna
#     # vertices que estão na mesma linha ou coluna são adjacentes
#     for k in range(0, 7, 3):
#         for m in range(0, 7, 3):
#             for i in range(9):
#                 for j in range(9):
#                     if i == 0 + k and j == 0 + m:
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])] = []
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j+1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j+2]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i+1][j]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i+2][j]))
#                     if i == 0 + k and j == 1 + m:
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])] = []
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j-1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j+1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i+1][j]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i+2][j]))
#                     if i == 0 + k and j == 2 + m:
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])] = []
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j-1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j-2]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i+1][j]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i+2][j]))
#                     if i == 1 + k and j == 0 + m:
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])] = []
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j+1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j+2]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i-1][j]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i+1][j]))
#                     if i == 1 + k and j == 1 + m:
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])] = []
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j-1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j+1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i-1][j]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i+1][j]))
#                     if i == 1 + k and j == 2 + m:
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])] = []
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j-1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j-2]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i-1][j]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i+1][j]))
#                     if i == 2 + k and j == 0 + m:
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])] = []
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j+1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j+2]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i-1][j]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i-2][j]))
#                     if i == 2 + k and j == 1 + m:
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])] = []
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j-1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j+1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i-1][j]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i-2][j]))
#                     if i == 2 + k and j == 2 + m:
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])] = []
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j-1]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i][j-2]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i-1][j]))
#                         matriz_de_vertices[i][j][getkeys(matriz_de_vertices[i][j])].append(getkeys(matriz_de_vertices[i-2][j]))


def criar_vetor():
    vetor_de_valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return vetor_de_valores


def sudoku_initiate():
    vertex = []
    matriz_sudoku = [
        [{7: []}, {8: []}, {0: []}, {4: []}, {0: []}, {0: []}, {1: []}, {2: []}, {0: []}],
        [{6: []}, {0: []}, {0: []}, {0: []}, {7: []}, {5: []}, {0: []}, {0: []}, {9: []}],
        [{0: []}, {0: []}, {0: []}, {6: []}, {0: []}, {1: []}, {0: []}, {7: []}, {8: []}],
        [{0: []}, {0: []}, {7: []}, {0: []}, {4: []}, {0: []}, {2: []}, {6: []}, {0: []}],
        [{0: []}, {0: []}, {1: []}, {0: []}, {5: []}, {0: []}, {9: []}, {3: []}, {0: []}],
        [{9: []}, {0: []}, {4: []}, {0: []}, {6: []}, {0: []}, {0: []}, {0: []}, {5: []}],
        [{0: []}, {7: []}, {0: []}, {3: []}, {0: []}, {0: []}, {0: []}, {1: []}, {2: []}],
        [{1: []}, {2: []}, {0: []}, {0: []}, {0: []}, {7: []}, {4: []}, {0: []}, {0: []}],
        [{0: []}, {4: []}, {9: []}, {2: []}, {0: []}, {6: []}, {0: []}, {0: []}, {7: []}]
    ]
    for i in range(9):
        vertex.append([])
    for a in range(9):
        for b in range(9):
            vertex[a].append(graph_neighbors_block(matriz_sudoku[a][b], a, b, matriz_sudoku))
    return vertex


def solvesudoku(matrix, i=0, j=0):      # adaptação do código que pode ser encontrado no endereço
    # https://stackoverflow.com/questions/1697334/algorithm-for-solving-sudoku
    new_matrix = []
    for r in range(9):
        new_matrix.append([])
    i, j = find_blank(matrix)
    if i == 3 and j == 8:
        print("uhum")
    if i == -1 and j == -1:
        return True
    for e in range(1, 10):
        if ispossible(i, j, e, matrix):
            old_key = getkeys(matrix[i][j])
            matrix[i][j][e] = matrix[i][j].pop(old_key)
            new_matrix = []
            for r in range(9):
                new_matrix.append([])
            for a in range(9):
                for b in range(9):
                    new_matrix[a].append(graph_neighbors_block(matrix[a][b], a, b, matrix))
            sudoku_print(new_matrix)
            if solvesudoku(new_matrix, i, j):
                return True
            # Undo the current cell for backtracking
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


# def sudoku_solve(matriz, i=0, j=0):   # utiliza-se o algoritmo Welsh Powell (greedy graph coloring algorithm) com backtracking
#     new_matrix = []
#     for i in range(9):
#         new_matrix.append([])
#     available_colors = criar_vetor()
#     if getkeys(matriz[i][j]) == 0:
#             for k in available_colors:
#                     if ispossible(i, j, k, matriz):
#                         # print("------------------------------------\n\n")
#                         # sudoku_print(matriz)
#                         # print(matriz)
#                         old_key = getkeys(matriz[i][j])
#                         matriz[i][j][k] = matriz[i][j].pop(old_key)
#                         for a in range(9):
#                             for b in range(9):
#                                 new_matrix[a].append(graph_neighbors_block(matriz[a][b], a, b, matriz))
#                         if sudoku_solve(new_matrix):
#                             return True
#                         matriz[i][j][getkeys(matriz[i][j])] = 0
#
#     return False


def graph_neighbors_block(vertice, i, j, matrix):    # vai ser a função q gera a lista de adj
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
print(sudoku)
sudoku_print(sudoku)
print("\n\n*************")
print("SOLVED SUDOKU")
print("*************\n\n")
print(solvesudoku(sudoku))
#
