import os 
os.system("cls")

print("")

tentativas = 0
login_salvo = "Marta"
senha_salva = "123"

for i in range(3): 
    while True:
        print (f"\ntentativa: {tentativas+1}")
        login = input("Digte seu login: ")
        senha = input("Digite sua senha: ")

        if login == login_salvo and senha == senha_salva: 
            print("Bem vindo!")
            break 
        else: 
            print("Login ou semha inválidos ")
            tentativas += 1