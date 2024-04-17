# CRUD
# C = Create
# R = Read
# U = Update
# D = Delete

import pandas as pd
from tabulate import tabulate
import mysql.connector
from datetime import datetime

# Conexão com o banco de dados

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '8yA@12.20kw',
    database = 'almoxarifado_db'
)
cursor = conexao.cursor ()
# ___________________________#
# Menu do app 

# def menu():
#     print("_____________________________________________________________")
#     print("Bem vindo ao sistema de controle de estoque do almoxarifado!")
#     print("Escolha uma opção:")
#     print("1 - Inserir novo produto")
#     print("2 - Visualizar produtos")
#     print("3 - Atualizar/alterar produto")
#     print("4 - Deletar produto")
#     print("_____________________________________________________________")






# Função para validar data
def valida_data(data_em_string): #o que é esse dentro do parenteses?
    try:
        datetime.strptime(data_em_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# def create():
#     Descricao = input("Insira a descrição do produto: ")
#     Unidade = input("Insira o tipo de unidade do produto: ")
#     Quantidade = float(input("Insira a quantidade de produto: "))
#     Valor_unitario = float(input("Insira o valor unitário do produto: "))
#     Nome_Fornecedor = input("Insira o nome do fornecedor: ")

#     # Solicitando a data com validação
#     Data_emissao_NF = input("Insira a data de emissão da nota fiscal (formato AAAA-MM-DD): ")
#     while not valida_data(Data_emissao_NF):
#         print("Data inválida, por favor insira uma data no formato AAAA-MM-DD.")
#         Data_emissao_NF = input("Insira a data de emissão da nota fiscal (formato AAAA-MM-DD): ")

#     num_NF = int(input("Insira o número da nota fiscal: "))
#     Almoxarife = input("Insira o nome do almoxarife responsável: ")
#     Setor_requerinte = input("Insira o setor requerente: ")

#     print('_____________________________________________________________')
#     print('Tem certeza que deseja adicionar o produto acima?')
#     print('1 - Sim')
#     print('2 - Não')

#     opcao = int(input('Escolha uma opção: '))

#     if opcao == 1:
#         comando = f'INSERT INTO entrada (Descricao, Unidade, Quantidade, Valor_unitario, Nome_Fornecedor, Data_emissao_NF, num_NF, Almoxarife, Setor_requerinte) VALUES ("{Descricao}", "{Unidade}", {Quantidade}, {Valor_unitario}, "{Nome_Fornecedor}", "{Data_emissao_NF}", {num_NF}, "{Almoxarife}", "{Setor_requerinte}")'
#         cursor.execute(comando)
#         conexao.commit()
#         print("Produto inserido com sucesso!")
#         cursor.close()
#         print('_____________________________________________________________')
#         print('Deseja adicionar outro produto?')
#         print('1 - Sim')
#         print('2 - Não')
#         print('_____________________________________________________________')
#         opcao2 = int(input('Escolha uma opção: '))
#         if opcao2 == 1:
#             create()
#             print('_____________________________________________________________')
#         else:
#             print('Operação cancelada.')
#             print('_____________________________________________________________')
#     else:
#         print('Operação cancelada.')
#         print('_____________________________________________________________')
#         create()

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
                print('Operação cancelada.')
                print('_____________________________________________________________')
        else:
            print('Operação cancelada.')
            print('_____________________________________________________________')
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        cursor.close()
        conexao.close()
        
    

# --Caso queira editar use o comando abaixo
# --conexao.commit()
# --caso queira visualizar
# --resultado = cursor.fetchall() 

# ----------------------------#
# READ - 0.1

# comando = f'select * from almoxarifado_db.entrada'
# cursor.execute(comando)
# resultado = cursor.fetchall()
# df = pd.DataFrame(resultado, columns=['id_Entrada' ,'Descricao', 'Unidade', 'Quantidade', 'Valor_unitario', 'Valor_total' , 'Nome_Fornecedor', 'Data_emissao_NF', 'num_NF', 'Almoxarife', 'Setor_requerinte'])
# print(tabulate(df, headers='keys', tablefmt='psql'))


# ----------------------------#
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



create()

cursor.close() # alteração imediata
conexao.close() # fechamento da conexão


