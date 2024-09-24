# Projeto Funções Banco

menu = """

[d] deposito
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 5
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o Valor do Deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"

        else: 
            print("Operaçao falhou! O valor informado é inválido." )

    elif opcao == "s":
        valor = float(input("Informe o Valor do Saque:"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite." )

        elif excedeu_saques:
            print("Operaçao falhou! Número de saques maximos excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\========= EXTRATO ==========")
        print("Não foram realizaddas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:. 2f}")
        print("============================")
    
    elif opcao == "q":
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
    






        







