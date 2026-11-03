def carregar_avaliacoes():
    avaliacoes = []

    try:
        arquivo = open("avaliacoes.txt", "r", encoding="utf-8")
        for linha in arquivo:
            dados = linha.strip().split(";")
            idade = int(dados[0])
            avaliacao = dados[1]
            avaliacoes.append((idade, avaliacao))
        arquivo.close()
    except FileNotFoundError:
        pass
    return avaliacoes
def cadastrar_avaliacao():
    print("\n===== CADASTRAR AVALIAÇÃO =====")
  
    while True:
        try:
            idade = int(input("Digite a idade do cliente: "))
            if idade > 0:
                break
            else:
                print("Digite uma idade válida.")

        except ValueError:
            print("Digite apenas números.")

    print("\nEscolha a avaliação:")
    print("1. Ótimo")
    print("2. Bom")
    print("3. Regular")
    print("4. Péssimo")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao >= 1 and opcao <= 4:
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Digite apenas números.")

    opcoes = ["Ótimo", "Bom", "Regular", "Péssimo"]
    avaliacao = opcoes[opcao - 1]
    arquivo = open("avaliacoes.txt", "a", encoding="utf-8")
    arquivo.write(f"{idade};{avaliacao}\n")
    arquivo.close()
    print("\nAvaliação cadastrada com sucesso!")


def listar_avaliacoes():
    print("\n===== AVALIAÇÕES CADASTRADAS =====")

    avaliacoes = carregar_avaliacoes()

    if len(avaliacoes) == 0:
        print("Nenhuma avaliação cadastrada.")
    else:
        contador = 1

        for idade, avaliacao in avaliacoes:
            print(f"Cliente {contador} - Idade: {idade} - Avaliação: {avaliacao}")
            contador += 1


def consultar_estatisticas():
    print("\n===== ESTATÍSTICAS DAS AVALIAÇÕES =====")

    avaliacoes = carregar_avaliacoes()

    if len(avaliacoes) == 0:
        print("Nenhuma avaliação cadastrada.")
        return

    total = len(avaliacoes)

    otimo = 0
    bom = 0
    regular = 0
    pessimo = 0

    mais_velho = avaliacoes[0]
    mais_novo = avaliacoes[0]

    for idade, avaliacao in avaliacoes:
        if avaliacao == "Ótimo":
            otimo += 1
        elif avaliacao == "Bom":
            bom += 1
        elif avaliacao == "Regular":
            regular += 1
        elif avaliacao == "Péssimo":
            pessimo += 1
        if idade > mais_velho[0]:
            mais_velho = (idade, avaliacao)
        if idade < mais_novo[0]:
            mais_novo = (idade, avaliacao)

    print(f"\nTotal de respondentes: {total}")

    print(f"\nÓtimo: {otimo}")
    print(f"Bom: {bom}")
    print(f"Regular: {regular}")
    print(f"Péssimo: {pessimo}")

    print("\nRespondente mais velho:")
    print(f"Idade: {mais_velho[0]} anos")
    print(f"Avaliação: {mais_velho[1]}")

    print("\nRespondente mais novo:")
    print(f"Idade: {mais_novo[0]} anos")
    print(f"Avaliação: {mais_novo[1]}")

while True:
    print("\n===== SISTEMA DE AVALIAÇÃO DO CINEMA =====")
    print("1. Cadastrar avaliação")
    print("2. Listar avaliações")
    print("3. Consultar estatísticas")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        cadastrar_avaliacao()
    elif opcao == "2":
        listar_avaliacoes()
    elif opcao == "3":
        consultar_estatisticas()
    elif opcao == "4":
        print("\nPrograma encerrado!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
