print('Bem-vendo a loja de gelados do Natanael Teixeira')
print('-'*19 + 'Cardápio' + '-'*20)
print('-'*47)
print('-'*3 + '|' + ' Tamanho ' + ' | ' + ' Cupuaçu (CP) ' + '|' + ' Açaí (AC) ' + ' |' + '-'*3)
print('-'*3 + '|' + '    P    ' + ' | ' + '  R$  9.00  ' + '  |' + ' R$  11.00 ' + ' |' + '-'*3)
print('-'*3 + '|' + '    M    ' + ' | ' + '  R$  14.00  ' + ' |' + ' R$  16.00 ' + ' |' + '-'*3)
print('-'*3 + '|' + '    G    ' + ' | ' + '  R$  18.00  ' + ' |' + ' R$  20.00 ' + ' |' + '-'*3)
print('-'*47)
print('-'*47)

pergunta = 'S' #Inicia a condicional do programa
total = 0 #Irá receber o valor total da compra no final de cada

while(pergunta == 'S'):
    sabor = input('Insira o sabor desejado (CP/AC):') #Recebe o sabor selecionado

    if(sabor == 'CP'):
        tamanho = input('insira o tamanho desejado (P/M/G):') #recebe o tamanho selecionado
        if(tamanho == 'P'):
            preco = 9.00
        elif(tamanho =='M'):
            preco = 14.00
        elif(tamanho == 'G'):
            preco = 18.00
        else:
            print('Opção invalida!!! tente novamente')
            print('')
            continue
        print(f'Você pediu um cupuaçu do tamanho {tamanho}: R${preco}')
        pergunta = input('Precisa de mais alguma coisa (S/N):')
        print(' ')
        total = total + preco #acumulador

    elif(sabor == 'AC'):
        tamanho = input('insira o tamanho desejado (P/M/G):') #Recebe o tamanho selecionado
        if (tamanho == 'P'):
            preco = 11.00
        elif (tamanho == 'M'):
            preco = 16.00
        elif (tamanho == 'G'):
            preco = 20.00
        else:
            print('Opção invalida!!! tente novamente')
            print('')
            continue
        print(f'Você pediu um açai do tamanho {tamanho}: R${preco}')
        pergunta = input('Precisa de mais alguma coisa(S/N):')
        print(' ')
        total = total + preco #acumulador

    elif(pergunta == 'N'): #Finaliza o programa
        break

    else:
        print('Opção invalida!!! tente novamente')
        print(' ')
        continue

print(f'O valor total a ser pago: R${total}')
