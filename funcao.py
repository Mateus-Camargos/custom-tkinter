def validar_login(usuario, senha, label_resultado):
    # Exemplo simples de validação
    if usuario == "Mateus" and senha == "05032011":
        label_resultado.configure(text="Login bem-sucedido!", text_color="green")
    else:
        label_resultado.configure(text="Usuário ou senha incorretos.", text_color="red")
