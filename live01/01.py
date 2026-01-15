nome = input("Digite seu nome: ")
idade = int(input ("Digite sua idade: "))

ano_atual = 2026

ano_nascimento = ano_atual - idade

print ("#"*30)
print (f"{nome} você nasceu em: {ano_nascimento}")