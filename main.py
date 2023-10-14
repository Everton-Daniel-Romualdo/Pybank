#Autor: Everton Daniel de Lima Romualdo
#Email: evertonrdaniel@gmail.com || evertondanieldelimaromualdo@gmail.com
#UFCG-Campina Grande
#Ciência da Computação - 1° Período
#Projeto de aprendizado pessoal
#Data de inicio 23/09/2023
import funtions as fc

opcao_escolhida = '' #Variavel responsavel por coleta o pront do usuario para direcionalo para a função correta
retorno_de_funcao = None #sempre vai receber apenas o retorno de alguma função.
                         #O retorno é True para uma ação feita com sucesso, False caso contrario.
usuario_logado = False #Indica se a um usurio online(True) ou não(False)

while True:
    if usuario_logado == False:
        while True: # while principal do programa
            #Menu inicial
            print("Bem vindo")
            print("Cadastrar Usuario [c]")
            print("Fazer Login [l]")
            opcao_escolhida = input("Selecione uma opção: ")
            
            if opcao_escolhida == "c":
                nome = input("Digite seu nome: ")
                senha = input("Digite sua senha")
                retorno_de_funcao = fc.cadastrar(nome, senha)
                if retorno_de_funcao == True:
                    print("CADASTRO REALIZADO COM SUCESSO!")
                else:
                    print("ERRO: USUARIO JÁ EXISTENTE!")
            elif opcao_escolhida == 'adm':
                fc.adm()
            elif opcao_escolhida == 'l':
                nome = input("Digite seu nome de usuario: ")
                senha = input("Digite sua senha: ")
                retorno_de_funcao = fc.logar(nome, senha)
                if retorno_de_funcao == True:
                    print("LOGIN REALIZADO COM SUCESSO!")
                    usuario_logado = True
                    break
                else:
                    print("NOME DE USUARIO OU SENHA INVALIDOS!")
    if usuario_logado == True:
        while True:
            print("Py Bank")
            print()
            print("Depositar [d]")
            print("Sacar [s]")
            print("Ver Saldo [vs]")
            print("Criar boleto [cb]")
            print("Sair [ex]")
            opcao_escolhida = input("Selecione uma opção: ")

            if opcao_escolhida == 'd':
                valor = input("Digite o valor de deposito: ")
                fc.depositar(valor)
                print(f"DEPOSITO REALIZADO COM SUCESSO! NOVO SALDO DE R$ {fc.user_online[2]}")
            elif opcao_escolhida == 'adm':
                fc.adm()
            elif opcao_escolhida == 's':
                valor = input("Digite o valor do saque: ")
                retorno_de_funcao = fc.sacar(valor)
                if retorno_de_funcao == True:
                    print(f"SAQUE REALIZADO COM SUCESSO! NOVO SALDO DE R${fc.user_online[2]}")
                else:
                    print(f"SALDO INSUFICIENTE! SEU SALDO É DE R${fc.user_online[2]}")
            elif opcao_escolhida == 'vs':
                print(f"SEU SALDO É DE R${fc.user_online[2]}")
            elif opcao_escolhida == 'cb':
                nome = input("digite o nome de usuario do devedor: ")
                valor = input("Digite o valor da cobrança: ")
                fc.criar_boleto(nome, valor)
                print(fc.user_debt)
            elif opcao_escolhida == 'ex':
                fc.sair()
                usuario_logado = False
                print("LOGOUT REALIZADO COM SUCESSO! ATÉ LOGO!")
                break
            
            
            

