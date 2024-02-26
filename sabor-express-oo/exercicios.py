# # Exercicio sobre Classes

# # Crie uma classe Música poderia ter 3 atributos que trazem as características ou propriedades de um objeto

# class musica:
#     nome = ''
#     artista = ''
#     duracao = 0 # em segundos

# musica_1 = musica()
# musica_1.nome = 'Ainda é cedo'
# musica_1.artista = 'Legião Urbana'
# musica_1.duracao = 180

# musica_2 = musica()
# musica_2.nome = 'Tempo Perdido'
# musica_2.artista = 'Legião Urbana'
# musica_2.duracao = 240

# print(musica_1.artista)

# #Outra maneira de fazer a mesma coisa é utilizando o método construtor __init__:

# class Musica:
#     def __init__(self, nome='', artista='', duracao=0):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao

# musica1 = Musica(nome='Chop Suey', artista='System of a Down', duracao=180)
# musica2 = Musica(nome='Toxicity', artista='System of a Down', duracao=240)
# musica3 = Musica(nome='Guajira', artista='Yerba Buena', duracao=300)

# print(musica1.artista)

# # Ou seja, a classe Musica com __init__ é uma maneira mais elegante de criar a classe, pois já cria os atributos e os inicializa com os valores passados como parâmetros, sem a necessidade de criar os atributos e depois atribuir os valores.
# # Agora, eu me desafiei, com a ajuda do chatGPT, a criar um método de inserir via input musicas e artistas, e depois listar as musicas e artistas cadastrados.

# class Concurso_de_Musicas: #Classe init para criar um objeto
#     def __init__(self, nome='', artista='', duracao=0):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao

# musicas = [] #Lista para armazenar as músicas

# def adicionar_musica(): #Função para adicionar músicas     
#     nome = input('Digite o nome da música: ') #Input para o usuário digitar o nome da música
#     artista = input('Digite o nome do artista: ') #Input para o usuário digitar o nome do artista
#     duracao = int(input('Digite a duração da música em segundos: ')) #Input para o usuário digitar a duração da música em segundos

#     nova_musica = Concurso_de_Musicas(nome, artista, duracao) #Instancia um novo objeto da classe Musica
#     musicas.append(nova_musica) #Adiciona o novo objeto à lista de músicas

# adicionar_musica() #Chama a função para adicionar músicas

# for musica in musicas: #Percorre a lista de músicas
#     print(f'{musica.nome} - {musica.artista} - {musica.duracao} segundos')


# # Aqui percebi que minha curva de aprendizado para classes em Python é acentuada, e decidi voltar ao básico da classe init, e praticar mais um pouco.
# # O chatGPT me sugeriu utilizar uma estrutura basica de uma classe com o método __init__
    
# class NomeDaClasse: #Vou utilizar esse modelo para criar uma classe
#     def __init__(self, parametro1, parametro2):
#         self.atributo1 = parametro1
#         self.atributo2 = parametro2

# class Carro

class Carro:
    def __init__ (self, ano, modelo, cor):
        self.ano = ano
        self.modelo = modelo
        self.cor = cor

novo_carro = Carro('2022', 'Celta', 'Preto')

print(vars(novo_carro))

# class musica

class Musica:
    def __init__ (self, nome_da_musica, artista, album):
        self.nome_da_musica = nome_da_musica
        self.artista = artista
        self.album = album

nova_musica = Musica('Chop Suey', 'System of a Down', 'Toxicity')

print(vars(nova_musica))

#class Cadastro_pessoa

class Cadastro_pessoa:
    def __init__ (self, nome_da_pessoa, cpf, data_de_nascimento):
        self.nome_da_pessoa = nome_da_pessoa
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento

novo_cadastro = Cadastro_pessoa('Caique', '000.000.000-0', '12/34/5678')

print(vars(novo_cadastro))
