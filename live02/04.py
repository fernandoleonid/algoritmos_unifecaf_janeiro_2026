### Listas + Dicionários ###

alunos = [
    {
        'nome': 'Ana',
        'idade': 22,
        'notas': [
            4.0,
            6.7,
            9.0
        ]
    },
    {
        'nome': 'Pedro',
        'idade': 44,
        'notas': [
            7.0,
            9.0,
            9.5
        ]
    }
]

alunos [1]['nome'] = 'Pedo da Silva'

print (alunos[1]['notas'][2])