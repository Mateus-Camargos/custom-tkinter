import customtkinter as ctk

ctk.set_appearance_mode('dark')
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x300")

label_usuario = ctk.CTkLabel(app, text="Usuário")
label_usuario.pack(pady=10)

entry_usuario = ctk.CTkEntry(app, placeholder_text="Digite seu usuário: ")
entry_usuario.pack(pady=10)

label_senha = ctk.CTkLabel(app, text="Senha")
label_senha.pack(pady=10)

entry_senha = ctk.CTkEntry(app, placeholder_text="Digite sua senha: ")
entry_senha.pack(pady=10)

botao = ctk.CTkButton(app, text="Confirmar")
botao.pack(pady=10)

app.mainloop()