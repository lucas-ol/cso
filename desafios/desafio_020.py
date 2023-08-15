
from random import shuffle


n1 = input("Informe o nome do primeiro aluno: ")
n2 = input("Informe o nome do segundo aluno: ")
n3 = input("Informe o nome do terceiro aluno: ")
n4 = input("Informe o nome do quarto aluno: ")
list = [n1, n2, n3, n4]
shuffle(list)
print("A ordem de apresentação será")
print(list)