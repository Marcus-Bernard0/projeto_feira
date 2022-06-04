import time

#implementar códigos
#preços dos produtos
#troco para o cliente


print("Bem vindo a feirinha casa de minas.")
time.sleep(2)
print("Temos os seguintes produtos)")
print("\n")

def usuario(user):
    print(f"Ola {user}. Bem vindo,escolha seus produtos:")
    
def produtos():
    print("Temos os seguintes produtos:")
    time.sleep(4)
    print("Pães, Bolacha Negresco, Macarrão, Feijão")


def jogo():

    usuario(input("Qual o seu nome: "))
    
    produtos()


if (__name__== "__main__"):
    jogo()








