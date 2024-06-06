from time import sleep
import textwrap

# Função "menu" irá mostrar as opções que o usuário tem
def menuFun():
    menu = """

    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q]  Sair

    => """
    print(menu)


def saqueFun(saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Opção de saque, não deve permitir mais que 3 saques diários
    # e nem um valor acima de seu saldo em conta. Deve armazenar a
    # operação no extrato e no saldo.
        if valor > saldo:
            print("Saldo insuficiente para realizar a operação.")
        elif valor > limite:
            print("O valor sacado não deve ser maior que R$500.00.")
        elif numero_saques >= limite_saques:
            print("O número de saques diários foi atingido.")
        else:
            saldo -= valor
            extrato += f"R$-{valor:.2f} "
            numero_saques += 1
            print("Saque realizado com sucesso.")
            
            return saldo, extrato


def depositoFun(saldo, valor, extrato):
    # Opção de depósito, deve receber somente valores positivos
    # que devem ser armazenados no extrato e no saldo.
        if valor <= 0:
            print("Valor inválido para depósito.")
        else:
            saldo += valor
            extrato += f"R${valor:.2f} "

        return saldo, extrato


def extratoFun(saldo, extrato):
    # Opção de extrato, deve mostrar o histórico de operações.
    # Adicionei um timer entre os valores com a função sleep.
        print("Segue abaixo seu extrato:")
        if extrato == "":
            print("Não ocorreram movimentações na conta.")
            print("Saldo: R$0.00")
        else:
            for i in extrato.split():
                sleep(0.5)
                print(i)
            print(f"Saldo: R${saldo:.2f}")


def sairFun():
    # Opção de sair, optei por colocar um timer com a função sleep
    # para indicar um "processamento" do computador ao fechar o programa.
    print("Saindo", end='')
    for i in range(3):
        sleep(0.5)
        print(".", end='')
    print("")


def criarUser(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtraUser(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtraUser(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None


def criarConta(agencia, numero_conta, usuarios):
     cpf = input("Informe seu CPF: ")
     usuario = filtraUser(cpf, usuarios)

     if usuario:
          print("\n=== Conta criada com sucesso! ===")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}


def listarConta(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))     


def main():

    # As variáveis que serão usadas ao longo do programa
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"
    
    # Looping infinito em que o usuário escolhe quando sair do programa
    while True:

        # Input do usuário que deve ser "d", "s", "e" ou "q"
        opcao = input(menuFun())

        if opcao == "d":
            valor = float(input(("Digite o valor do depósito: R$")))
            saldo, extrato = depositoFun(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: R$"))
            saldo, extrato = saqueFun(saldo=saldo, 
                                    valor=valor, 
                                    extrato=extrato, 
                                    limite=limite, 
                                    numero_saques=numero_saques, 
                                    limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            extratoFun(saldo, extrato=extrato)
        
        elif opcao == 'nc':
             numero_conta = len(contas) + 1
             conta = criarConta(AGENCIA, numero_conta, usuarios)

        elif opcao == 'lc':
             listarConta(contas)

        elif opcao == 'nu':
             criarUser(usuarios)
        
        elif opcao == "q":
            sairFun()
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()