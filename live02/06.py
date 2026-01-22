def mostrar_menu ():
    print ('1 - Somar')
    print ('2 - Subtrair')
    print ('3 - Multiplicar')
    print ('4 - Dividir')
    print ('0 - Sair')

def somar ():
    numero1 = float (input('Digite o primeiro número: '))
    numero2 = float (input('Digite o segundo número: '))
    soma = numero1 + numero2
    print ()
    print (f' --> {soma}')
    print ()

def subtrair ():
    numero1 = float (input('Digite o primeiro número: '))
    numero2 = float (input('Digite o segundo número: '))
    diferenca = numero1 - numero2
    print ()
    print (f' --> {diferenca}')
    print ()

def multiplicar ():
    numero1 = float (input('Digite o primeiro número: '))
    numero2 = float (input('Digite o segundo número: '))
    produto = numero1 * numero2
    print ()
    print (f' --> {produto}')
    print ()

def dividir ():
    numero1 = float (input('Digite o primeiro número: '))
    numero2 = float (input('Digite o segundo número: '))
    resultado = numero1 / numero2
    print ()
    print (f' --> {resultado:.1f}')
    print ()

def escolher_opcao (resposta):
    if resposta == '1':
        somar()
    elif resposta == '2':
        subtrair()
    elif resposta == '3':
        multiplicar()
    elif resposta == '4':
        dividir()
    elif resposta == '0':
        print ('Saindo do Sistema...')
    else:
        print ('Opção errada, tente novamente!')



resposta = ''
while resposta != '0':
    mostrar_menu()
    resposta = input ('Escolha uma opção: ')
    escolher_opcao(resposta)