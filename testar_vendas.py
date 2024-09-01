from produto import Produto
from venda import Venda

def exibir_menu():

    print("\nMenu de Vendas")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Listar produtos da venda")
    print("4. Mostrar total da venda")
    print("5. Sair")
    return int(input("Escolha uma opção: "))

def main():

    produtos = []
    data_venda = input("Digite a data da venda (dd/mm/aaaa): ")
    venda = Venda(produtos, data_venda)

    while True:
        opcao = exibir_menu()

        if opcao == 1:
            
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))
            produto = Produto(nome, preco, quantidade)
            venda.get_produtos().append(produto)
            venda.set_produtos(venda.get_produtos())
            print("Produto adicionado com sucesso!")

        elif opcao == 2:
            nome = input("Nome do produto a remover: ")
            produto_encontrado = False
            for produto in venda.get_produtos():
                if produto.get_nome() == nome:
                    venda.get_produtos().remove(produto)
                    venda.set_produtos(venda.get_produtos())
                    produto_encontrado = True
                    print("Produto removido com sucesso!")
                    break
            if not produto_encontrado:
                print("Produto não encontrado!")

        elif opcao == 3:
            if venda.get_produtos():
                print("\nProdutos na venda:")
                for produto in venda.get_produtos():
                    print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco()}, Quantidade: {produto.get_quantidade()}")
            else:
                print("Nenhum produto na venda.")

        elif opcao == 4:
            print(f"Total da venda: R${venda.get_total():.2f}")

        elif opcao == 5:
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
