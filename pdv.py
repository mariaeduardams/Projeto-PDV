import time
#Inicialização do estoque
estoque = {
    'Bola': 50,
    'Garrafa': 25,
    'Mochila': 15,
    'Corda': 5,
    'Capa de Chuva': 5
}

#Lista de clientes
clientes = []

#Solicitar nome do cliente e adicionar à lista de clientes
nome = input('Seja bem-vindo(a), digite seu nome: ')
clientes.append(nome)
print('Clientes:', clientes)

#Lista de vendedores disponíveis
vendedores = ['1- Ana', '2- Gabriela', '3- Mariana']

#Exibir lista de vendedores disponíveis
print('Vendedores disponíveis:')
vendedora_nome = None
while True:
    for vendedor in vendedores:
        print(vendedor)

    vendedora = input('Por quem você deseja ser atendido(a) hoje?: ')
    if vendedora == '1':
        vendedora_nome = 'Ana'
        break      
    elif vendedora == '2':
        vendedora_nome = 'Gabriela'
        break
    elif vendedora == '3':
        vendedora_nome = 'Mariana'
        break
    else:
        print('Escolha inválida')

#Verificar se a escolha da vendedora é válida
if vendedora_nome:
    print(f'A vendedora escolhida foi: {vendedora_nome}')

#Variáveis globais(para as variáveis serem executadas no final do código e fora do looping)
imposto_adicional = 0
valor_venda_final = 0
comissao_adicional = 0
vendas_realizadas = []

#Função para retornar o preço do produto
def preco_produto(nome_produto):
        precos = {'Bola': 5, 'Garrafa': 30, 'Mochila': 100, 'Corda': 15, 'Capa de Chuva': 50}
        return precos.get(nome_produto, 0)

#Função para registrar uma venda
def registrar_venda(produto, quantidade_escolhida):
        global imposto_adicional, valor_venda_final, comissao_adicional
        if produto in estoque:
            if quantidade_escolhida <= estoque[produto]:
                estoque[produto] -= quantidade_escolhida
                valor_venda = quantidade_escolhida * preco_produto(produto)
                imposto = valor_venda * 0.25
                comissao = valor_venda * 0.05
                valor_venda_final += valor_venda
                imposto_adicional += imposto
                comissao_adicional += comissao
                vendas_realizadas.append((produto, quantidade_escolhida, valor_venda))
                print(f'{quantidade_escolhida} unidades de {produto} vendidas. Estoque atualizado: {estoque[produto]} unidades disponíveis.')
            else:
                print(f'Quantidade escolhida indisponível. Estoque atual de {produto}: {estoque[produto]} unidades.')
        else:
            print('Produto não encontrado no estoque.')

#Processo de compra
while True:
        print('\nProdutos disponíveis:')
        print('1- Bola')
        print('2- Garrafa')
        print('3- Mochila')
        print('4- Corda')
        print('5- Capa de Chuva')
        
        decisao = input('Qual produto você deseja (1, 2, 3, 4 ou 5)?: ')

        produto_escolhido = '' 
        if decisao == '1':
            produto_escolhido = 'Bola'
        elif decisao == '2':
            produto_escolhido = 'Garrafa'
        elif decisao == '3':
            produto_escolhido = 'Mochila'
        elif decisao == '4':
            produto_escolhido = 'Corda'
        elif decisao == '5':
            produto_escolhido = 'Capa de Chuva'
        else:
            print('Decisão inválida')
            continue
        
        quantidade_escolhida = int(input(f'Quantas unidades de {produto_escolhido} você deseja? '))
        registrar_venda(produto_escolhido, quantidade_escolhida)

        continuar = input('Deseja realizar outra compra? (s/n): ')
        if continuar.lower() != 's':
            break

formas_de_pagamentos = []
print(f'O valor foi de {valor_venda_final} reais, Qual será a forma de pagamento?')
forma_de_pagamentos = input()
formas_de_pagamentos.append(forma_de_pagamentos)
print (f'A o pagamento em {formas_de_pagamentos[0]} sera efetuado em instantes...')
time.sleep (3)
print('pagamento bem sucedido')


#Nota fiscal de forma simplificada
print('\nNota Fiscal')
print(f'Cliente: {nome}')
print(f'Vendedora: {vendedora_nome}')
print('Produtos comprados:')
for venda in vendas_realizadas:
        produto, quantidade, valor = venda
        print(f'{quantidade}x {produto} - R${valor:.2f}')
print(f'\nValor total da compra: R${valor_venda_final:.2f}')
print(f'Imposto total: R${imposto_adicional:.2f}')
print(f'Comissão total da vendedora: R${comissao_adicional:.2f}')