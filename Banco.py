menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

        opcao = input(menu)

        if opcao == "d":        
                valor_deposito = float(input("Digite o valor do depósito: "))
                if valor_deposito > 0:
                    saldo += valor_deposito
                    extrato += f"Depósito: +R$ {valor_deposito:.2f}\n"
                    print("Depósito bem sucedido. Novo saldo: R$ {:.2f}".format(saldo))
                else:
                    print("O valor para depósito deve ser positivo.")
                       
                
        elif opcao == "s":
                if numero_saques >= LIMITE_SAQUES:
                    print("Você atingiu seu limite diário de saques.")
                else:
                    valor_saque = float(input("Digite o valor do saque: "))
                if 0 < valor_saque <= 500 and valor_saque <= saldo and numero_saques < LIMITE_SAQUES:
                    saldo -= valor_saque
                    extrato += f"Saque: -R${valor_saque: .2f}\n"
                    numero_saques += 1
                    print("Depósito bem-sucedido. Novo saldo: R$ {:.2f}".format(saldo))
                elif valor_saque > 500:
                    print("O limite máximo para saque é de R$ 500.00")
                elif valor_saque > saldo:
                    print("Saldo insuficiente para saque. Saldo atual: R$ {:.2f}".format(saldo))
        
        elif opcao == "e":
                print("=== Extrato ===")
                print(extrato)
                print("Saldo atual: R$ {:.2f}".format(saldo))
                print("================")

        elif opcao == "q":
                print("Obrigado por utilizar nosso sistema!")
                break
        
        else:
                print("Operação inválida, por favor selecione uma das opções válidas.")