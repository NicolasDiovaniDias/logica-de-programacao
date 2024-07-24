# Gerenciamento de Alunos com Menu Interativo em Python
# Objetivo:

# Desenvolver um programa em Python que utilize um menu interativo para gerenciar informações de alunos em um conjunto de listas. O programa deve permitir ao usuário:

# Inserir novos alunos: v
# Solicitar o nome completo do aluno.  Lista => Alunos v
# Solicitar a nota de cada disciplina (até 4 notas). Listas => nota1, nota2, nota3 e nota4 v
# Armazenar os dados do aluno em uma lista de forma organizada que o índice do aluno seja equivalente no índice das notas. v
# Listar todos os alunos: v
# Apresentar o nome completo de cada aluno, juntamente com suas respectivas notas. v
# Calcular a média da turma : v
# Listar todos alunos e notas v
# calcular media das notas da turma e calcular media total da turma v 
# Buscar um aluno por nome: v 
# Solicitar o nome completo do aluno. v 
# Verificar se o aluno existe na lista de alunos. v
# Se o aluno for encontrado, exibir suas informações completas (nome e notas). v
# Calcular e exibir as notas e a média aritmética das notas do aluno encontrado nas listas nota1, nota2, nota3 e nota4 v
# Se o aluno não for encontrado, informar que a busca não obteve resultados. v
# Detalhes Adicionais:
# O programa deve utilizar um menu interativo para apresentar as opções ao usuário.v
# As informações dos alunos devem ser armazenadas em um conjunto de listas, onde cada aluno é representado por uma sublista contendo seu nome e suas notas.v
# O programa deve ser robusto e capaz de lidar com entradas incorretas do usuário. x
# Utilize funções para modularizar o código e torná-lo mais organizado. v
# Adicione comentários explicativos no código para facilitar sua compreensão x
import sys
alunos=[]
qnt_alunos=int(input("quantos alunos voce quer inserir? "))
def inicializacao():
    opcao=input("voce deseja fazer alguma das opções abaixo?\n1-adicionar mais alunos\n2-procurar um aluno\n3-mostrar notas de todos os alunos\n4-não\n")
    if opcao=="1":
        mais_alunos=int(input("quantos alunos voce quer adicionar a mais?"))
        adicionar(mais_alunos)
    if opcao=="2":
        procurar()
    if opcao=="3":
        mostrar_alunos()
    if opcao=="4":
        print("tchau")
        sys.exit()
    else:
        print("voce digitou um valor invalido")
        inicializacao()
def adicionar(num):
    for i in range(num):
        nome=input("digite o nome do aluno: ")
        nota1=input("primeira nota: ")
        nota2=input("segunda nota: ")
        nota3=input("terceira nota: ")
        nota4=input("quarta nota: ")
        media=(int(nota1)+int(nota2)+int(nota3)+int(nota4))/4
        aluno={"nome":nome,"nota1":nota1,"nota2":nota2,"nota3":nota3,"nota4":nota4,"media":round(media,2)}
        alunos.append(aluno)
    inicializacao()

def procurar():
    nome=input("qual aluno voce esta procurando? ")
    for i in range(len(alunos)):
        if nome in alunos[i]["nome"]:
            print(f'o aluno esta na lista {i}! ')
            ver_aluno=input("voce quer ver as informações do aluno? \n1-sim\n2-não\n")
            if ver_aluno=='1':
                mostrar_aluno(i)
                inicializacao()
            elif ver_aluno=='2':
                print("ok")
                return
            else:
                print("valor invalido")
                return
    print("o aluno não foi encontrado")
    inicializacao()

def mediatotal():
    media_total=0
    for i in range(len(alunos)):
        media_total+=int(alunos[i]["media"])
    print(f"media total       {media_total/len(alunos)}\n")
    inicializacao()

def mostrar_aluno(num):
    for tags in alunos[num].keys():
            print(f"{tags:<7} {alunos[num][tags]}")

def mostrar_alunos():
    for i in range(len(alunos)):
        for tags in alunos[i].keys():
            print(f"{tags:<7} {alunos[i][tags]}")
        print("\n")
    mediatotal()
    inicializacao()

adicionar(qnt_alunos)
inicializacao()