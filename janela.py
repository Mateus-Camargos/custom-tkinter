import customtkinter as ctk
from funcao import validar_login

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x300")

# Campo de Usuário
label_usuario = ctk.CTkLabel(app, text="Usuário")
label_usuario.pack(pady=10)

entry_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário: ")
entry_usuario.pack(pady=10)

# Campo de Senha
label_senha = ctk.CTkLabel(app, text="Senha")
label_senha.pack(pady=10)

entry_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha: ", show="*")
entry_senha.pack(pady=10)

resultado = ctk.CTkLabel(app, text="")
resultado.pack(pady=10)

botao = ctk.CTkButton(
    app, 
    text="Confirmar", 
    command=lambda: validar_login(entry_usuario.get(), entry_senha.get(), resultado)
)
botao.pack(pady=10)

app.mainloop()

