
'''Primeira opção'''
nome = 'Valdinei MR'
idade = 32 
pais = 'Brasil'
'''
print 
(f'Olá, eu sou o {nome}. Tenho {idade} anos. Moro no {pais}.')
'''
'''segunda opção'''
'''
print('Olá, eu sou o {nome}. Tenho {idade} anos. moro no {pais}.'.format(
    nome=nome, pais=pais, idade=idade)
)
'''
'''Terceira opção'''
print('Olá, eu sou o {}. Tenho {} anos. Moro no {}'.format(nome, idade, pais))
'''tudo esses bagulho funciona'''