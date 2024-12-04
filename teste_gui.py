import customtkinter as ctk
from tkinter import messagebox

# Configurações iniciais do customtkinter
ctk.set_appearance_mode("System")  # Alternativa: "Dark" ou "Light"
ctk.set_default_color_theme("blue")  # Alternativa: "dark-blue" ou "green"

# Função para exibir a janela de login
def abrir_login():
    limpar_janela()
    ctk.CTkLabel(root, text="Login", font=("Arial", 20)).pack(pady=20)

    ctk.CTkLabel(root, text="Usuário:").pack(pady=5)
    entry_usuario = ctk.CTkEntry(root, placeholder_text="Digite seu usuário")
    entry_usuario.pack(pady=5)

    ctk.CTkLabel(root, text="Senha:").pack(pady=5)
    entry_senha = ctk.CTkEntry(root, placeholder_text="Digite sua senha", show="*")
    entry_senha.pack(pady=5)

    ctk.CTkButton(root, text="Entrar", command=lambda: fazer_login(entry_usuario.get(), entry_senha.get())).pack(pady=10)
    ctk.CTkButton(root, text="Voltar", command=mostrar_pergunta).pack(pady=5)

# Função para exibir a janela de registro
def abrir_registro():
    limpar_janela()
    ctk.CTkLabel(root, text="Registrar", font=("Arial", 20)).pack(pady=20)

    ctk.CTkLabel(root, text="Novo Usuário:").pack(pady=5)
    entry_usuario = ctk.CTkEntry(root, placeholder_text="Digite um nome de usuário")
    entry_usuario.pack(pady=5)

    ctk.CTkLabel(root, text="Nova Senha:").pack(pady=5)
    entry_senha = ctk.CTkEntry(root, placeholder_text="Digite uma senha forte", show="*")
    entry_senha.pack(pady=5)

    ctk.CTkButton(root, text="Registrar", command=lambda: fazer_registro(entry_usuario.get(), entry_senha.get())).pack(pady=10)
    ctk.CTkButton(root, text="Voltar", command=mostrar_pergunta).pack(pady=5)

# Função para validar o login (simples para demonstração)
def fazer_login(usuario, senha):
    if usuario == "admin" and senha == "admin123":
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")

# Função para processar o registro (simples para demonstração)
def fazer_registro(usuario, senha):
    if usuario and senha:
        messagebox.showinfo("Sucesso", f"Usuário {usuario} registrado com sucesso!")
        abrir_login()  # Redirecionar para o login após registro
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

# Função para exibir a pergunta inicial
def mostrar_pergunta():
    limpar_janela()
    ctk.CTkLabel(root, text="Você já tem uma conta?", font=("Arial", 20)).pack(pady=20)
    ctk.CTkButton(root, text="Sim", command=abrir_login).pack(pady=10)
    ctk.CTkButton(root, text="Não", command=abrir_registro).pack(pady=10)

# Função para limpar todos os widgets da janela
def limpar_janela():
    for widget in root.winfo_children():
        widget.destroy()

# Configuração da janela principal
root = ctk.CTk()
root.title("Sistema de Login e Registro")
root.geometry("500x400")

# Exibir a pergunta inicial
mostrar_pergunta()

# Iniciar o loop principal
root.mainloop()
