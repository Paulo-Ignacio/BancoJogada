# Dicionário para armazenar usuários
usuarios = {}

# Dicionário para armazenar contas correntes
contas = {}

def cadastrar_usuario(nome, cpf):
    if cpf in usuarios:
        print("Usuário já cadastrado.")
    else:
        usuarios[cpf] = {"nome": nome, "cpf": cpf}
        contas[cpf] = {"saldo": 0.0, "extrato": []}
        print(f"Usuário {nome} cadastrado com sucesso.")

def login(cpf): # Grupo 1
    if cpf in usuarios:
        print(f"Login bem-sucedido. Bem-vindo(a), {usuarios[cpf]["nome"]}!")
        return True
    else:
        print("Usuário não encontrado.")
        return False

def depositar(cpf, valor):
    if cpf in contas:
        contas[cpf]["saldo"] += valor
        contas[cpf]["extrato"].append(f"Depósito: +R${valor:.2f}")
    else:
        print("Usuário não encontrado.")

def sacar(cpf, valor):
    if cpf in contas:
        if valor > contas[cpf]["saldo"]:
            print("Saldo insuficiente.")
        else:
            contas[cpf]["saldo"] -= valor
            contas[cpf]["extrato"].append(f"Saque: -R${valor:.2f}")
    else:
        print("Usuário não encontrado.")

def transferir(cpf_origem, cpf_destino, valor):
    if cpf_origem in contas and cpf_destino in contas:
        if valor > contas[cpf_origem]["saldo"]:
            print("Saldo insuficiente para transferência.")
        else:
            contas[cpf_origem]["saldo"] -= valor
            contas[cpf_destino]["saldo"] += valor
            contas[cpf_origem]["extrato"].append(f"Transferência enviada: -R${valor:.2f} para {usuarios[cpf_destino]['nome']}")
            contas[cpf_destino]["extrato"].append(f"Transferência recebida: +R${valor:.2f} de {usuarios[cpf_origem]['nome']}")
    else:
        print("Usuário de origem ou destino não encontrado.")

def gerar_extrato(cpf):
    if cpf in contas:
        print(f"Extrato da conta de {usuarios[cpf]['nome']} (CPF: {usuarios[cpf]['cpf']}):")
        for item in contas[cpf]["extrato"]:
            print(item)
        print(f"Saldo atual: R${contas[cpf]['saldo']:.2f}")
    else:
        print("Usuário não encontrado.")

def editar_usuario(cpf):
    if cpf in usuarios:
        novo_nome = input("Digite o novo nome: ").strip()
        usuarios[cpf]['nome'] = novo_nome
        print(f"Dados do usuário {cpf} atualizados para: {usuarios[cpf]}")
    else:
        print("Usuário não encontrado.")

# Adicione a função fechar_conta aqui
# Adicione a função consultar_saldo aqui

# Menu Interativo = Grupo 1 
def menu():
    logado = False
    while not logado:
        print("===== Sistema Bancário =====")
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Digite o nome: ").strip()
            cpf = input("Digite o CPF: ").strip()
            cadastrar_usuario(nome, cpf)
        
        elif opcao == "2":
            cpf = input("Digite o CPF: ").strip()
            logado = login(cpf)
            if logado:
                while logado:
                    print("===== Menu Principal =====")
                    print("1. Depositar")
                    print("2. Sacar")
                    print("3. Transferir")
                    print("4. Gerar extrato")
                    print("5. Editar usuário")
                    print("6. Fechar conta")
                    print("7. Consultar saldo")
                    print("0. Sair")
                    
                    opcao = input("Escolha uma opção: ")
                    
                    if opcao == "1":
                        valor = float(input("Digite o valor a ser depositado: "))
                        depositar(cpf, valor)
                    
                    # elif opcao == "2":
                        
                    # elif opcao == "3":
                        
                    # elif opcao == "4":
                        
                    # elif opcao == "5":
                        
                    # elif opcao == "6": # Adicionado o "logado = false" para tirar o login, basta criar e adicionar a função
                    #     logado = False

                    # elif opcao == "7":
                        
                    elif opcao == "0":
                        print("Saindo do sistema...")
                        logado = False
                    
                    else:
                        print("Opção inválida. Por favor, tente novamente.")
        
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executar o menu
menu()
