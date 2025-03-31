print('Bem vindo a copiadora de Natanael Teixeira \n')

def escolha_servico(): #Realiza a seleção do serviço
    servico = ''
    while(servico not in ('DIG', 'ICO', 'IPB', 'FOT')):
        print('Entre com o tipo de serviço desejado: \n DIG - Digitalização \n ICO - Impressão colorida \n IPB - Impressão Preto e Branco \n FOT - Fotocópia')
        servico = input('>>')
        if(servico not in ('DIG', 'ICO', 'IPB', 'FOT')):
            print('opção invalida, tente novamente a seguir \n')
        elif(servico in ('DIG', 'ICO', 'IPB', 'FOT')):
            return servico

servico_E = escolha_servico() #Salva custo por pagina do serviço selecionado
if servico_E == 'DIG':
    custo_p_pag = 1.10
elif servico_E == 'ICO':
    custo_p_pag = 1.00
elif servico_E == 'IPB':
    custo_p_pag = 0.40
elif servico_E == 'FOT':
    custo_p_pag = 0.20

def num_pagina(): #define o número de paginas escolhido
    x = 0
    while(True):

        try:
            x = int(input('Insira o número de páginas: '))
            if x > 20000:
                print('Valor acima do esperado!!Por favor tente novamente:\n')
            else:
                return x
        except ValueError:
            print('Esse não é um número válido!! Por favor tente novamente')

paginas = num_pagina()

if paginas >= 20 and paginas < 200: #Define o valor do desconto pelo número de páginas
    desconto = 15 / 100
elif paginas >= 200 and paginas < 2000:
    desconto =  20 / 100
elif paginas >= 2000 and paginas < 20000:
    desconto = 25 / 100
else:
    desconto = 0
paginas_desconto = paginas - (paginas * desconto) #calcula o desconto


def servico_extra(): #retorna o valor do serviço requisitado
    servico_add = ''
    while(servico_add not in ('1', '2','0')):
        print('Deseja adicioar algum serviço? \n 1 - Encardenação Simples - R$ 15.00 \n 2 - Encardenação Capa Dura - R$ 40.00 \n 0 - Não desejo mais nada')
        servico_add = input('>>')
        if(servico_add == '1'):
            return 15.00
        elif(servico_add == '2'):
            return 40.00
        elif(servico_add == '0'):
            return 0
        else:
            print('Valor invalido, por favor insira novamente')
extra = servico_extra()

total = (custo_p_pag * paginas_desconto) + extra #calcula o valor total

if extra == None: #mostra o valor total e a função sem serviço e com serviço adicional
    print(f'Total: R$ {total} (serviço: R${custo_p_pag}) * páginas: {paginas} (SEM SERVIÇO ADICIONAL)')
else:
    print(f'Total: R$ {total} serviço: R$ {custo_p_pag} * páginas: {paginas} + extra: R$ {extra}')


















