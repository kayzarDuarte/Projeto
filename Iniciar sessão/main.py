import time
import bcrypt
import sqlite3
import re

conexao = sqlite3.connect("utilizadores.db")
cursor = conexao.cursor()

cursor.execute( """
CREATE TABLE IF NOT EXISTS usuarios (
    usuario TEXT UNIQUE NOT NULL,
    hash_senha TEXT NOT NULL
)
"""
)



conexao.commit()

def validar_senha(senha):
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return False
    if not re.search(r"[A-Z]", senha):
        print("A senha deve conter pelo menos uma letra maiúscula.")
        return False
    if not re.search(r"[a-z]", senha):
        print("A senha deve conter pelo menos uma letra minúscula.")
        return False
    if not re.search(r"[0-9]", senha):
        print("A senha deve conter pelo menos um número.")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        print("A senha deve conter pelo menos um caractere especial.")
        return False
    return True



def iniciar_sessao ():


    cadastrar = input("Bem-Vindo ao nosso programa! Já possui conta? ")
    
    if cadastrar == "Nao" or cadastrar == "nao":
        print(str("Muito Bem! Vamos então passar à criação da sua nova conta no nosso sistema!!"))
        nome_usuario = input("Introduza o seu nome de utilizador. ")
        senha_usuario = input("Introduza a sua senha. ")

        if validar_senha(senha_usuario):
            cadastrar_usuario(nome_usuario, senha_usuario)
        else:
            print("Não atendeste aos requisitos da criação de uma palavra pass!")
    else:
        cadastro_feito()


def cadastrar_usuario(nome, senha):
    hash_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO usuarios (usuario, hash_senha) VALUES (?, ?)",(nome, hash_senha.decode('utf-8')))
        conexao.commit()
        print (f"{nome} Bem-Vindo ao nosso programa!")
    except sqlite3.IntegrityError:
        print(f"Erro: O seu nome já existe!")



def cadastro_feito():
    Max_tentativas = 3
    tempo_bloqueio = 1
    block = 0
    tentativas = 0 

    while tentativas < Max_tentativas:
        usuario = input("Por favor introduza o seu nome de utilizador: ")
        senha = input("Por favor introduza a sua palavra pass: ").encode('utf-8')

        cursor.execute("SELECT hash_senha FROM usuarios WHERE usuario = ?", (usuario,))
        resultado = cursor.fetchone()

        if resultado:  
            hash_senha = resultado[0]

            if bcrypt.checkpw(senha, hash_senha.encode('utf-8')):
                print(f"Os dados introduzidos estão corretos! Bem-vindo, {usuario}!")
                return  
            else:
                print("A senha introduzida está incorreta!")
        else:
            print("Usuário que introduziu não foi encontrado no nosso sistema.")

        tentativas += 1
        if tentativas < Max_tentativas:
            print(f"Você tem {Max_tentativas - tentativas} tentativas restantes.")
        else:
            block += 1
            tempo_atual_bloqueios = tempo_bloqueio * block
            print(f"Excedeu o máximo de tentativas! O seu acesso foi bloqueado por {tempo_atual_bloqueios} segundo(s).")
            time.sleep(tempo_atual_bloqueios)  
            tentativas = 0  


iniciar_sessao()    


conexao.close()