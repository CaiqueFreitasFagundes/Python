class Restaurante:#Classe sempre com a primeira letra maiúscula.
    restaurantes = []
    def __init__(self, nome, categoria):#Método construtor, que é chamado quando um objeto é instanciado. O self é uma referência ao próprio objeto.
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):#Método para retornar uma string com as informações do objeto, quando o objeto é passado como parâmetro para a função print. 
        return f'Nome: {self.nome} - Categoria: {self.categoria} - Ativo: {self.ativo}'
    
    def listar_restaurantes():#Método estático para listar os restaurantes cadastrados. Não recebe o self como parâmetro, pois não é um método de instância.
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} - {restaurante.categoria} - {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Fast Food')

Restaurante.listar_restaurantes()