# Desenvolver um programa que:
# 1 - Permita cadastrar informações de pacientes (nome, idade, telefone)
# 2 - Calcule e exiba: Nº total de pacientes cadastrados, Idade média dos pacientes, Paciente novo e mais velho
# 3 - Permita Buscar um paciente pelo nome
# 4 - Exiba todos os pacientes cadastrados de forma organizada
# Precisa conter listas e dicionários;
# Menu simples para navegação;
# Tratar possíveis erros de entrada;
# O programa deve funcionar em loop até o usuário escolher sair.

def main():
    opção = 0

    # Já com cadastros genéricos para verificar a funcionalidade do programa
    # Atualmente grava novos cadastros apenas na memória
    # Falta adicionar um salvamento externo, pela literatura, em formato json
    cadastros = [
        {'nome': 'Roberto Silva', 'idade': 35, 'telefone': '(14) 99999-8888'},
        {'nome': 'Jovana Oliveira', 'idade': 10, 'telefone': '(14) 98888-7777'}
    ]

    while opção != 5:
        print("=~"*19)
        print("Menu\n"
              "[1] Cadastrar Novo Paciente\n"
              "[2] Estatísticas\n"
              "[3] Buscar Paciente\n"
              "[4] Exibir Pacientes Cadastrados\n"
              "[5] Sair")
        print("=~"*19)
        opção = int(input("Qual comando deseja efetuar? "))

        if opção == 1:
            paciente = cadastrar_paciente()
            cadastros.append(paciente)
            print("Paciente cadastrado com sucesso!")
            aguardar_continuar()

        elif opção == 2:
            estatística(cadastros)
            aguardar_continuar()

        elif opção == 3:
            buscar(cadastros)
            aguardar_continuar()

        elif opção == 4:
            exibir(cadastros)
            aguardar_continuar()

        elif opção == 5:
            break

        else:
            print("Opção inválida. Escolha de 1 a 5")
        print("=-=" * 13)
    print("Fim do programa! Volte Sempre!")


def cadastrar_paciente():
    # Coleta dados de um paciente, tratando possíveis erros no nome, idade e telefone
    respostas = {}

    # Verifica se há números no nome e armazena com a primeira letra sempre maiúscula
    while True:
        try:
            nome = input("Nome: ").strip().title()
            if not nome:
                raise ValueError("O nome não pode estar vazio.")
            if any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            respostas['nome'] = nome
            break
        except ValueError as e:
            print(f"entrada inválida: {e} Tente novamente.")

    # Verifica se a idade é um valor inteiro e positivo
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0:
                raise ValueError("A idade não pode ser negativa.")
            respostas['idade'] = idade
            break
        except ValueError:
            print("Entrada inválida, digite um número inteiro para a idade")

    # Verifica se o telefone tem 10 ou 11 números e armazena no formato (XX) XXXXX-XXXX
    while True:
        try:
            telefone = input("Telefone: ").strip()
            telefone_limpo = ''.join(filter(str.isdigit, telefone))
            if len(telefone_limpo) < 10 or len(telefone_limpo) > 11:
                raise ValueError(
                    "Telefone deve ter 10 ou 11 dígitos (DDD + número).")

            if len(telefone_limpo) == 10:
                telefone_formatado = f"({telefone_limpo[:2]}) {telefone_limpo[2:6]}-{telefone_limpo[6:]}"

            else:
                telefone_formatado = f"({telefone_limpo[:2]}) {telefone_limpo[2:7]}-{telefone_limpo[7:]}"

            respostas['telefone'] = telefone_formatado
            break
        except ValueError as e:
            print(f"Telefone inválido: {e}")

    return respostas


def estatística(cadastros):
    # Calcular e exibir: Nº total de pacientes cadastrados, Idade média dos pacientes, Paciente novo e mais velho
    if not cadastros:
        print("Ainda não possui nenhum paciente cadastrado.")
        return

    total = len(cadastros)
    idades = [paciente['idade'] for paciente in cadastros]
    média_idades = sum(idades) / total

    paciente_mais_velho = max(cadastros, key=lambda x: x['idade'])
    paciente_mais_novo = min(cadastros, key=lambda x: x['idade'])

    print("=" * 39)
    print("Estatísticas dos Pacientes")
    print("=" * 39)
    print(f"Total de pacientes cadastrados: {total}")
    print(f"Média de idades dos pacientes: {média_idades:.1f}")
    print(
        f"Paciente mais velho: {paciente_mais_velho['nome']} com {paciente_mais_velho['idade']} anos")
    print(
        f"Paciente mais novo: {paciente_mais_novo['nome']} com {paciente_mais_novo['idade']} anos")
    print("=" * 39)


def exibir(cadastros):
    # Mostra uma lista de todos os cadastros
    if not cadastros:
        print("Ainda não possui nenhum paciente cadastrado.")
        return

    print("=" * 39)
    print("Pacientes Cadastrados:", len(cadastros))
    print("=" * 39)
    print(f"{'NOME':<15} {'IDADE':<6} {'TELEFONE':<15}")
    print("-" * 39)
    for paciente in cadastros:
        print(
            f"{paciente['nome']:<15} {paciente['idade']:<6} {paciente['telefone']:<15}")


def buscar(cadastros):
    # Busca um paciente específico
    if not cadastros:
        print("Ainda não possui nenhum paciente cadastrado.")
        return

    print("Digite o nome do paciente que deseja buscar.")
    nome_busca = str(input("Nome: ")).strip().title()

    resultados = []

    for paciente in cadastros:
        if nome_busca in paciente['nome']:
            resultados.append(paciente)

    if resultados:
        print("=" * 39)
        print("Pacientes Encontrados:", len(resultados))
        print("=" * 39)
        print(f"{'NOME':<15} {'IDADE':<6} {'TELEFONE':<15}")
        print("-" * 39)
        for paciente in resultados:
            print(
                f"{paciente['nome']:<15} {paciente['idade']:<6} {paciente['telefone']:<15}")

    else:
        print("O paciente em questão ainda não possui cadastro.")


def aguardar_continuar():
    # Aguarda pressionar enter para voltar ao menu
    input("\n -- Aperte Enter para continuar --\n")


main()
