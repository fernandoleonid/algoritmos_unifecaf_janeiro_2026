from manipulando_arquivos import *
import os 

def mostrar_tarefas():
    tarefas = ler_arquivo().splitlines()
    limpar_tela()
    print ('--- TAREFAS CADASTRADAS ---')
    for indice, tarefa in enumerate(tarefas):
        print (f'{indice} - {tarefa}')

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input ('Digite ENTER para continuar...')

def exibir_menu():
    limpar_tela()
    print ('-- SISTEMA XYZ --')
    print ('1 - Adicionar tarefa')
    print ('2 - Ler tarefas')
    print ('3 - Atualizar tarefa')
    print ('4 - Excluir tarefa')
    print ('0 - Sair')   

def selecionar_menu(opcao):
    if opcao == '1':
        tarefa = input ('Digite uma tarefa: ')
        escrever_arquivo(tarefa)

    elif opcao == '2':
        mostrar_tarefas()
        pausar()

    elif opcao == '3':
        mostrar_tarefas()
        indice = int(input('Escolha a tarefa para atualizar: '))
        tarefa_editada = input ('Digite a nova tarefa: ') 
        tarefas = ler_arquivo().splitlines()
        tarefas[indice] = tarefa_editada
        tarefas_atualizadas =  '\n'.join(tarefas)
        atualizar_arquivo(tarefas_atualizadas)

    elif opcao == '4':
        mostrar_tarefas()
        indice = int(input('Escolha a tarefa para excluir: '))
        tarefas = ler_arquivo().splitlines()
        del tarefas[indice]
        tarefas_atualizadas =  '\n'.join(tarefas)
        atualizar_arquivo(tarefas_atualizadas)

    elif opcao  == '0':
        print ('Saindo do Sistema...')
        exit(0)
    else:
        print ('Opção incorreta, tente novamente!')
        

def sistema():
    exibir_menu()
    opcao = input('Escolha uma opção: ')
    selecionar_menu(opcao)
    sistema()

sistema()