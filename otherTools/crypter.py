import os
import hashlib
from termcolor import colored

# Função para limpar a tela e exibir o banner em vermelho
def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(colored("                                                      ", "blue"))
    print(colored("                                                      ", "blue"))
    print(colored("   █████████                                  █████   ", "blue"))
    print(colored("  ███░░░░░███                                ░░███    ", "blue"))
    print(colored(" ███     ░░░  ████████  █████ ████ ████████  ███████  ", "blue"))
    print(colored("░███         ░░███░░███░░███ ░███ ░░███░░███░░░███░   ", "blue"))
    print(colored("░███          ░███ ░░░  ░███ ░███  ░███ ░███  ░███    ", "blue"))
    print(colored("░░███     ███ ░███      ░███ ░███  ░███ ░███  ░███ ███", "blue"))
    print(colored(" ░░█████████  █████     ░░███████  ░███████   ░░█████ ", "blue"))
    print(colored("  ░░░░░░░░░  ░░░░░       ░░░░░███  ░███░░░     ░░░░░  ", "blue"))
    print(colored("                         ███ ░███  ░███               ", "blue"))
    print(colored("                        ░░██████   █████              ", "blue"))
    print(colored("                         ░░░░░░   ░░░░░               ", "blue"))
    print("                                                                       ")
    print(colored("Nós não nos responsabilizamos pelo mau uso desta ferramenta", "blue"))
    print("                                                                       ")
    print("                                                                       ")
# Função para exibir as opções de criptografia
def exibir_opcoes():
    print("[01] MD5")
    print("[02] Y4X Level 7 crypt")
    print("[03] SHA")
    print("[04] R7G Level 11 crypt")
    print("[05] FLK Level 21 crypt")
    print("[06] H1X Level 53 crypt")
    print(colored("[07] Fucking 9517 crypt", "red"))
    print(colored("[08] I don't know", 'yellow', 'on_red'))
    print(colored("[09] XTC Neg 3917", 'green', 'on_blue'))

    
# Função para criptografar o texto usando a tecnologia MD5
def criptografar_md5(texto):
    md5_hash = hashlib.md5()
    md5_hash.update(texto.encode('utf-8'))
    return md5_hash.hexdigest()

# Função para criptografar o texto usando a tecnologia SHA
def criptografar_sha(texto):
    sha_hash = hashlib.sha256()
    sha_hash.update(texto.encode('utf-8'))
    return sha_hash.hexdigest()

# Função para criptografar o texto usando a criptografia Y4X Level 7
def criptografar_y4x(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 7)
        else:
            criptografado += char
    return criptografado

# Função para criptografar o texto usando a criptografia R7G Level 11
def criptografar_r7g(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 11)
        else:
            criptografado += char
    return criptografado

# Função para criptografar o texto usando a criptografia FLK Level 21
def criptografar_flk(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 21)
        else:
            criptografado += char
    return criptografado

# Função para criptografar o texto usando a criptografia H1X
def criptografar_h1x(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 53)
        else:
            criptografado += char
    return criptografado

#dumb chatgpt

def criptografar_fcking(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 9517)
        else:
            criptografado += char
    return criptografado
    
#no way

    
def criptografar_sla(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 1733)
        else:
            criptografado += char
    return criptografado
    
def criptografar_xtc(texto):
    criptografado = ""
    for char in texto:
        if char.isalpha():
            criptografado += chr(ord(char) + 8932)
        else:
            criptografado += char
    return criptografado


# Limpa a tela e exibe o banner em vermelho
limpar_tela()

# Pede ao usuário um texto para codificar
Pcrypt = input("Texto para ser criptografado: ")

# Exibe as opções de criptografia
exibir_opcoes()

# Pede ao usuário para escolher uma opção
escolha = input("Escolha uma opção: ")


# Verifica a escolha do usuário e executa a criptografia correspondente
if escolha in ["1", "01"]:
    texto_criptografado = criptografar_md5(Pcrypt)
elif escolha in ["2", "02"]:
    texto_criptografado = criptografar_y4x(Pcrypt)
elif escolha in ["3", "03"]:
    texto_criptografado = criptografar_sha(Pcrypt)
elif escolha in ["4", "04"]:
    texto_criptografado = criptografar_r7g(Pcrypt)
elif escolha in ["5", "05"]:
    texto_criptografado = criptografar_flk(Pcrypt)
elif escolha in ["6", "06"]:
    texto_criptografado = criptografar_h1x(Pcrypt)
elif escolha in ["7", "07"]:
    texto_criptografado = criptografar_fcking(Pcrypt)
elif escolha in ["8", "08"]:
    texto_criptografado = criptografar_sla(Pcrypt)
elif escolha in ["9", "09"]:
    texto_criptografado = criptografar_xtc(Pcrypt)
else:
    print("Opção inválida!")

# Exibe o resultado da criptografia
print("Texto criptografado:   \n\n", texto_criptografado)
