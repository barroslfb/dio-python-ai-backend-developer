from time import sleep

# Variável "menu" irá mostrar as opções que o usuário tem
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# As variáveis que serão usadas ao longo do programa
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Looping infinito em que o usuário escolhe quando sair do programa
while True:

    # Input do usuário que deve ser "d", "s", "e" ou "q"
    opcao = input(menu)

    # Opção de depósito, deve receber somente valores positivos
    # que devem ser armazenados no extrato e no saldo.
    if opcao == "d":

        deposito = float(input(("Digite o valor do depósito: R$")))
        if deposito <= 0:
            print("Valor inválido para depósito.")
        else:
            saldo += deposito
            extrato += f"R${deposito:.2f} "

    # Opção de saque, não deve permitir mais que 3 saques diários
    # e nem um valor acima de seu saldo em conta. Deve armazenar a
    # operação no extrato e no saldo.
    elif opcao == "s":
        saque = float(input("Digite o valor a ser sacado: R$"))
        if saque > saldo:
            print("Saldo insuficiente para realizar a operação.")
        elif saque > limite:
            print("O valor sacado não deve ser maior que R$500.00.")
        elif numero_saques >= LIMITE_SAQUES:
            print("O número de saques diários foi atingido.")
        else:
            saldo -= saque
            extrato += f"R$-{saque:.2f} "
            numero_saques += 1
            print("Saque realizado com sucesso.")

    # Opção de extrato, deve mostrar o histórico de operações.
    # Adicionei um timer entre os valores com a função sleep.
    elif opcao == "e":
        print("Segue abaixo seu extrato:")
        if extrato == "":
            print("Não ocorreram movimentações na conta.")
            print("Saldo: R$0.00")
        else:
            for i in extrato.split():
                sleep(0.5)
                print(i)
            print(f"Saldo: R${saldo:.2f}")
    
    # Opção de sair, optei por colocar um timer com a função sleep
    # para indicar um "processamento" do computador ao fechar o programa.
    elif opcao == "q":
        print("Saindo", end='')
        for i in range(3):
            sleep(0.5)
            print(".", end='')
        print("")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
