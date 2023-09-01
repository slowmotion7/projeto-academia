def apresentacao_academia():
    print()
    print("Bem-vindo à Academia Rogerinho!")
    print("Nossa academia é o lugar ideal para você alcançar seus objetivos de condicionamento físico e bem-estar.")
    print("Em nossa academia, você encontrará equipamentos modernos, salas de treinamento especializadas e uma equipe dedicada.")
    print("Junte-se a nós na Academia Rogerinho e comece sua jornada para uma vida mais saudável e ativa!")
    print()

# Chamada da função para exibir a introdução da academia
apresentacao_academia()

import re

def validar_cpf(cpf):
    entrada = re.findall("\d", cpf)  # remover caracteres NÃO numéricos

    # validar quantidade de caracteres digitados
    if len(cpf) > 14 or len(entrada) < 11 or len(entrada) > 11:
        print('CPF INVÁLIDO')
        return False

    # verificar se todos os dígitos são iguais
    valid = 0
    for dig in range(0, 11):
        valid += int(entrada[dig])
        dig += 1
    if int(entrada[0]) == valid / 11:
        print("CPF INVÁLIDO")
        return False

    # rotina de cálculos do dígito verificador do CPF
    else:
        # verificação do 10º dígito verificador
        soma = 0
        count = 10
        for i in range(0, len(entrada) - 2):
            soma = soma + (int(entrada[i]) * count)
            i += 1
            count -= 1
        dg1 = 11 - (soma % 11)
        if dg1 >= 10:
            dg1 = 0

        # verificação do 11º dígito verificador
        soma = 0
        count = 10
        for j in range(1, len(entrada) - 1):
            soma = soma + (int(entrada[j]) * count)
            j += 1
            count -= 1
        dg2 = 11 - (soma % 11)
        if dg2 >= 10:
            dg2 = 0

        # mensagem ao usuário
        if int(entrada[9]) != dg1 or int(entrada[10]) != dg2:
            print("CPF INVÁLIDO")
            return False
        else:
            print('* CPF VÁLIDO *')
            return True

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o CPF do aluno: ")

    # Validação do CPF
    if not validar_cpf(cpf):
        return

    peso = float(input("Digite o peso do aluno (em kg): "))
    altura = float(input("Digite a altura do aluno (em metros): "))
    status = False  # O status é definido como False por padrão
    imc = peso / (altura ** 2)
    imc_ = "{:.2f}".format(imc)
    print("Seu IMC é: ", imc_)

    if imc < 16:
        print("Magreza grave")
    elif 16 <= imc < 17:
        print("Magreza moderada")
    elif 17 <= imc < 18.5:
        print("Magreza leve")
    elif 18.5 <= imc < 25:
        print("Saudável")
    elif 25 <= imc < 30:
        print("Sobrepeso")
    elif 30 <= imc < 35:
        print("Obesidade Grau I")
    elif 35 <= imc < 40:
        print("Obesidade Grau II (severa)")
    else:
        print("Obesidade Grau III (mórbida)")

    print("\n--- Planos de Academia ---")
    print("1 - Plano Básico (3 dias na semana)")
    print("2 - Plano Regular (5 dias na semana)")
    print("3 - Plano Premium (7 dias na semana)")
    plano = int(input("Selecione o plano do aluno: "))

    valor_plano = 0.0
    if plano == 1:
        valor_plano = 100.0
        plano_descricao = "Plano Básico"
    elif plano == 2:
        valor_plano = 175.0
        plano_descricao = "Plano Regular"
    elif plano == 3:
        valor_plano = 500.0
        plano_descricao = "Plano Premium"
    else:
        print("Plano inválido. O aluno será cadastrado sem plano definido.")
        plano_descricao = "Sem plano"

    aluno = {
        "Nome": nome,
        "CPF": cpf,
        "Peso": peso,
        "Altura": altura,
        "IMC": imc_,
        "Status": status,
        "Plano": plano_descricao,
        "Valor Plano": valor_plano
    }
    alunos.append(aluno)
    treinos.append([])  # Adiciona uma linha vazia para o treino do aluno

    print("\nAluno cadastrado com sucesso!")
    print("Dados do aluno:")
    print("Nome:", aluno["Nome"])
    print("CPF:", aluno["CPF"])
    print("Peso:", aluno["Peso"])
    print("Altura:", aluno["Altura"])
    print("imc_:", aluno["IMC"])
    print("Status:", aluno["Status"])
    print("Plano:", aluno["Plano"])
    print("Valor do Plano: R$", aluno["Valor Plano"], "\n")


def buscar_aluno():
    nome = input("Digite o nome do aluno: ")
    encontrado = False

    for aluno in alunos:
        if aluno["Nome"].lower() == nome.lower():
            encontrado = True
            print("\nDados do aluno:")
            print(f"Nome: {aluno['Nome']}")
            print(f"CPF: {aluno['CPF']}")
            print(f"Peso: {aluno['Peso']}")
            print(f"Altura: {aluno['Altura']}")
            print(f"imc_: {aluno['IMC']}")

            index = alunos.index(aluno)
            treino = treinos[index]

            if len(treino) > 0:
                print("\nTreino:")
                for exercicio in treino:
                    print(f"Exercício: {exercicio['Nome']}")
                    print(f"Número de repetições: {exercicio['Repeticoes']}")
                    print(f"Peso: {exercicio['Peso']}")
            else:
                print("\nO aluno não possui exercícios no treino.")

            break

    if not encontrado:
        print("Aluno não encontrado.")

def gerenciar_treino():
    nome = input("Digite o nome do aluno: ")
    encontrado = False

    for aluno in alunos:
        if aluno["Nome"].lower() == nome.lower():
            encontrado = True
            index = alunos.index(aluno)
            treino = treinos[index]

            while True:
                print("\n--- Menu de Gerenciamento de Treino ---")
                print("1 - Incluir exercício")
                print("2 - Alterar exercício")
                print("3 - Excluir exercício")
                print("4 - Excluir todos os exercícios")
                print("0 - Voltar ao menu principal")

                opcao = input("\nDigite a opção desejada: ")

                if opcao == "1":
                    if len(treino) < 10:
                        exercicio = {}
                        exercicio["Nome"] = input("Digite o nome do exercício: ")
                        exercicio["Repeticoes"] = int(input("Digite o número de repetições: "))
                        exercicio["Peso"] = float(input("Digite o peso utilizado (em kg): "))

                        if exercicio not in treino:
                            treino.append(exercicio)
                            aluno["Status"] = True
                            print("Exercício adicionado com sucesso!\n")
                        else:
                            print("O exercício já existe no treino.\n")
                    else:
                        print("O treino já atingiu o número máximo de exercícios.\n")

                elif opcao == "2":
                    nome_exercicio = input("Digite o nome do exercício a ser alterado: ")
                    encontrado_exercicio = False

                    for exercicio in treino:
                        if exercicio["Nome"].lower() == nome_exercicio.lower():
                            encontrado_exercicio = True
                            exercicio["Repeticoes"] = int(input("Digite o novo número de repetições: "))
                            exercicio["Peso"] = float(input("Digite o novo peso utilizado (em kg): "))
                            print("Exercício alterado com sucesso!\n")
                            break

                    if not encontrado_exercicio:
                        print("Exercício não encontrado.\n")

                elif opcao == "3":
                    nome_exercicio = input("Digite o nome do exercício a ser excluído: ")
                    encontrado_exercicio = False

                    for exercicio in treino:
                        if exercicio["Nome"].lower() == nome_exercicio.lower():
                            encontrado_exercicio = True
                            treino.remove(exercicio)
                            print("Exercício excluído com sucesso!\n")
                            break

                    if not encontrado_exercicio:
                        print("Exercício não encontrado.\n")

                elif opcao == "4":
                    treino.clear()
                    aluno["Status"] = False
                    print("Todos os exercícios foram excluídos do treino.\n")

                elif opcao == "0":
                    break

                else:
                    print("Opção inválida. Por favor, digite novamente.\n")

            break

    if not encontrado:
        print("Aluno não encontrado.")

def atualizar_cadastro():
    nome = input("Digite o nome do aluno: ")
    encontrado = False

    for aluno in alunos:
        if aluno["Nome"] == nome:
            encontrado = True

            print("\nDados atuais do aluno:")
            print(f"Nome: {aluno['Nome']}")
            print(f"CPF: {aluno['CPF']}")
            print(f"Peso: {aluno['Peso']}")
            print(f"Altura: {aluno['Altura']}")
            print(f"imc_: {aluno['IMC']}")
            print(f"Plano: {aluno['Plano']}")

            print("Deixe em branco caso não queira atualizar o campo.")

            novo_nome = input("Digite o novo nome do aluno: ")
            aluno["Nome"] = novo_nome if novo_nome != "" else aluno["Nome"]

            novo_cpf = input("Digite o novo CPF do aluno: ")
            if novo_cpf != "":
                if validar_cpf(novo_cpf):
                    aluno["CPF"] = novo_cpf
                    print("CPF atualizado com sucesso!\n")

            novo_peso = input("Digite o novo peso do aluno (em kg): ")
            if novo_peso != "":
                aluno["Peso"] = float(novo_peso)
                aluno["imc"] = "{:.2f}".format(aluno["Peso"] / (aluno["Altura"] ** 2))

            nova_altura = input("Digite a nova altura do aluno (em metros): ")
            if nova_altura != "":
                aluno["Altura"] = float(nova_altura)
                aluno["imc"] = "{:.2f}".format(aluno["Peso"] / (aluno["Altura"] ** 2))

            print("\n--- Planos de Academia ---")
            print("1 - Plano Básico (3 dias na semana)")
            print("2 - Plano Regular (5 dias na semana)")
            print("3 - Plano Premium (7 dias na semana)")
            novo_plano = input("Selecione o novo plano do aluno (Digite o número correspondente): ")

            if novo_plano == "1":
                aluno["Plano"] = 1
                aluno["Valor Plano"] = 100.0
            elif novo_plano == "2":
                aluno["Plano"] = 2
                aluno["Valor Plano"] = 175.0
            elif novo_plano == "3":
                aluno["Plano"] = 3
                aluno["Valor Plano"] = 500.0
            elif novo_plano != "":
                print("Plano inválido. O plano do aluno não foi alterado.")

            print("Cadastro atualizado com sucesso!\n")
            break

    if not encontrado:
        print("Aluno não encontrado.")


# Função para excluir um aluno
def excluir_aluno():
    nome = input("Digite o nome do aluno: ")
    encontrado = False

    for aluno in alunos:
        if aluno["Nome"].lower() == nome.lower():
            encontrado = True

            print("\nDados do aluno:")
            print(f"Nome: {aluno['Nome']}")
            print(f"CPF: {aluno['CPF']}")
            print(f"Peso: {aluno['Peso']}")
            print(f"Altura: {aluno['Altura']}")

            index = alunos.index(aluno)
            treino = treinos[index]

            if len(treino) > 0:
                print("\nTreino:")
                for exercicio in treino:
                    print(f"Exercício: {exercicio['Nome']}")
                    print(f"Número de repetições: {exercicio['Repeticoes']}")
                    print(f"Peso: {exercicio['Peso']}")

            confirmacao = input("\nTem certeza de que deseja excluir este aluno? (S/N): ")

            if confirmacao.lower() == "s":
                alunos.remove(aluno)
                treinos.remove(treino)
                print("Aluno excluído com sucesso!\n")

            break

    if not encontrado:
        print("Aluno não encontrado.")

def relatorio_alunos(): # Função para exibir o relatório de alunos
    print("\n--- Relatório de Alunos ---")
    print("1 - Todos os alunos")
    print("2 - Alunos ativos")
    print("3 - Alunos inativos")
    print("0 - Voltar ao menu principal")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        lista_alunos = alunos
    elif opcao == "2":
        lista_alunos = [aluno for aluno in alunos if aluno["Status"]]
    elif opcao == "3":
        lista_alunos = [aluno for aluno in alunos if not aluno["Status"]]
    elif opcao == "0":
        return
    else:
        print("Opção inválida. Por favor, digite novamente.\n")
        return

    lista_alunos = sorted(lista_alunos, key=lambda x: x["Nome"])

    print("\n--- Lista de Alunos ---")
    for aluno in lista_alunos:
        print(f"Nome: {aluno['Nome']}")
        print(f"CPF: {aluno['CPF']}")
        print(f"Peso: {aluno['Peso']}")
        print(f"Altura: {aluno['Altura']}")
        print(f"imc_: {aluno['IMC']}")
        print(f"Status: {'Ativo' if aluno['Status'] else 'Inativo'}")
        if aluno['Plano'] == 1:
            print("Plano: Básico (3 dias na semana)")
        elif aluno['Plano'] == 2:
            print("Plano: Regular (5 dias na semana)")
        elif aluno['Plano'] == 3:
            print("Plano: Premium (7 dias na semana)")
        else:
            print("Plano: Não definido")
        print()

alunos = []
treinos = []

while True:
    print("--- Menu Principal ---")
    print("1 - Cadastrar aluno")
    print("2 - Gerenciar treino")
    print("3 - Consultar aluno")
    print("4 - Atualizar cadastro do aluno")
    print("5 - Excluir aluno")
    print("6 - Relatório de alunos")
    print("7 - IMC rápido")
    print("0 - Sair")


    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        gerenciar_treino()
    elif opcao == "3":
        buscar_aluno()
    elif opcao == "4":
        atualizar_cadastro()
    elif opcao == "5":
        excluir_aluno()
    elif opcao == "6":
        relatorio_alunos()
    elif opcao == "7":
        peso = float(input("Digite o peso do aluno: "))
        altura = float(input("Digite a altura do aluno: "))
        imc = peso / (altura ** 2)
        imc_ = "{:.2f}".format(imc)
        print("Seu IMC é: ", imc_)

        if imc < 16:
            print("Magreza grave")
        elif 16 <= imc < 17:
            print("Magreza moderada")
        elif 17 <= imc < 18.5:
            print("Magreza leve")
        elif 18.5 <= imc < 25:
            print("Saudável")
        elif 25 <= imc < 30:
            print("Sobrepeso")
        elif 30 <= imc < 35:
            print("Obesidade Grau I")
        elif 35 <= imc < 40:
            print("Obesidade Grau II (severa)")
        else:
            print("Obesidade Grau III (mórbida)")
        
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, digite novamente.\n")