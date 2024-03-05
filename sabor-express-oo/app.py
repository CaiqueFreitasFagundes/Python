from modelos.restaurante import Restaurante #Importamos a classe Restaurante do módulo restaurante. Logo em seguida, criamos três objetos da classe Restaurante, passando os parâmetros nome e categoria.

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

# Para comprovar que o código está rodando, chamamos o método listar_restaurantes da classe Restaurante, que lista os restaurantes cadastrados, e em seguida, chamamos o método alternar_estado do objeto restaurante_praca, que altera o estado do restaurante.
restaurante_praca.alternar_estado()

# No def main(), chamamos o método listar_restaurantes da classe Restaurante, que lista os restaurantes cadastrados. Logo em seguida, por meio do if __name__ == '__main__', chamamos a função main(), que é a função principal do programa. 
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()