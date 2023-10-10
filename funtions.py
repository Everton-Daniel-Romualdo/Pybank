#Arquivos com as funções para manipular e processar informações e pedidos
user_info = []
user_online = []#nome,senha,saldo,divida


def adm():
    print(f"User info: {user_info}")
    print(f"User_online {user_online}")

def menu_Inicial():#Emprimi o menu principal na tela
    print("Bem vindo")
    print("Cadastrar Usuario [c]")
    print("Fazer Login [l]")

def menu_principal():
    print("Depositar [d]")
    print("Sacar [s]")
    print("Ver Saldo [vs]")

def atualizar(): #Sincroniza o user_online com a lista principal user_info
    for i in range(len(user_info)):
        if user_online[0] == user_info[i]:
            user_info[i + 1] = user_online[1]
            user_info[i+2] = user_online[2]
            user_info[i+3] = user_info[3]

def cadastrar():#Cadastra o usuario      
    nome = input("Digite seu nome: ")
    senha = input("Digite a sua senha")

    if nome in user_info:
        print("Nome de usuario ja existente")
        return None
    else:
        user_info.append(nome)
        user_info.append(senha)
        user_info.append(0)
        user_info.append(False)
        print("USUARIO CADASTRADO COM SUCESSO!")

def logar():#Faz login com o usuario
    nome = input("Digite seu nome de usuario")
    senha = input("Digite sua senha")

    for i in range(len(user_info)):
        if user_info[i] == nome and user_info[i+1] == senha:
            user_online.append(user_info[i])
            user_online.append(user_info[i+1])
            user_online.append(user_info[i+2])
            user_online.append(user_info[i+3])
            print(f"USUARIO LOGADO COM SUCESSO! BEM VINDO {user_online[0]}!")
            return True
        else:
            print('NOME DE USUARIO OU SENHA INVALIDOS!')
            return False

def depositar():
    valor = input("Qual o valor do deposito?")
    user_online[2] += int(valor)
    atualizar()
    print("Deposito realizado com sucesso")

def sacar():
    valor = int(input("Qual o valor de saque"))

    if valor > user_online[2]:
        print("SALDO INSUFICIENTE")
    else:
        user_online[2] -= valor
        atualizar()
        print("VALOR SACADO COM SUCESSO!")

def ver_saldo():
    print(f" SEU SALDO É DE: R${user_online[2]}")