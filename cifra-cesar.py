from colorama import Fore, Style, init
init(autoreset=True) 

opcoes = input(Fore.GREEN + "\n""======================= \n" 
    "Escolha uma das opções:\n \n "
    "1 - Criptografar \n "
    "2 - Descriptografar \n"
    "======================= \n"+ Style.RESET_ALL)

chave =  8 - (3 * 2)

def texto_criptografar(texto, deslocamento):
    palavraFinal = ""
    for letra in texto:
        if letra.isalpha():
            base=ord('A') if letra.isupper() else ord('a')
            codigo = (ord(letra) - base + deslocamento) % 26 + base
            palavraFinal += chr(codigo) 
        else:
            palavraFinal += letra 
    return palavraFinal

def texto_descriptografar(texto, deslocamento):
    return texto_criptografar(texto,-deslocamento)

if opcoes == "1":
    mensagem = input("Digite a mensagem a ser criptografada:")
    mensagem_cifrada = texto_criptografar(mensagem, chave)
    print("Mensagem criptografada: ", mensagem_cifrada)
elif opcoes == "2":
    mensagem = input("Digite a mensagem a ser descriptografada:")
    mensagem_cifrada = texto_descriptografar(mensagem, chave)
    print("Mensagem descriptografada: ", mensagem_cifrada)
else:
    print("Opção inválida")      

        

