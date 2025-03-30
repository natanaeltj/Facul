print('Bem vindo a copiadora de Natanael Teixeira \n')

servico_preco = 0

def escolha_servico():
    servico = ''
    while(servico not in ('DIG', 'ICO', 'IPB', 'FOT')):
        print('Entre com o tipo de serviço desejado: \n DIG - Digitalização \n ICO - Impressão colorida \n IPB - Impressão Preto e Branco \n FOT - Fotocópia')
        servico = input('>>')
        if(servico not in ('DIG', 'ICO', 'IPB', 'FOT')):
            print('opção invalida, tente novamente a seguir \n')
        elif(servico in ('DIG', 'ICO', 'IPB', 'FOT')):
            return servico

servico_E = escolha_servico()
if servico_E == 'DIG':
    custo_p_pag = 1.10
elif servico_E == 'ICO':
    custo_p_pag = 1.00
elif servico_E == 'IPB':
    custo_p_pag = 0.40
elif servico_E == 'FOT':
    custo_p_pag = 0.20

def num_pagina():
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


def servico_extra():
    servico_add = ''
    while(servico_add not in ('1', '2','0')):
        print('Deseja adicioar algum serviço? \n 1 - Encardenação Simples - R$ 15.00 \n 2 - Encardenação Capa Dura - R$ 40.00 \n 0 - Não desejo mais nada')
        servico_add = input('>>')
        if(servico_add == '1'):
            servico_preco = 15.00
            return servico_preco
        elif(servico_add == '2'):
            servico_preco = 40.00
            return servico_preco
        elif(servico_add == '0'):
            servico_preco = 0
            return servico_preco
        else:
            print('Valor invalido, por favor insira novamente')
extra = servico_extra()

if extra == '1':
    servico_preco = 15.00
elif extra == '2':
    servico_preco = 40.00
elif extra == '0':
    extra = 0



total = custo_p_pag * paginas + servico_preco

if extra == None:
    print(f'Total: R$ {total} (serviço: R${custo_p_pag}) * páginas: {paginas} (SEM SERVIÇO ADICIONAL)')
else:
    print(f'Total: R$ {total} serviço: R$ {custo_p_pag} * páginas: {paginas} + extra: R$ {extra}')


















