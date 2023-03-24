
u1="leo"  
u2="lucas"
u3="bruno"
u4="gustavo"
u5="iza"
snha1="1234"

i=0
def pdt1():
    produto=input("Digite o nome do produto:")
    valor=input("Digite o valor de venda:")
    codigo=input("Digite o código do produto:")
    
acesso=input("Bem vindo á LCBL!\n----------------------------------------------------------------------------- \nDigite o número da opção com a qual você deseja acessar:\n 1- Administrador\n 2- Cliente\n")

if(acesso == "1" ):
  log=input("Digite o nome de Usuário: \n")
  
  if log == u1 or log == u2 or log == u3 or log == u4 or log == u5:
         
         print("Olá", log,"!")
         snha=input("Digite sua senha:")
         if(snha != snha1):
           print("Senha Invalida!")  
         else:  
          opcaoAdmin=input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Pesquisa de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Cadastro de fornecedores\n 6- Informações do fornecedor\n ")
          if opcaoAdmin == "1":
             pdt1()
             cont=input("Deseja adicionar mais algum produto? (s/n)")
             if cont == "s":
                pdt1()
             else:
                 opcaoAdmin=input("Digite o número da função desejada:\n 1- Cadastro de produto\n 2- Pesquisa de produto\n 3- Cadastro de cliente\n 4- Informaçoes do cliente\n 5- Cadastro de fornecedores\n 6- Informações do fornecedor\n ")              
             if opcaoAdmin == "2":
                cdg=input("Digite o código do produto:")
             if cdg == "1":
               print(pdt1())