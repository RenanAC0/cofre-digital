import random
import time

def mostra_senha(indice, digitos):
    if indice == 0:
        return '__'
    elif indice == 1:
        return f'{digitos[0]}_'
    elif indice == 2:
        return f'{digitos[0]}{digitos[1]}__'
    elif indice == 3:
        return f'{digitos[0]}{digitos[1]}{digitos[2]}_'
    else:
        return f'{digitos[0]}{digitos[1]}{digitos[2]}{digitos[3]}'

def jogar():
   
    digitos = str(random.randint(0, 9999)).zfill(4)

    print("\n🔒 Cofre Digital")
    print("Tente descobrir a senha de 4 dígitos!")
    print("------")

    tentativas = 0
    inicio = time.time()

    i = 0
    while i < 4:
        print(f"\n{mostra_senha(i, digitos)}")
        print()

        while True:
            chute = int(input(f"Digite o {i+1}º dígito (0-9): "))
            tentativas += 1
            correto = int(digitos[i])

            if chute == correto:
                print("✅ Dígito correto!")
                i += 1
                break
            elif chute < correto:
                print("O dígito correto é MAIOR.")
            else:
                print("O dígito correto é MENOR.")

    tempo_total = time.time() - inicio

    print(f"\n{mostra_senha(4, digitos)}")
    print("\n🔓 Cofre aberto com sucesso!")
    print(f"Senha: {digitos}")
    print(f"Tentativas: {tentativas}")
    print(f"Tempo: {tempo_total:.2f} segundos")

    return True

while True:
    jogar()
    print()
    resposta = input("Deseja jogar novamente? (s/n): ")
    if resposta != 's':
        print("Obrigado por jogar! Até a próxima.")
        break