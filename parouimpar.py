#projeto do par ou impar
while True:
    try:
        valor = int(input('Digite um número '))
        if valor % 2 ==0:
            print ('Esse é um número par ')
        else:
            print ('Esse é um número impar ')    
    except:
            print ('Digite apenas números ')