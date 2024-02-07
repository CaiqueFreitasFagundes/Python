import os
import time

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                { 'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}
                ]

def exibir_subtitulo(texto):
    ''' Exibe um texto formatado como um subtitulo'''

    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def finalizar_app():
    exibir_subtitulo('Finalizando o app\n')

def opcao_invalida():
    '''Exibe uma mensagem de erro para opções inválidas e retorna ao menu principal.'''

    exibir_subtitulo('\nOpção invalida!' ,'Voltando ao Menu de opções\n')
    time.sleep(4)
    os.system('cls')
    main()   

def exibir_nome_do_programa():
    exibir_subtitulo('\nBem vindo ao Sabor Express\n')

def exibir_opcoes():
    '''Exibe as opções do menu principal do programa.'''

    print('Escolha uma das opçoes abaixo:')
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    '''Cadastra um novo restaurante na lista de restaurantes.'''

    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso.')

    print('Voltando ao menu principal em alguns segundos.')
    time.sleep(6)
    main()

def listar_restaurantes():
    '''Exibe a lista de restaurantes cadastrados'''


    exibir_subtitulo('Lista dos restaurantes:\n')

    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante ['nome']
        categoria = restaurante ['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    input('\nAperte ENTER para voltar ao menu principal')
    main()

def alternar_estado_restaurante():
    '''Altera o estado de um restaurante entre ativo e desativado.'''

    os.system('cls')
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input ('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante ['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante ['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    print('Voltando ao menu principal em alguns segundos.')
    time.sleep(4)
    main()
    

def escolher_opcao():
    '''Espera o usuário escolher uma opção do menu principal e chama a função correspondente.'''
    
    try:
        opcao_escolhida = int(input('Escolha uma opção:   '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal do programa.'''

    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()