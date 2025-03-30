print('Bem vindo a loja do Natanael Teixeira')
desconto = 0 
valorP = int(input('Insira o valor do produto:')) #valorP guarda o valor individual do produto
quant = int(input('Insira a quantidade do produto:')) #quant indica a quantidade de produtos a serem comprados
valorF = valorP * quant #valorF recebe o valor da soma do valor do produto com a quantidade de produtos a serem comprados sem o desconto
valorD = 0 #valorD irá receber o valor com o desconto

if(valorF < 2500):
    desconto = 0 / 100 * valorF
    valorD = desconto - valorF
    print(f'Valor sem desconto: R${valorF}')
    print(f'Valor com desconto:R${abs(valorD)}')

elif(valorF >= 2500 and valorF < 6000):
    desconto = 4 / 100 * valorF
    valorD = desconto - valorF
    print(f'Valor sem desconto: R${valorF}')
    print(f'Valor com desconto:R${abs(valorD)}')
    
elif(valorF >= 6000 and valorF < 10000):
    desconto = 7 / 100 * valorF
    valorD = desconto - valorF
    print(f'Valor sem desconto: R${valorF}')
    print(f'Valor com desconto:R${abs(valorD)}')

else:
    desconto = 11 / 100 * valorF
    valorD = desconto - valorF
    print(f'Valor sem desconto: R${abs(valorF)}')
    print(f'Valor com desconto:R${abs(valorD)}')