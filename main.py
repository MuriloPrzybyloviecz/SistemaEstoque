#Sistema de Estoque

def ConsultarProduto():
    for i in range(0, len(produtos)):
        print("Produto {} - {} - RS{:.2f} - Quantidade em estoque: "
              "{}".format(i, produtos[i][0], produtos [i][1], produtos[i][2]))
produtos = []

while True:
    escolha = int(input("\n**************** MENU *******************"
                        "\n-----------------------------------------"
                        "\n------- 1 - Adicionar Produto -----------"
                        "\n------- 2 - Consultar Produto -----------"
                        "\n------- 3 - Remover Produto -------------"
                        "\n------- 4 - Sair do Programa ------------"
                        "\n*****************************************"
                        "\n\nEscolha uma das opções: "))

    if escolha == 1:
        nome = input("Qual o nome do produto? ")
        preço = float(input("Qual o preço do produto? "))
        quantidade = int(input("Qual a quantidade do produto? "))

        produto = []
        produto.append(nome)
        produto.append(preço)
        produto.append(quantidade)
        produtos.append(produto)

    if escolha == 2:
        ConsultarProduto()

    if escolha == 3:
        print("Escolha um produto abaixo: \n")
        ConsultarProduto()

        numero = int(input("\nInforme o número do produto: "))
        quantidade = int(input("Qual a quantidade? "))
        if produtos[numero][2] >= quantidade:
            print("Produto removido com sucesso")
            produtos[numero][2] -= quantidade
        else:
            print("Não foi possível remover, quantidade informada é maior do que o estoque")

    if escolha == 4:
        print("Saindo do programa")
        break