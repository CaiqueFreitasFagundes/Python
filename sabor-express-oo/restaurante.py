class Restaurante:#Classe sempre com a primeira letra maiúscula.
    restaurantes = []
    def __init__(self, nome, categoria):#O Init é um método especial que é chamado quando um objeto é criado a partir de uma classe. Ele é o construtor da classe. 
        
        # O Self é uma referência ao objeto que está sendo criado, ele é usado para acessar os atributos e métodos do objeto. 

        self._nome = nome.title() #self.nome é chamado, pois queremos acessar o atributo nome do objeto que está sendo criado, e além de acessar, damos o valor nome a ele, que foi passado como parâmetro na criação do objeto, lá no __init__. Assim, quando o objeto é criado, ele já é criado com o atributo nome preenchido. Foi modificado para self._nome para que o atributo seja privado.
        
        self._categoria = categoria.upper() #O mesmo acontece com a categoria.   

        self._ativo = False 

        Restaurante.restaurantes.append(self) #Adiciona o objeto à lista de restaurantes.

    def __str__(self):#Método para retornar uma string com as informações do objeto, quando o objeto é passado como parâmetro para a função print. 
        return f'Nome: {self._nome} | Categoria: {self._categoria}'
    
    def listar_restaurantes():#Método estático para listar os restaurantes cadastrados. Não recebe o self como parâmetro, pois não é um método de instância.

        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property #o property é um decorador que permite que o método seja chamado como um atributo, sem a necessidade de usar os parênteses. Ele oferece a possibilidade de criar um método que se comporta como um atributo.

    def ativo(self):
        return '✔️' if self._ativo else '❌'

# Instanciando a classe Restaurante
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('pizza Express', 'Italiana')
restaurante_pizza._ativo = True

Restaurante.listar_restaurantes()