#Definir valores

def main():
    saldo = 0
    extrato = []
    LIMITE_SAQUE = 500
    numero_saques = 3
    saques_diarios = 0

#Disponibilizar opções

    while True:
        print("\n====== Banco do Léo :D ======")
        print("")
        print("d. Depositar")
        print("s. Sacar")
        print("e. Extrato")
        print("q. Sair")
        print("")
        opcao = input("Escolha uma opção: ")

#Opção "Depositar"

        if opcao == "d":
            valor = float(input("Insira o valor do depósito: "))
            
            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f}")
                print(f"Depósito: R$ {valor:.2f} ")
            
            else:
                print("ERRO: Insira um valor válido.")

#Opção "Sacar"

        elif opcao == "s":
            
            if saques_diarios >= numero_saques:
                print("ERRO: Limite de saques diário atingido.")
           
            else:
                valor = float(input("Insira o valor do saque: "))
                
                if valor > saldo:
                    print("ERRO: Saldo insuficiente.")
                
                elif valor > LIMITE_SAQUE:
                    print(f"ERRO: Valor excede o limite por saque.")
                
                elif valor > 0:
                    saldo -= valor
                    saques_diarios += 1
                    extrato.append(f"Saque: R$ {valor:.2f}")
                    print(f"Saque: R$ {valor:.2f} ")
                
                else:
                    print("ERRO: Insira um valor válido.")

#Opção "Extrato"

        elif opcao == "e":
            print("\n====== EXTRATO ======")

            if not extrato:
                print("Sem movimentações recentes.")
                
            else:
                for item in extrato:
                    print(item)
                print(f"\nSaldo: R$ {saldo:.2f}")

#Opção "Sair"

        elif opcao == "q":
            print("Obrigado escolher o Banco do Léo :D")
            break

        else:
            print("ERRO: Escolha uma opção válida.")

if __name__ == "__main__":
    main()
