from os import system

opc = ''
saldo = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


print("Bem-vindo ao banco Py")

while  True:
    print("O que deseja?\n\n")

    print("1 - Realizar saque")
    print("2 - Realizar Deposito")
    print("3 - Consultar Extrato")
    print("q - Sair")
    opc = input(f"->")

    if opc == '1':
        saque  = int(input("Quanto deseja sacar? "))
        if saque > saldo:
            print("Não é possivel realizar a ação")
            system("pause")
            system("cls")
        elif saque <= 0:
            print("Não é possivel sacar valores menores que ZERO")
            system("pause")
            system("cls")
        elif saldo == 0:
            print("Saldo insuficiente!")
            system("pause")
            system("cls")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Excedeu seu limite de saque diario ({LIMITE_SAQUES})")
            system("pause")
            system("cls")
        else:
            saldo -= saque
            print(f"Você sacou R$:{saque}, lhe restam R$:{saldo}")
            numero_saques += 1
            extrato += f"Saque: R$:{saque}\n"
            system("pause")
            system("cls")
            
    elif opc == '2':
        deposito = int(input("Quanto deseja depositar?"))
        if deposito < 0:
            print("Não é possivel depositar números menores que ZERO")
            system("pause")
            system("cls")
            break
        else:
            saldo += deposito
            print("Deposito realizado com sucesso!")
            print(f"Seu saldo agora é de : R$:{saldo}")
            extrato += f"Deposito: R$:{deposito}\n"
            system("pause")
            system("cls")
    elif opc == '3':
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$:{saldo}")
        system("pause")
        system("cls")
    elif opc == 'q':
        break