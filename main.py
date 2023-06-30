import os

valorConta = 0
lista = []

def add_extrato(natureza, valor):
    global lista
    if natureza == "deposito":
        lista.append("R$" + "+" + str(valor))
    elif natureza == "saque":
        lista.append("R$" + "-" + str(valor))
    else:
        print("ERROR 404 NATUREZA INVÁLIDA")

def extrato():
    global valorConta
    print("\n \n \n \nExtrato:")
    for item in lista:
        print(item)
    print("Seu saldo é: R$", valorConta)

def deposito(valor):
    global valorConta
    valorConta = valor + valorConta
    add_extrato("deposito", valor)
    
def saque(valor):
    global valorConta
    valorConta = valorConta - valor
    add_extrato("saque", valor)

sistema = int(input("1-Windows 2-Linux:  "))

while True:
    print('_' * 32)
    print("Seja bem-vindo ao Banco do Kayke")
    print('_' * 32)

    print("Sistema Bancário:\nPara saque digite 1\nPara depósito digite 2\nPara extrato digite 3\nPara sair digite 0")
    operacao = int(input("Entrada: "))
    
    if operacao == 0:
        print("Operação finalizada")
        extrato()
        break
    elif operacao == 1:
        valor_saque = int(input("Valor do saque: "))
        saque(valor_saque)
        input("Aperte qualquer tecla para limpar terminal")
        if (sistema == 1):
            os.system('cls')
        elif (sistema == 2):
            os.system('clear')
        else:
            continue
    elif operacao == 2:
        valor_deposito = int(input("Valor do depósito: "))
        deposito(valor_deposito)
        input("Aperte qualquer tecla para limpar terminal")
        if (sistema == 1):
            os.system('cls')
        elif (sistema == 2):
            os.system('clear')
        else:
            continue
    elif operacao == 3:
        extrato()
        input("Aperte qualquer tecla para limpar terminal")
        if (sistema == 1):
            os.system('cls')
        elif (sistema == 2):
            os.system('clear')
        else:
            continue
    else:
        print("Entrada inválida")
