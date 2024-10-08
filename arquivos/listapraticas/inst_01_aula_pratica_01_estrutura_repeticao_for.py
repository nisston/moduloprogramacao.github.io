# -*- coding: utf-8 -*-
"""Inst_01_Aula_Pratica_01_Estrutura_Repeticao_For

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mIOYFenH1Eb5TV6oHybKd5qxilB29179

# Estrutu

Aqui vamos apresentar todos os tópicos discutidos em sala de aula pelo professor, com uma ou duas células com exemplos práticos da aplicação do comando ou recurso. A seguir a lista de tópicos trabalhados:

* Estruturas de repetição
* Comando de repetição “for”
* Estruturas de repetição aninhadas



Para maiores informações segue um pequeno tutorial: [Tutorial de Python](https://docs.python.org/pt-br/3/reference/compound_stmts.html#index-4)

# Estrutura de repetição for
"""

# Estrutura for simples
for i in range(5):
    print("Contador é:", i)

# Estrutura for com else:
for i in range(5):
    print(i)
else:
    print("Laço completo!")

"""# Comandos break e continue"""

# Sai do laço quando i for 5
for i in range(10):
    if i == 5:
        break
    print(i)

# Pula a iteração atual se i for par
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)