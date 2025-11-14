# Uma lista é uma "variável" que suporta muitos dados
frutas = []  # cria uma lista vazia chamada frutas

# quando eu coloco a lista apenas [], eu estou dizendo que ela é vazia
print(frutas)  # mostra na tela a lista (no momento, vazia)

# o usuário pode "add" valor à lista, pode "excluir" da lista,
# pode "ver" a lista, e pode "sair" do sistema

print("-------- Bem vindo, ao varejão Gen --------")  # mensagem de boas-vindas
print("\nSelecione uma opção:")  # mostra o título das opções
print("01 - Adicione uma fruta")  # opção para adicionar frutas
print("02 - Excluir uma fruta")  # opção para excluir frutas
print("03 - Ver lista de fruta")  # opção para visualizar todas as frutas
print("04 - SAIR")  # opção para sair do programa

# pede para o usuário escolher uma opção digitando um número
escolha = int(input("\nQual opção você desejada incluir?"))

# verifica se o número digitado está fora das opções (menor que 1 ou maior que 4)
if escolha < 1 or escolha > 4:
    print("\nEscolha não reconhecida, finalizando o sistema")  # mensagem de erro
else:
    # se a escolha estiver entre 1 e 4, o programa entra no loop
    while escolha >= 1 or escolha < 4:
        
        # caso 1 - adicionar fruta
        if escolha == 1:
            nova_fruta = input("\nQual fruta quer adicionar?")  # pede o nome da fruta
            # para adicionar um elemento na lista eu devo chamar a lista e usar o método append(), anexando o novo valor
            frutas.append(nova_fruta)
            # exibe o último item adicionado (frutas[-1] é o último da lista)
            print("\nFruta", frutas[-1], "adicionada com sucesso!")
            # pergunta novamente o que o usuário deseja fazer
            escolha = int(input("\nQual opção desejada?"))

        # caso 2 - excluir fruta
        elif escolha == 2:  # vai aparecer enumerado
            # percorre a lista, mostrando posição e nome da fruta
            for posicao, cada_fruta in enumerate(frutas, start=1):  # mostra a lista numerada a partir de 1
                print(posicao, " - ", cada_fruta)
            print("\nAgora você pode excluir um produto")  # avisa que o usuário pode excluir
            posicao_fruta = int(input("Digite a posição da fruta"))  # pede qual número o usuário quer remover
            print("A", posicao_fruta, "foi exlcuida")  # mostra qual posição foi excluída
            frutas.pop(posicao_fruta - 1)  # pop remove 01 item da lista (índice é posição - 1)
            print("\nFruta excluida com sucesso")  # confirma exclusão
            escolha = int(input("Qual a opção desejada?"))  # pergunta novamente o que o usuário deseja fazer
        
        # caso 3 - ver lista
        elif escolha == 3:
            print("\nSua lista de frutas é:")  # título da lista
            for nome_fruta in frutas:  # percorre a lista mostrando cada fruta
                print(nome_fruta)  # mostra o nome da fruta
            escolha = int(input("\nQual outra opção desejada?"))  # pergunta novamente o que o usuário deseja fazer

        # caso 04 - sair
        elif escolha == 4:
            print("\nTchau, até próxima!")  # mensagem de despedida
            break  # encerra o loop e o programa termina