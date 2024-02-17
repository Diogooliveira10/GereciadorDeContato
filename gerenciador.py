def adicionar_contato(contatos, nome_contato):
    contato = {"nome": nome_contato, "completada": False}

    contatos.append(contato)
    print(f"Contato {nome_contato} foi adicionada com sucesso!")
    return

def adicionar_telefone(telefones, numero_telefone):
    telefone = {"telefone": numero_telefone, "completada": False}

    telefones.append(telefone)
    print(f"Telefone {numero_telefone} foi adicionada com sucesso!")
    return

def adicionar_email(emails, nome_email):    
    email = {"email": nome_email, "completada": False}

    emails.append(email)
    print(f"E-mail {nome_email} foi adicionada com sucesso!")
    return


def ver_contatos(contatos):
    print("\nLista de nome dos contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["completada"] else " "

        nome_contato = contato["nome"]
        print(f"{indice}. [{status}] {nome_contato}")
        return

def ver_telefones(telefones):
    print("\nLista de telefones:")
    for indice, telefone in enumerate(telefones, start=1):
        status = "✓" if telefone["completada"] else " "
    
        numero_telefone = telefone["telefone"]
        print(f"{indice}. [{status}] {numero_telefone}")
        return

def ver_emails(emails):
    print("\nLista de e-mails:")
    for indice, email in enumerate(emails, start=1):
        status = "✓" if email["completada"] else " "
    
        nome_email = email["email"]
        print(f"{indice}. [{status}] {nome_email}")
        return

def atualizar_nome_contatos(contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
        print(f"Contato {indice_contato} atualizado para {novo_nome_contato}.")
    else:
        print("Índice de contato inválido!")
    return

def atualizar_numero_telefones(telefones, indice_telefone, novo_numero_telefone):
    indice_telefone_ajustado = int(indice_telefone) - 1
    if indice_telefone_ajustado >= 0 and indice_telefone_ajustado < len(telefones):
        telefones[indice_telefone_ajustado]["telefone"] = novo_numero_telefone
        print(f"Número {indice_telefone} atualizado para {novo_numero_telefone}.")
    else:
        print("Índice de número inválido!")
    return

def atualizar_emails(emails, indice_email, novo_email):
    indice_email_ajustado = int(indice_email) - 1
    if indice_email_ajustado >= 0 and indice_email_ajustado < len(emails):
        emails[indice_email_ajustado]["email"] = novo_email
        print(f"E-mail {indice_email} atualizado para {novo_email}")
    else:
        print("Índice de e-mail inválido!")
    return

def marcar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    contatos[indice_contato_ajustado]["completada"] = True
    print(f"Contato {indice_contato} marcado como favorito!")
    return

def marcar_telefone(telefones, indice_telefone):
    indice_telefone_ajustado = int(indice_telefone) - 1
    telefones[indice_telefone_ajustado]["completada"] = True
    print(f"Telefone {indice_contato} marcado como favorito!")
    return

def marcar_email(emails, indice_email):
    indice_email_ajustado = int(indice_email) - 1
    emails[indice_email_ajustado]["completada"] = True
    print(f"E-mail {indice_email} marcado como favorito!")
    return

contatos = []
telefones = []
emails = []

while True:
    print("\nMenu do Gerenciador de Contato:")
    print("1. Adicionar contatos.")
    print("2. Ver lista de contatos cadastrados.")
    print("3. Atualizar contatos.")
    print("4. Marcar/Desmarcar contatos favoritos.")
    print("5. Deletar contato.")
    print("6. Sair.")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        adicionar_contato(contatos, nome_contato)
        numero_telefone = int(input("Digite o número do telefone que deseja adicionar: "))
        adicionar_telefone(telefones, numero_telefone)
        nome_email = input("Digite o e-mail que deseja adicionar: ")
        adicionar_email(emails, nome_email)

    elif escolha == "2":
        ver_contatos(contatos)
        ver_telefones(telefones)
        ver_emails(emails)

    elif escolha == "3":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        atualizar_nome_contatos(contatos, indice_contato, novo_nome)

        ver_telefones(telefones)
        indice_telefone = input("Digite o número do telefone que deseja atualizar: ")
        novo_numero = input("Digite o novo número do telefone: ")
        atualizar_numero_telefones(telefones, indice_telefone, novo_numero)

        ver_emails(emails)
        indice_email = input("Digite o número do e-mail que deseja atualizar: ")
        novo_email = input("Digite o novo e-mail: ")
        atualizar_emails(emails, indice_email, novo_email)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja marcar como favorito: ")
        marcar_contato(contatos, indice_contato)

        ver_telefones(telefones)
        indice_telefone = input("Digite o número do telefone que deseja marcar como favorito: ")
        marcar_telefone(telefones, indice_telefone)

        ver_emails(emails)
        indice_email = input("Digite o número do e-mail que deseja marcar como favorito: ")
        marcar_email(emails, indice_email)

    elif escolha == "6":
        break

print("Programa finalizado!")