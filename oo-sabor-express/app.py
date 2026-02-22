from model.restaurante import Restaurante

kandoo = Restaurante("Kandoo", "Sushi")
madalosso = Restaurante("Madalosso", "Buffet")
perez = Restaurante("Perez", "Pizza")

kandoo.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()