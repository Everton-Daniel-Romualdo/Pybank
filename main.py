#Autor: Everton Daniel de Lima Romualdo
#Email: evertonrdaniel@gmail.com || evertondanieldelimaromualdo@gmail.com
#UFCG-Campina Grande
#Ciência da Computação - 1° Período
#Projeto de aprendizado pessoal
#Data de inicio 23/09/2023
import funtions as fc

while True:
    fc.menu_Inicial()
    opcao = input('O que deseja? ')
    if opcao == "c":
        fc.cadastrar()
    elif opcao == 'l':
        aux = fc.logar()
        if aux == True:
            opcao = ''
            break
    elif opcao == "adm":
        fc.adm()
    

while True:
    fc.menu_principal()
    opcao = input('O que deseja? ')
    if opcao == "c":
        fc.cadastrar()
    elif opcao == 'l':
        fc.logar()
    elif opcao == "d":
        fc.depositar()
    elif opcao == "s":
        fc.sacar()
    elif opcao == "vs":
        fc.ver_saldo()
    elif opcao == "adm":
        fc.adm()
