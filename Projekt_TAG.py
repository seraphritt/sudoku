# Codigo feito por: Isaque Augusto da Silva Santos, Matricula: 190089245
# Projeto 3 de Teoria e Aplicação de Grafos, Turma A, 2021/1
# Prof. Dibio
import random


def criar_vetor():
    vetor_de_valores = [" ", 1, 2, 3, 4, " ", 5, 6, 7, 8, " ", 9]
    return vetor_de_valores


def sudoku_start():
    matriz_sudoku = []
    for k in range(9):
        matriz_sudoku.append([])
    v = criar_vetor()
    for i in range(3):  # preenche cada bloco do sudoku
        for j in range(3):
            valor = random.choice(v)
            matriz_sudoku[i].append(valor)
            v.remove(valor)  # remove temporarimente o valor para que ele não seja escolhido novamente
    v = criar_vetor()
    for i in range(3, 6):
        for j in range(3):
            valor = random.choice(v)
            matriz_sudoku[i].append(valor)
            v.remove(valor)  # remove temporarimente o valor para que ele não seja escolhido novamente
    v = criar_vetor()
    for i in range(6, 9):
        for j in range(3):
            valor = random.choice(v)
            matriz_sudoku[i].append(valor)
            v.remove(valor)  # remove temporarimente o valor para que ele não seja escolhido novamente
    v = criar_vetor()
    for i in range(3):
        for j in range(3, 6):
            valor = random.choice(v)
            matriz_sudoku[i].append(valor)
            v.remove(valor)  # remove temporarimente o valor para que ele não seja escolhido novamente
    v = criar_vetor()
    for i in range(3, 6):
        for j in range(3, 6):
            valor = random.choice(v)
            matriz_sudoku[i].append(valor)
            v.remove(valor)  # remove temporarimente o valor para que ele não seja escolhido novamente
    v = criar_vetor()
    for i in range(3, 6):
        for j in range(6, 9):
            valor = random.choice(v)
            matriz_sudoku[i].append(valor)
            v.remove(valor)  # remove temporarimente o valor para que ele não seja escolhido novamente
    v = criar_vetor()
    for i in range(6, 9):
        for j in range(3):
            valor = random.choice(v)
            matriz_sudoku[i].append(valor)
            v.remove(valor)  # remove temporarimente o valor para que ele não seja escolhido novamente
    v = criar_vetor()
    for i in range(6, 9):
        for j in range(3, 6):
            valor = random.choice(v)
            matriz_sudoku[i].append(valor)
            v.remove(valor)  # remove temporarimente o valor para que ele não seja escolhido novamente
    v = criar_vetor()
    for i in range(6, 9):
        for j in range(6, 9):
            valor = random.choice(v)
            matriz_sudoku[i].append(valor)
            v.remove(valor)  # remove temporarimente o valor para que ele não seja escolhido novamente


sudoku_start()
