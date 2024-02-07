'''Exercicios de pratica com dicionarios referente ao curso: Python: crie a sua primeira aplicação'''


# Tema: Prática com dicionários
# Exercícios
# # 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

cadastro_pessoa = [{'nome': 'Caique', 'idade': 31, 'cidade': 'São Paulo'},
                   {'nome': 'Dara', 'idade': 27, 'cidade': 'Cerro Azul'},
                   {'nome': 'Douglas', 'idade': 22, 'cidade': 'Curitiba'}
]


# # 2 - Utilizando o dicionário criado no item 1:
# # Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);

cadastro_pessoa[0]['idade']= 32

# # Adicione um campo de profissão para essa pessoa;

cadastro_pessoa[0][profissao] = 'Desenvolvedor'

# # Remova um item do dicionário.

cadastro_pessoa[0].pop('cidade')

# # 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

numeros_quadrados = {'1': 1, '2': 4, '3': 9, '4': 16, '5': 25}

# # 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

dicionario = {'nome': 'Caique', 'idade': 31, 'cidade': 'São Paulo'}

idade = dicionario.get('idade')
print(idade)

#  ou 

idade = dicionario['idade'] if 'idade' in dicionario else 'Chave não encontrada'
print(idade)

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = 'O rato roeu a roupa do rei de Roma'
palavras = frase.split()
frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1
print(frequencia)

