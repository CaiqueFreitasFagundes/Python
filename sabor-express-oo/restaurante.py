class Restaurante:#Classe sempre com a primeira letra maiúscula.
    restaurantes = []
    def __init__(self, nome, categoria):#O Init é um método especial que é chamado quando um objeto é criado a partir de uma classe. Ele é o construtor da classe. 
        
        # O Self é uma referência ao objeto que está sendo criado, ele é usado para acessar os atributos e métodos do objeto. 

        self.nome = nome #self.nome é chamado, pois queremos acessar o atributo nome do objeto que está sendo criado, e além de acessar, damos o valor nome a ele, que foi passado como parâmetro na criação do objeto, lá no __init__. Assim, quando o objeto é criado, ele já é criado com o atributo nome preenchido.
        self.categoria = categoria #O mesmo acontece com a categoria.     
        self.ativo = False 
        Restaurante.restaurantes.append(self) #Adiciona o objeto à lista de restaurantes.

    def __str__(self):#Método para retornar uma string com as informações do objeto, quando o objeto é passado como parâmetro para a função print. 
        return f'Nome: {self.nome} - Categoria: {self.categoria} - Ativo: {self.ativo}'
    
    def listar_restaurantes():#Método estático para listar os restaurantes cadastrados. Não recebe o self como parâmetro, pois não é um método de instância.
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} - {restaurante.categoria} - {restaurante.ativo}')

# Instanciando a classe Restaurante
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Fast Food')

Restaurante.listar_restaurantes()