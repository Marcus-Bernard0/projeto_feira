import time


#implementar códigos
#preços dos produtos
#troco para o cliente

print("#######################################")
print("Bem vindo a feirinha Casa de Minas.")
print("#######################################")
time.sleep(2)
print("\n")

def usuario(user):
    print(f"Ola, {user.title()}. Bem vindo,escolha seus produtos:")
    
def produtos():
    print("Temos os seguintes produtos:")
    time.sleep(4)
    print("Paes, Bolacha Negresco, Macarrão, Feijao")
   

def codigos(Paes, Bolacha_Negresco, Macarrao, Feijao):
    print(f"Para escolher digite o código do produto Paes ({Paes} Bolacha ({Bolacha_Negresco}) Macarrao ({Macarrao}) Feijao ({Feijao})")
codigos(Paes = 22, Bolacha_Negresco= 23, Macarrao= 24, Feijao=25)




def jogo():

    usuario(input("Qual o seu nome: "))
    
    time.sleep(2)
    produtos()

    time.sleep(2)
    def precos(Paes, Bolacha_Negresco, Macarrao, Feijao):
        print(f"Com os respetivos preços. Paes= {Paes}, Bolacha negresco = {Bolacha_Negresco}, Macarrao = {Macarrao}, Feijão = {Feijao}")
    precos(Paes = 1.0,  Bolacha_Negresco = 2.50, Macarrao = 1.50, Feijao = 6.10)   

    print('\n')
    time.sleep(3)

    def codigos(Paes, Bolacha_Negresco, Macarrao, Feijao):
        print(f"Para escolher digite o código do produto Paes ({Paes}) Bolacha ({Bolacha_Negresco}) Macarrao ({Macarrao}) Feijao ({Feijao})")
        
        carrinho = []
        while True:
            escolha_produto = input("Escolha seu produto: ")
            carrinho.append(escolha_produto)
            comprar_mais = int(input("Se quiser comprar mais, digite o código produto, se não, digite 0 : "))
            if comprar_mais == 0 :
                break
        print(carrinho)

    codigos(Paes = 22, Bolacha_Negresco= 23, Macarrao= 24, Feijao=25)
            
        
    
        

        
    

if (__name__== "__main__"):
    jogo()








