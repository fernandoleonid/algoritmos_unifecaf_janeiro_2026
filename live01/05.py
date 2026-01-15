senha_cadastrada = "unifecaf123"

senha_digitada = input ("Digite sua senha: ")

while senha_digitada != senha_cadastrada:
    print ("Senha incorreta, tente novamente!")
    senha_digitada = input ("Digite sua senha: ")

print ("Sistema XYZ iniciando...")