from model.restaurante import Restaurante
from model.cardapio.bebida import Bebida
from model.cardapio.prato import Prato

kandoo = Restaurante("Kandoo", "Sushi")
madalosso = Restaurante("Madalosso", "Buffet")
perez = Restaurante("Perez", "Pizza")

kandoo.alternar_estado()
kandoo.receber_avaliacao('Alan', 10)

bebida = Bebida('Suco', 9.90, "Grande")
bebida.aplicar_desconto()
prato = Prato('Sfiha', 3.99, 'Carne')
prato.aplicar_desconto()

kandoo.adicionar_no_cardapio(bebida)
kandoo.adicionar_no_cardapio(prato)

def main():
    # Restaurante.listar_restaurantes()
    kandoo.exibir_cardapio



if __name__ == '__main__':
    main()