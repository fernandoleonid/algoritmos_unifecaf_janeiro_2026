def escrever_arquivo(tarefa):
    arquivo = open ('banco_dados.txt','a')
    arquivo.write(tarefa + '\n')
    arquivo.close()

def ler_arquivo ():
    arquivo = open ('banco_dados.txt','r')
    conteudo = arquivo.read()
    arquivo.close()
    return conteudo

def atualizar_arquivo(tarefas):
    arquivo = open ('banco_dados.txt','w')
    arquivo.write(tarefas + '\n')
    arquivo.close()