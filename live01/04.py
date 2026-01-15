contador = 1
nome_aluno = input ("Digite seu nome: ")
soma = 0

while contador <= 4:
    nota = float (input("Digite sua nota: "))
    contador += 1
    soma += nota

media = soma / 4

if media >= 5:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print (f"{nome_aluno} sua média é: {media:.1f} e você está {situacao}")