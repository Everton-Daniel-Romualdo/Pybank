#Arquivos com as funções para manipular e processar informações e pedidos
user_info = [] #Banco de dados dos usuarios 
user_online = []#dados do usuario logado - nome,senha,saldo,divida


def adm():
    print(f"User info: {user_info}")
    print(f"User_online {user_online}")



def atualizar(): #Sincroniza o user_online com a lista principal user_info
    for i in range(len(user_info)):
        if user_online[0] == user_info[i]:
            user_info[i + 1] = user_online[1]
            user_info[i+2] = user_online[2]
            user_info[i+3] = user_info[3]



def cadastrar(nome, senha):#Cadastra o usuario      
    if nome in user_info:
        return False
    else:
        user_info.append(nome)
        user_info.append(senha)
        user_info.append(0)
        user_info.append(False)
        return True
    


def logar(nome, senha):#Faz login com o usuario
    for i in range(len(user_info)):
        if user_info[i] == nome and user_info[i+1] == senha:
            user_online.append(user_info[i])
            user_online.append(user_info[i+1])
            user_online.append(user_info[i+2])
            user_online.append(user_info[i+3])
            return True
        else:
            return False
        


def sair():
    user_online = []



def depositar(valor):
    user_online[2] += int(valor)
    atualizar()

    

def sacar(valor):
    if int(valor) > user_online[2]:
       return False
    else:
        user_online[2] -= int(valor)
        atualizar()
        return True
