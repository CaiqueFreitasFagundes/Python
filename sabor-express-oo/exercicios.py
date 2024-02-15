# Exercicio sobre Classes

# Crie uma classe Música poderia ter 3 atributos que trazem as características ou propriedades de um objeto

class musica:
    nome = ''
    artista = ''
    duracao = 0 # em segundos

musica_1 = musica()
musica_1.nome = 'Ainda é cedo'
musica_1.artista = 'Legião Urbana'
musica_1.duracao = 180

musica_2 = musica()
musica_2.nome = 'Tempo Perdido'
musica_2.artista = 'Legião Urbana'
musica_2.duracao = 240

print(musica_1.artista)

#Outra maneira de fazer a mesma coisa é utilizando o método construtor __init__:

class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Chop Suey', artista='System of a Down', duracao=180)
musica2 = Musica(nome='Toxicity', artista='System of a Down', duracao=240)
musica3 = Musica(nome='Guajira', artista='Yerba Buena', duracao=300)

print(musica1.artista)
