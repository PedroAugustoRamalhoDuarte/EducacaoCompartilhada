import glob
# Variáveis Globais
dict = {}
monitor = ""
materia = ""
ano = 1
# Por acaso queira os arquivos em ordem
"""
list_file = ["files/humanas1.txt",
             "files/humanas2.txt",
             "files/obrasdopas.txt",
             "files/portugues.txt",
             "files/ingles.txt",
             "files/biologia.txt",
             "files/química.txt",
             "files/física.txt",
             "files/matemática.txt",
             ]
"""
for file in glob.glob("files/*.txt"):
    isFirstLine = True
    for line in open(file):
        if isFirstLine:
            materia = line[0:-1]
            dict[materia] = {}
            isFirstLine = False
            continue

        verifyAno = line.split(' ')
        if len(verifyAno) == 2 and verifyAno[1] == "ANO\n":
            ano = verifyAno[0]
        else:
            verifyMonitor = line.split('-')
            if len(verifyMonitor) == 2:
                monitor = line[0:-1]
                dict[materia][monitor] = []
            else:
                dict[materia][monitor].append(line[0:-1])

# Inteface com usuário
while 1:
    print("Digite o nome do(a) aluno(a):")
    nome = input()
    for key_materia, value_materia in dict.items():
        for key, value in value_materia.items():
            if nome in value:
                print(key_materia + ' - ' + key)
