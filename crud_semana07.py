def mostrar_menu_principal():
    print("Bem vindo ao Menu")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")

    return int(input("Digite uma opção válida: "))

def mostrar_menu_secundario():
    print(f"Menu de operações - Opção  {opcao}")
    print("1. Incluir")
    print("2. Listar")
    print("3. Excluir")
    print("4. Editar")
    print("5. Voltar")

    return int(input("Digite uma opção válida: "))

def incluir_estudantes():
    lista_estudantes = []
    for i in range(3):
        codigo = int(input("Qual o código do estudante: "))
        nome = (input("Qual o nome do estudante: "))
        cpf = int(input("Qual o CPF do estudante: "))

        dados_estudante = {
            "codigo": codigo,
            "nome": nome,
            "cpf": cpf
        }

        lista_estudantes.append(dados_estudante)

        return lista_estudantes

def mostrar_estudantes():
    print(lista_estudantes)

def remover_estudantes():
    codigo_para_excluir = int(input("Qual código deseja excluir?"))

    estudante_para_ser_removido = None
    for dicionario_estudante in lista_estudantes:
        if dicionario_estudante["codigo"] == codigo_para_excluir:
            estudante_para_ser_removido = dicionario_estudante
            break

    if estudante_para_ser_removido is None:
        print(f"Não encontramos o estudante de código {codigo_para_excluir} na lista")
    else:
        lista_estudantes.remove(estudante_para_ser_removido)

    print(lista_estudantes)

def editar_estudantes():
    codigo_para_editar = int(input("Qual código deseja editar?"))

    estudante_para_ser_modificado = None
    for dicionario_estudante in lista_estudantes:
        if dicionario_estudante["codigo"] == codigo_para_editar:
            estudante_para_ser_modificado = dicionario_estudante
            break

    if estudante_para_ser_modificado is None:
        print(f"Não encontramos o estudante de código {codigo_para_editar} na lista")
    else:
        estudante_para_ser_modificado["codigo"] = int(input("Digite o novo código"))
        estudante_para_ser_modificado["nome"] = input("Digite o novo nome")
        estudante_para_ser_modificado["cpf"] = input("Digite o novo cpf")

    print(lista_estudantes)

while True:
    opcao = mostrar_menu_principal()
    if opcao == 1:

       while True:
            print(f"Você escolheu a opção VÁLIDA {opcao}")

            # Coletar a opção do menu Secundário
            opcao_secundaria = mostrar_menu_secundario()

            print(f"Você escolheu a opção secundária {opcao_secundaria}")
            if opcao_secundaria == 1 :
                print(f"Você escolheu a opção INCLUIR  {opcao}")
                lista_estudantes = incluir_estudantes()

            elif opcao_secundaria == 2:
                mostrar_estudantes()

            elif opcao_secundaria == 3:
                remover_estudantes()

            elif opcao_secundaria == 4:
                editar_estudantes()

            elif opcao_secundaria == 5:
                break
            else:
                print("Você digitou uma opção secundária inválida")

    elif opcao == 2 and opcao == 3 and opcao == 4 and opcao == 5:
        print("EM DESENVOLVIMENTO")

    elif opcao == 0:
        print("Você Você pediu para sair")
        break

    else:
        print("Você digitou uma opção inválida")