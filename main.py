import numpy as np

#Setando variáveis necessárias para a entrada ao programa
nome = ''
senha = ''
cadastro = False

#Menu com repetição para login
while True:
    print('')
    print('>>>CHEVOTECH<<<')
    print('---------------')
    print('1. Fazer Cadastro')
    print('2. Fazer login')
    print('3. Sair')
    print('---------------')

    opcao_login = int(input("Digite o número da opção que deseja: "))

    #Interações com o menu
    match opcao_login:

        #Cadastrar
        case 1:
            print('')
            print('>>>CHEVOTECH<<<')
            print('---------------')
            nome_cadastro = input('Digite seu login para cadastro: ')
            nome = nome_cadastro
            senha_cadastro = input('Digite sua senha para cadastro: ')
            senha = senha_cadastro
            cadastro = True
            print('Cadastro realizado!')

        #Login
        case 2:
            if cadastro:
                print('')
                print('>>>CHEVOTECH<<<')
                print('---------------')
                nome_login = input('Digite seu login: ')
                senha_login = input('Digite sua senha: ')

                if nome_login == nome and senha_login == senha:
                    lista_manutencoes = []
                    dados_sensores = []

                    #Menu principal do programa
                    while True:
                        print('')
                        print('>>>CHEVOTECH<<<')
                        print('---------------')
                        print('Bem vindo! O que deseja fazer?')
                        print('1. Coletar dados dos sensores')
                        print('2. Prever manutenção')
                        print('3. Adicionar data da manutenção')
                        print('4. Histórico de manutenção')
                        print('5. Sair')

                        opcao_menu = input('Digite o número da opção que deseja: ')

                        match opcao_menu:
                            #Coletar dados do sensor (usado np.random para gerar numeros fictícios)
                            case '1':
                                print('')
                                dados_sensores.extend(np.random.rand(10))
                                print('Dados dos sensores coletados com sucesso!')

                            #Prever manutenção necessária com base nos dados gerados pelo sensor
                            case '2':
                                threshold = 0.8
                                print('')
                                if np.mean(dados_sensores) > threshold:
                                    print('Manutenção recomendada.')
                                else:
                                    print('Nenhuma manutenção necessária!')

                            #Adicionar ultima manutenção feita a uma lista
                            case '3':
                                print('')
                                manutencao = input('Adicione a data da manutenção feita (dd/MM/yyyy): ')
                                lista_manutencoes.append(manutencao)

                            #Mostrar lista de todas as manutenções feitas
                            case '4':
                                print('')
                                print(f'Manutenções feitas nos dias: {lista_manutencoes}')

                            #Sair do programa
                            case '5':
                                print('')
                                print('LogOut feito! Obrigado!')
                                break

                            #Caso nenhuma opção for válida
                            case _:
                                print('')
                                print('Digite uma opção válida!')



                else:
                    print('Login inválido!')

            else:
                print('')
                print('Realize o cadastro para fazer login!')

        #Sair do programa
        case 3:
            print('Obrigado!')
            break

        #Caso nenhuma opção for válida
        case _:
            print('')
            print('Digite uma opção válida.')
