import os

restaurantes = []

def limpar():
    os.system('clear')

def retornar_menu_principal():
    input('Digite uma tecla para voltar ao menu principal ')
    main()

def exibir_nome_do_programa():
    print("----- SABOR EXPRESS -----\n")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def listar_restaurantes():
    limpar()
    print('Listando os restaurantes:\n')

    for restaurante in restaurantes:
        print(f'- {restaurante}')
    
    retornar_menu_principal()

def finalizar_app():
    limpar()
    print('Finalizando...')

def opcao_invalida():
    print('Opcao invalida')
    retornar_menu_principal()

def cadastrar_novo_restaurante():
    limpar()
    print('Cadastro de novos restaurantes\n')

    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso')
    retornar_menu_principal()

def alternar_status_restaurante():
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            retornar_menu_principal()
        else:
            print('Restaurante nao encontrado')
            retornar_menu_principal()
    

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()