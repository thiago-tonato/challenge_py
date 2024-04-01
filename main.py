nome = ''
senha = ''

while True:
    print('')
    print('>>>CHEVOTECH<<<')
    print('---------------')
    print('1. Fazer Cadastro')
    print('2. Fazer login')
    print('3. Sair')
    print('---------------')

    opcao = int(input("Digite o número da opção que deseja: "))

    match opcao:
        case 1:
            print('')
            print('>>>CHEVOTECH<<<')
            print('---------------')
            nome_cadastro = input('Digite seu login para cadastro: ')
            nome = nome_cadastro
            senha_cadastro = input('Digite sua senha para cadastro: ')
            senha = senha_cadastro

        case 2:
            print('')
            print('>>>CHEVOTECH<<<')
            print('---------------')
            nome_login = input('Digite seu login: ')
            senha_login = input('Digite sua senha: ')

            if nome_login!=nome and senha_login!=senha:
                print('Login inválido!')

            else:
                while True:
                    print('>>>CHEVOTECH<<<')
                    print('---------------')
                    print('Bem vindo! O que deseja fazer?')
                    print('1. ')
                    print('2. ')
                    print('3. ')
        
        case 3:
            print('Obrigado!')
            break

        case _:
            print('')
            print('Digite uma opção válida.')