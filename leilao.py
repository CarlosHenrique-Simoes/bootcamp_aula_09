# TODO @<carlos>: - Solicitar nome e lance
# TODO @<carlos>: - Armazenar os dados em um dict
# TODO @<carlos>: - Verificar se novos lances serão adicionados
# TODO @<carlos>: - Comparbar os lances no dict

lances = {}


def maior_lance(lances):
    ganhador = ""
    maior_lance = 0

    max(lances)

    for jogador in lances:
        valor_do_lance = lances[jogador]
        if valor_do_lance > maior_lance:
            maior_lance = valor_do_lance
            ganhador = jogador

    print(f"O vencedor do leilão é {ganhador}, com o lance de {maior_lance} reais.")


continuar_leilao = True
while continuar_leilao:
    nome = input("Digite o seu nome: ")
    valor = int(input("Digite o seu lance: "))
    lances[nome] = valor
    novos_jogadores = input("Há algum outro jogador? (S/N): \n").lower()

    if novos_jogadores == "n":
        continuar_leilao = False
        maior_lance(lances)
    elif novos_jogadores == "s":
        print("\n" * 20)
