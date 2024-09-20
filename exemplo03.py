# Digitar o tamanho da matriz
n = int(input('Digite a dimensão n da matriz: '))
m = int(input('Digite a dimensão m da matriz: '))
matriz = []

matriz2 = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(0)
    matriz.append(linha)

for i in range(n):
    matriz2.append(['x']*m)

print(matriz)
print(matriz2)