produtos = [
    'Teclado', 
    'Mouse', 
    'CPU',
    'wifi',
    'GPU', 
    'RAM', 
    'Monitor',
    'Impressora'
]

contador = 0

limite = len(produtos)

while contador < limite:
    print (f' --> {produtos [contador]}')
    contador += 1