
u1 = "leo"
u2 = "lucas"
u3 = "bruno"
u4 = "gustavo"
u5 = "iza"
snha1 = "1234"

x = 0
log =False
cont =False
cont1=False
cont2=False
cont3=False
cont4=False
cont5=False


def cdPdt():
    produto = input("Digite o nome do produto:\n")
    valor = input("Digite o valor de venda:\n")
    codigo = input("Digite o código do produto:\n")
    print("\n-----------------------------------------------------------------------------")
    print("Produto cadastrado com sucesso!")
    print("-----------------------------------------------------------------------------\n")
def pPdt():
    pesquisar = input("Digite o código do produto:")
    print("\n-----------------------------------------------------------------------------")
    print("Falha na conexão com o banco de dados, tente denovo mais tarde...")
    print("-----------------------------------------------------------------------------\n")

def cdClt():
    cltName=input("Digite o mome do cliente:\n ")
    cltPhone=input("Digite o numero de telefone do cliente:\n")
    cltCPF=input("Digite o CPF do cliente:\n")
    print("\n-----------------------------------------------------------------------------")
    print("Cliente cadastrado com sucesso!")
    print("-----------------------------------------------------------------------------\n")
def pClt():
    cpf=input("Digite o CPF do cliente:\n ")
    print("\n-----------------------------------------------------------------------------")
    print("Falha na conexão com o banco de dados, tente denovo mais tarde...")
    print("-----------------------------------------------------------------------------\n")

def cdFncd():
    fncd=input("Digite o mome do fornecedor:\n ")
    cltPhone=input("Digite o numero de telefone do forncedor:\n")
    cltCPF=input("Digite o CNPJ do fornecedor:\n")
    print("\n-----------------------------------------------------------------------------")
    print("Fornecedor cadastrado com sucesso!")
    print("-----------------------------------------------------------------------------\n")

def pFncd():
    cnpj=input("Digite o CNPJ do fornecedor:\n ")
    print("\n-----------------------------------------------------------------------------")
    print("Falha na conexão com o banco de dados, tente denovo mais tarde...")
    print("-----------------------------------------------------------------------------\n")

acesso = input("Bem vindo á LCBL!\n----------------------------------------------------------------------------- \nDigite o número da opção com a qual você deseja acessar:\n 1- Administrador\n 2- Cliente\n")

if (acesso == "1"):
   while (x < 4 and log != True):
    log = input("Digite o nome de Usuário: \n")

    x = x+1
    if log == u1 or log == u2 or log == u3 or log == u4 or log == u5:
        print("\n")

        print("Olá", log, "!\n")
        log = True

        snha = input("Digite sua senha:")

        if (snha != snha1):
            print("Senha Invalida!")
        else:
            print("\n-----------------------------------------------------------------------------")
            print("Você está logado como administrador!")
            print("-----------------------------------------------------------------------------\n")

            opcaoAdmin = input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Pesquisa de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Cadastro de fornecedores\n 6- Informações do fornecedor\n ")
            if opcaoAdmin == "1":
                while cont != 'n':
                    cdPdt()
                    cont = input("Deseja cadastrar mais algum produto? (s/n)\n")
                opcaoAdmin = input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Pesquisa de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Cadastro de fornecedores\n 6- Informações do fornecedor\n ")
                                   
            if opcaoAdmin == "2":
                while cont1 != 'n':
                    pPdt()
                    cont1 = input("Deseja pesquisar mais algum produto? (s/n)\n")
                opcaoAdmin = input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Pesquisa de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Cadastro de fornecedores\n 6- Informações do fornecedor\n ")
                   
            if opcaoAdmin == "3":
                while cont2 != 'n':
                    cdClt()
                    cont2 = input("Deseja cadastrar mais algum cliente? (s/n)\n")
                opcaoAdmin = input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Pesquisa de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Cadastro de fornecedores\n 6- Informações do fornecedor\n ")

            if opcaoAdmin == "4":
                while cont3 != 'n':
                    pClt()
                    cont3 = input("Deseja buscar as informaçoes de agum outro cliente? (s/n)")
                opcaoAdmin = input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Pesquisa de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Cadastro de fornecedores\n 6- Informações do fornecedor\n ")
   
            if opcaoAdmin == "5":
                while cont4 != 'n':
                    cdFncd()
                    cont4 = input("Deseja buscar as informaçoes de agum outro cliente? (s/n)")
                opcaoAdmin = input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Pesquisa de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Cadastro de fornecedores\n 6- Informações do fornecedor\n ")
   
            if opcaoAdmin == "6":
                while cont5 != 'n':
                    pFncd()
                    cont5 = input("Deseja buscar as informaçoes de agum outro cliente? (s/n)")
                opcaoAdmin = input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Pesquisa de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Cadastro de fornecedores\n 6- Informações do fornecedor\n ")
   
    else:
        print("Usuário invalido! você tem mais ", 4-x ,"tentativas:") 
