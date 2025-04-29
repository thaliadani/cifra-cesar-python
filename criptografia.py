def cifra_cesar(texto, deslocamento):
    palavraFinal = ""
    for letra in texto:
        if letra.isalpha():
            base=ord('A') if letra.isupper() else ord('a')
            codigo = (ord(letra) - base + deslocamento) % 26 + base
            palavraFinal += chr(codigo) 
        else:
            palavraFinal += letra 
    return palavraFinal
            
mensagem = input("Digite a mensagem a ser criptografada:")
chave = 3 * 2
        
mensagem_cifrada = cifra_cesar(mensagem, chave)
print("Mensagem criptografada: ", mensagem_cifrada)