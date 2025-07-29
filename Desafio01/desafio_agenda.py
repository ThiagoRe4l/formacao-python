def add_contact(agenda, name, number, email):
    contact = {
        "Nome do contato": name, 
        "Telefone do contato": number, 
        "Email": email, 
        "favorito": False
    }
    agenda.append(contact)
    print(f"Contato {name} foi adicionado com sucesso!\nTelefone: {number}\nemail: {email}")
    return

def see_contact(agenda):
    print("\nLista de contatos:")
    for index, contact in enumerate(agenda, start=1):
        status = "✓" if contact["favorito"] else " "
        name = contact["Nome do contato"]
        print(f"{index}. [{status}] {name}")
    return

def edit_contact(agenda, index_contact, new_name, new_number, new_email):
    new_contact_index = int(index_contact) -1
    if new_contact_index >= 0 and new_contact_index < len(agenda):
        agenda[new_contact_index]["Nome do contato"] = new_name
        agenda[new_contact_index]["Telefone do contato"] = new_number
        agenda[new_contact_index]["Email"] = new_email
        print(f"Contato atualizado para as seguintes informações:\nNome: {new_name}\nTelefone: {new_number}\nEmail: {new_email}")
    else:
        print("Índice de contato inválido.")
    return

def favorite_contact(agenda, index_contact):
    new_contact_index = int(index_contact) - 1
    agenda[new_contact_index]["favorito"] = True
    print(f"Contato {index_contact} marcado como favorito")
    return

def favorite_list(agenda):
    print("\nLista de contatos favoritos:")
    favorite = False
    for index, contact in enumerate(agenda, start=1):
        if contact.get("favorito"):
            favorite = True
            print(f"{index}. [✓] {contact['Nome do contato']}")
    if not favorite:
        print("Nenhum contato marcado como favorito.")

def delete_contact(agenda, index_contact):
    index = int(index_contact) - 1
    contact_remove = agenda.pop(index)
    print(f"Contato '{contact_remove['Nome do contato']}' removido com sucesso.")


agenda = []
while True:
    print("\nMenu do gerenciador de Agenda:")
    print("1. Adicionar contato")
    print("2. Ver lista de contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar contato favorito")
    print("5. Ver contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        name = input("Digite o nome do contato que deseja adicionar: ")
        number = input("Digite o telefone do contato que deseja adicionar: ")
        email = input("Digite o email do contato que deseja adicionar: ")
        add_contact(agenda, name, number, email)

    elif escolha == "2":
        see_contact(agenda)

    elif escolha == "3":
        see_contact(agenda)
        index_contact = input("Digite o número do contato que deseja atualizar: ")
        new_name = input("Digite o novo nome do contato: ")
        new_number = input("Digite o novo telefone do contato: ")
        new_email = input("Digite o novo email do contato: ")
        edit_contact(agenda, index_contact, new_name, new_number, new_email)

    elif escolha == "4":
        see_contact(agenda)
        index_contact = input("Digite o número do contato que deseja favoritar: ")
        favorite_contact(agenda, index_contact)

    elif escolha == "5":
        favorite_list(agenda)

    elif escolha == "6":
        see_contact(agenda)
        index_contact = input("Digite o número do contato que deseja deletar: ")
        delete_contact(agenda, index_contact)
        see_contact(agenda)

    elif escolha == "7":
        break

print("Programa finalizado.")