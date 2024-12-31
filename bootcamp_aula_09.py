dicionario_de_programacao = {
    "Bug": "Um erro no código que impede que o programa funcione como esperado.",
    "Feature": "Um novo recurso ou funcionalidade que o usuário pode adicionar ao programa.",
    "Refactor": "Uma alteração no código que não altera o comportamento do programa, mas torna o código mais legível e fácil de manter.",
    "Function": "Um conjunto de instruções que realiza uma tarefa específica.",
    "Loop": "Um conjunto de instruções que se repetem até que uma condição seja satisfeita."
}

# print(dicionario_de_programacao["Refactor"])

dicionario_de_programacao["List"] = "Uma estrutura de dados que armazena uma coleção de elementos."

# print(dicionario_de_programacao["List"])

for chave in dicionario_de_programacao:
    print(chave)
    print(dicionario_de_programacao[chave])