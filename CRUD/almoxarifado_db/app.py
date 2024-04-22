import pandas as pd
from tabulate import tabulate
import mysql.connector
from datetime import datetime

# Conexão com o banco de dados MySQL
conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8yA@12.20kw',
    database = 'almoxarifado_db'
)

cursor = conexao.cursor ()

# Menu do app   
def menu():
    print("_____________________________________________________________")
    print("Bem vindo ao sistema de controle de estoque do almoxarifado!")
    print("Escolha uma das opções abaixos:")
    print("1 - Inserir novo produto")
    print("2 - Visualizar produtos")
    print("3 - Atualizar/alterar produto")
    print("4 - Deletar produto")
    print("5 - Sair do programa")
    print("_____________________________________________________________")
    opcao = int(input("Digite o nº da opção: "))
    try:
        opcao = int(opcao)
        if opcao == 1:
            create()
        elif opcao == 2:
            read()
        elif opcao == 3:
            pass #update()
        elif opcao == 4:
            pass #delete()
        elif opcao == 5:
            print("Saindo do programa...")
        else:
            print('Opção inválida, por favor tente novamente.')
    except:
        print('Opção invalida, tente novamente')

# Função para validar data
def valida_data(data_em_string):
    try:
        datetime.strptime(data_em_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def create():
    try:
        Descricao = input("Insira a descrição do produto: ")
        Unidade = input("Insira o tipo de unidade do produto: ")
        Quantidade = float(input("Insira a quantidade de produto: "))
        Valor_unitario = float(input("Insira o valor unitário do produto: "))
        Nome_Fornecedor = input("Insira o nome do fornecedor: ")

        # Solicitando a data com validação
        Data_emissao_NF = input("Insira a data de emissão da nota fiscal (formato AAAA-MM-DD): ")
        while not valida_data(Data_emissao_NF):
            print("Data inválida, por favor insira uma data no formato AAAA-MM-DD.")
            Data_emissao_NF = input("Insira a data de emissão da nota fiscal (formato AAAA-MM-DD): ")

        num_NF = int(input("Insira o número da nota fiscal: "))
        Almoxarife = input("Insira o nome do almoxarife responsável: ")
        Setor_requerinte = input("Insira o setor requerente: ")

        print('_____________________________________________________________')
        print('Tem certeza que deseja adicionar o produto acima?')
        print('1 - Sim')
        print('2 - Não')

        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            comando = 'INSERT INTO entrada (Descricao, Unidade, Quantidade, Valor_unitario, Nome_Fornecedor, Data_emissao_NF, num_NF, Almoxarife, Setor_requerinte) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            valores = (Descricao, Unidade, Quantidade, Valor_unitario, Nome_Fornecedor, Data_emissao_NF, num_NF, Almoxarife, Setor_requerinte)
            cursor.execute(comando, valores)
            conexao.commit()
            print("Produto inserido com sucesso!")
            print('_____________________________________________________________')
            print('Deseja adicionar outro produto?')
            print('1 - Sim')
            print('2 - Não')
            print('_____________________________________________________________')
            opcao2 = int(input('Escolha uma opção: '))
            if opcao2 == 1:
                create()
                print('_____________________________________________________________')
            else:
                print('Voltando ao menu principal')
                print('_____________________________________________________________')
                menu()
        else:
            print('Operação cancelada.')
            print('_____________________________________________________________')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        cursor.close()
        conexao.close()

def read():
    comando = f'select * from almoxarifado_db.entrada'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    df = pd.DataFrame(resultado, columns=['id_Entrada' , 'Descricao' , 'Unidade' , 'Quantidade' , 'Valor_unitario' , 'Valor_total' , 'Nome_Fornecedor', 'Data_emissao_NF', 'num_NF', 'Almoxarife', 'Setor_requerinte'])
    print(tabulate(df, headers='keys', tablefmt='psql'))


# UPDATE - precisa atualizar

# nome_produto = "Café"
# valor = 1
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

# ----------------------------#
# DELETE - precisa atualizar

# nome_produto = "Café"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit()

def main():
    menu()

cursor.close() # alteração imediata
conexao.close() # fechamento da conexão

if __name__ == '__main__':
    main()