print("")
print("----- U.R.S.A - Unity of Resolution for Software and Application -----")
print("")
print("Seja bem-vindo(a) ao serviço de vistoria de bicicletas!")
print("Para ter acesso as nossas funcionalidades, realize um cadastro.")
print("")

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
senha = input("Crie uma senha: ")

print("")
print("Cadastro realizado com sucesso! Agora vamos efetuar um login, ok?")

emailLogin = input("Email: ")
senhaLogin = input("Senha: ")

print("")
    
if emailLogin == email and senhaLogin == senha:
    print("Olá", nome + "!")
    continuar = 1
    while continuar == 1:
        funcionalidade = int(input("Digite o número correspondente à operação desejada:\n1 - Cadastrar Bicicleta\n2 - Cadastrar Acessórios\n"))
        match funcionalidade:
            case 1:
                print("Vamos cadastrar sua bicicleta!")
                marcaBicicleta = input("Digite a marca: ")
                modelo = input("Digite o modelo: ")
                valorBicicleta = float(input("Quanto custou($)? "))
                numeroSerie = input("Digite o número de série da sua bicicleta: ")
                print("")
                print("Sucesso! :)") 
                print("Sua bicicleta é da marca", marcaBicicleta + ", do modelo", modelo, "e custou R$", str(valorBicicleta) + ".")
                print("O número de série da sua bicicleta é", numeroSerie + ". Usaremos ele para identificação da bicicleta.")
                print("")
                print("Deseja realizar alguma outra operação?")
                continuar = int(input("Digite 1 para SIM e qualquer outro número para NÂO:\n"))
            case 2:
                print("Vamos cadastrar um acessório!")
                acessorio = input("Digite o nome: ")
                tipo = input("Digite o tipo: ")
                marcaAcessorio = input("Digite a marca: ")
                valorAcessorio = float(input("Quanto custou($)? "))
                print("")
                print("Sucesso! :)")
                print("O", acessorio, "é do tipo", tipo + ", da marca", marcaAcessorio, "e custou R$", str(valorAcessorio) + ".")
                print("")
                print("Deseja realizar alguma outra operação?")
                continuar = int(input("Digite 1 para SIM e qualquer outro número para NÂO:\n"))
            case _:
                input("Opção inválida! Escolha uma das opções diponíveis!")
    print("Obrigada por escolher os nossos serviços " + nome + "! Até breve!")
else:
    print("Email ou senha incorreta. Tente novamente!")