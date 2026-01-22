### LISTAS ###

produtos = [
    'Teclado', 
    'Mouse', 
    'CPU',
    'wifi',
    'GPU', 
    'RAM', 
    'Monitor',
    'Impressora',
    'Caixa de som'
]

produtos [1] = 'Mouse sem fio'

for produto in produtos:
    print (f'--> {produto}')