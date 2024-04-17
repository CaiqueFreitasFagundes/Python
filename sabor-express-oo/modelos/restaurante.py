from modelos.avaliacao import Avaliacao #Importamos a classe Avaliacao do módulo avaliacao.

class Restaurante:#Classe sempre com a primeira letra maiúscula.

    restaurantes = []
    def __init__(self, nome, categoria):#O Init é um método especial que é chamado quando um objeto é criado a partir de uma classe. Ele é o construtor da classe. 
        
        # O Self é uma referência ao objeto que está sendo criado, ele é usado para acessar os atributos e métodos do objeto. 

        self._nome = nome.title() #self.nome é chamado, pois queremos acessar o atributo nome do objeto que está sendo criado, e além de acessar, damos o valor nome a ele, que foi passado como parâmetro na criação do objeto, lá no __init__. Assim, quando o objeto é criado, ele já é criado com o atributo nome preenchido. Foi modificado para self._nome para que o atributo seja privado.
        
        self._categoria = categoria.upper() #O mesmo acontece com a categoria.   

        self._ativo = False 

        self._avaliacao = [] #Lista para armazenar as avaliações do restaurante.

        Restaurante.restaurantes.append(self) #Adiciona o objeto à lista de restaurantes.

    def __str__(self):#Método para retornar uma string com as informações do objeto, quando o objeto é passado como parâmetro para a função print. 
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    @classmethod #O classmethod é um decorador que permite que o método seja chamado a partir da classe, sem a necessidade de criar um objeto. Ele é usado para criar métodos que operam na classe em si, e não em instâncias da classe.

    def listar_restaurantes(cls):#Método estático para listar os restaurantes cadastrados. Não recebe o self como parâmetro, pois não é um método de instância.

        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property #o property é um decorador que permite que o método seja chamado como um atributo, sem a necessidade de usar os parênteses. Ele oferece a possibilidade de criar um método que se comporta como um atributo.

    def ativo(self):  #Método para verificar se o restaurante está ativo ou não.
        return '✔️' if self._ativo else '❌'
    
    def alternar_estado(self): #Método para alternar o estado do restaurante. Método para alterar o objeto.
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota): #Método para receber a avaliação do cliente.
        avaliacao = Avaliacao(cliente, nota) 
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1) 
        
        return media
    