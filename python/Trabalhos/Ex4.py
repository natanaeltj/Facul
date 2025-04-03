lista_livro = [] #Irá guardar todos os objetos
id_global = 0 #id para contagem de livros criados
global contador

print('Bem vindo a livraria de Natanael Teixeira')

def menu_principal():#inicia o programa
    while (True):
        print('-'*54)
        print('-' * 20 + ('Menu Principal') + ('-') * 20)
        print('Escolha a opção desejada: \n 1 - Cadastrar Livro \n 2 - Consultar livro(s) \n 3 - Remover Livro \n 4 - Sair')
        try:
            opcoes = int(input('>>'))
            if opcoes in (1, 2, 3, 4):
                return opcoes
            else:
                print('Opção invalida!!! tente novamente')
        except:
            ('Tente um número de 1 a 4 por favor meu querido')

def cadastrar_livro(id): #adiciona o id,nome,autor e editora do livro a um objeto
    global id_global
    print('-' * 70)
    print('-' * 25 + 'MENU CADASTRAR LIVRO' + '-' * 25)
    contador = 1

    nome_livro = input('Por favor insira com o nome do livro: ')

    autor_livro = input('Por favor insira com o autor do livro: ')

    editora_livro = input('Por favor insira o editor(a) do livro: ')
    id_global += 1 #adiciona o id automaticamente a cada livro criado
    livro = { #salva as informações obtidas acima temporariamente e as salva para sempre no array lista_livro
        'id': id_global,
        'nome': nome_livro,
        'autor': autor_livro,
        'editora': editora_livro,
    }
    lista_livro.append(livro)
    print(f'Livro {nome_livro} cadastrado com sucesso')

def consultar_livro(): #Consulta os livros entrando no array e lendo o objeto
    print('-'* 60)
    print('-'*20 + 'MENU CONSULTAR LIVRO' + '-'*20)
    while(True):
        print('Escolha a opção desejada:\n 1 - Consultar todos \n 2 - Consultar por Id\n 3 - Consultar por autor\n 4 - Retornar ao menu')
        try:
            opcoes = int(input('>>'))

        except:
            print('Opção invalida! tente um numero de 1 a 4')

        if opcoes == 1:
            if len(lista_livro) == 0: #Olha se tem livros cadastrados no sistema
                print('Os livros ainda não foram cadastrados, tente novamente outra hora')
            else:
                for livro in lista_livro: # consulta todos os livros dentro do array e printa um por um no terminal
                    print(f'ID: {livro["id"]} \n Nome: {livro["nome"]} \n Autor: {livro["autor"]} \n Editora: {livro["editora"]}\n')

        elif opcoes == 2:
            id_pesquisa = int(input('Digite o ID do livro: '))
            livro_encontrado = next((livro for livro in lista_livro if livro['id'] == id_pesquisa)) #verifica id por id para encontrar o id requisitado de maneira sequencial retornando o primeiro elemento através do next
            if livro_encontrado:
                print(f'ID: {livro_encontrado["id"]} \n Nome: {livro_encontrado["nome"]} \n Autor: {livro_encontrado["autor"]} \n Editora: {livro_encontrado["editora"]}')
            else:
                print('Id inválido')

        elif opcoes == 3:
            autor_busca = input('Digite o nome do autor: ')
            livros_autor = [livro for livro in lista_livro if livro['autor'] == autor_busca] #realiza a busca pelo autor olhando lista por lista
            if livros_autor:
                for livro in livros_autor:
                    print(f'ID: {livro["id"]} \n Nome: {livro["nome"]} \n Autor: {livro["autor"]} \n Editora: {livro["editora"]}\n')
            else:
                print('Nenhum livro encontrado para este autor!')
        elif opcoes == 4:
            return

def remover_livro(): #Remove os livros por id
        print('-' * 65)
        print('-' * 25 + ' REMOVER LIVRO ' + '-' * 25)
        if not lista_livro:
            print('Nenhum livro cadastrado para remover.')
            return
        try:
            removedor = int(input('Digite o ID do livro a ser removido: '))
            livro_encontrado = next((livro for livro in lista_livro if livro['id'] == removedor))#verifica id por id para encontrar o id requisitado de maneira sequencial retornando o primeiro elemento através do next

            if livro_encontrado:
                lista_livro.remove(livro_encontrado)#Quando encontrado remove o livro da lista.
                print('livro removido com sucesso!')
            else:
                print('Id inválido!!')

        except ValueError:
            print('digite um número válido para o id por favorrrr.')

while True: #garante que a função menu_principal() continue rodando
    escolha = menu_principal()
    if escolha == 1:
        cadastrar_livro(1)
    elif escolha == 2:
        consultar_livro()
    elif escolha == 3:
        remover_livro()
    elif escolha == 4:
        print('Finalizando o programa...')
        break





