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
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
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
            print(f"Transferência de R${valor:.2f} para {usuarios[cpf_destino]['nome']} realizada com sucesso.")
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

def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar usuário")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Transferir")
        print("5. Gerar extrato")
        print("6. Editar usuário")
        print("7. Fechar Conta")
        print("8. Consultar Saldo")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            cpf = input("Digite o CPF do usuário: ")
            cadastrar_usuario(nome, cpf)
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário: ")
            valor = float(input("Digite o valor do depósito: "))
            depositar(cpf, valor)
        elif opcao == "3":
            cpf = input("Digite o CPF do usuário: ")
            valor = float(input("Digite o valor do saque: "))
            sacar(cpf, valor)
        elif opcao == "4":
            cpf_origem = input("Digite o CPF do usuário que vai depositar: ")
            cpf_destino = input("Digite o CPF do usuário que vai receber: ")
            valor = float(input("Digite o valor da transferência: "))
            transferir(cpf_origem, cpf_destino, valor)
        elif opcao == "5":
            cpf = input("Digite o CPF do usuário: ")
            gerar_extrato(cpf)
        elif opcao == "6":
            cpf = input("Digite o CPF do usuário: ")
            editar_usuario(cpf)
        elif opcao == "7":
            cpf = input("Digite o CPF do usuário: ")
            fechar_conta(cpf)
        elif opcao == "8":
            cpf = input("Digite o CPF do usuário: ")
            consultar_saldo(cpf)
        elif opcao == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()