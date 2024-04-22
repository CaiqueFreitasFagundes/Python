class Avaliacao: #Classe que representa a avaliação de um cliente.
    def __init__(self, cliente, nota): #Método construtor da classe.
        self._cliente = cliente #Utilizamos o _ para indicar que o atributo é privado.
        self._nota = nota
        