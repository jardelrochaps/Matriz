# Preencher a matriz por leitura
turma = []
for i in range(3):
    # cria linha vazia
    linha = []
    for j in range(5):
         #vai pedindo e adicionando as notas na linha
         nota = int(input('Digite a nota['+ str(1) + ',' + str(j) + ']: '))
         linha.append(nota)

    turma.append(linha)
    print(turma)