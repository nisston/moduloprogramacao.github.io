# -*- coding: utf-8 -*-
"""Inst_01_Aula_Pratica_02_Estrutura_Repeticao_While

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xwRdgKIxUz0i6G1TW7PQ-mKP94UX_QqH

# Estrutura de repetição While

Aqui vamos apresentar todos os tópicos discutidos em sala de aula pelo professor, com uma ou duas células com exemplos práticos da aplicação do comando ou recurso. A seguir a lista de tópicos trabalhados:

* Estruturas de repetição
* Comando de repetição "While"
* Estruturas de repetição aninhadas



Para maiores informações segue um pequeno tutorial: [Tutorial de Python](https://docs.python.org/pt-br/3/reference/compound_stmts.html#index-4)

# Estrutura de repetição While
"""

# Exemplo prático
contador = 0
while contador < 5:
    print("Contador é:", contador)
    contador += 1

# Estrutura While com if - else
contador = 0
while contador < 5:
    if contador % 2 == 0:
        print(contador, "é par")
    else:
        print(contador, "é ímpar")
    contador += 1

# Estrutura While com else
contador = 0
while contador < 5:
    print("Contador é:", contador)
    contador += 1
else:
    print("Laço while terminou.")

# Trabalhando a estrutura While de maneira aninhada
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

linha = 1
coluna = 1

for x in range(10):
    print(x)

# Definindo dois conjuntos de números
conjunto1 = [1, 2, 3]
conjunto2 = ['a', 'b', 'c']

# Trabalhando a estrutura for de maneira aninhada
for num in conjunto1:
    for letra in conjunto2:
        print(num, letra)

# Lista de números
numeros = [3, 2, 1]

# Laço while externo
indice = 0
while indice < len(numeros):
    num = numeros[indice]

    # Laço for interno
    for i in range(num, 0, -1):
        print(f"Contando a partir de {num}: {i}")

    indice += 1

"""# Comandos break e continue"""

# Sai do laço quando contador for 5
contador = 0
while contador < 10:
    if contador == 5:
        break
    print(contador)
    contador += 1

# Pula a iteração atual se contador for par
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)