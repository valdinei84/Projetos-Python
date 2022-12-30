#Crie uma função que receba duas palavras e retorne True caso 
# a primeira palavra seja um prefixo da segunda. Exemplo: 
# ’uf’ é prefixo de ’ufabc’. ’ufabc’ não é prefixo de ’uf’.
def verifica_prefixo(prefixo,palavra):
    if palavra[:len(prefixo)] == prefixo:
        return True
    else:
        return False
print(verifica_prefixo("para", "paralelepipedo"))


        