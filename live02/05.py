def mensagem ():
    print ('#'*30)
    print ('Live 02 - Lista, dicionários e funções')
    print ('#'*30)

mensagem ()


def verificar_situacao (nota):
    if nota >= 5:
        print ("Aprovado")
    else:
        print ("Reprovado")


verificar_situacao(4.5)

def calcular_media (nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

media = calcular_media(9, 8)
print (media)

# --> Responsabilidade única
# --> Função pura