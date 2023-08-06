import os

BANNER = r"""
$$$$$$$\  $$$$$$$$\  $$$$$$\  $$$$$$$\ $$\     $$\ $$$$$$$\ $$$$$$$$\ 
$$  __$$\ $$  _____|$$  __$$\ $$  __$$\\$$\   $$  |$$  __$$\\__$$  __|
$$ |  $$ |$$ |      $$ /  \__|$$ |  $$ |\$$\ $$  / $$ |  $$ |  $$ |   
$$ |  $$ |$$$$$\    $$ |      $$$$$$   | \$$$$  /  $$$$$$$  |  $$ |   
$$ |  $$ |$$  __|   $$ |      $$  __$$<   \$$  /   $$  ____/   $$ |   
$$ |  $$ |$$ |      $$ |  $$\ $$ |  $$ |   $$ |    $$ |        $$ |   
$$$$$$$  |$$$$$$$$\ \$$$$$$  |$$ |  $$ |   $$ |    $$ |        $$ |   
\_______/ \________| \______/ \__|  \__|   \__|    \__|        \__|   
                                                                      
                                                                      
                                                                         
                                                                                           
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para descriptografar o texto usando a tecnologia MD5
def descriptografar_md5(texto_criptografado):
    return texto_criptografado

# Função para descriptografar o texto usando a tecnologia SHA
def descriptografar_sha(texto_criptografado):
    return texto_criptografado

# Função para descriptografar o texto usando a criptografia Y4X Level 7
def descriptografar_y4x(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 7)
        else:
            descriptografado += char
    return descriptografado

# Função para descriptografar o texto usando a criptografia R7G Level 11
def descriptografar_r7g(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 11)
        else:
            descriptografado += char
    return descriptografado

# Função para descriptografar o texto usando a criptografia FLK Level 21
def descriptografar_flk(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 21)
        else:
            descriptografado += char
    return descriptografado

# Função para descriptografar o texto usando a criptografia H1X
def descriptografar_h1x(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 53)
        else:
            descriptografado += char
    return descriptografado
    
def descriptografar_fck(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 9517)
        else:
            descriptografado += char
    return descriptografado


    
def descriptografar_sla(texto_criptografado):
    descriptografado = ""
    for char in texto_criptografado:
        if char.isalpha():
            descriptografado += chr(ord(char) - 1733)
        else:
            descriptografado += char
    return descriptografado
    

def main():
    clear_screen()
    print("\033[1;31m" + BANNER + "\033[0m")

    # Pede ao usuário um texto criptografado para descriptografar
    texto_criptografado = input("Texto criptografado: ")

    # Exibe as opções de descriptografia
    print("[01] MD5")
    print("[02] Y4X Level 7 crypt")
    print("[03] SHA")
    print("[04] R7G Level 11 crypt")
    print("[05] FLK Level 21 crypt")
    print("[06] H1X")
    print("[7] fck")
    print("[8] sla")
    # Pede ao usuário para escolher uma opção
    escolha = input("Escolha uma opção: ")

    # Verifica a escolha do usuário e executa a descriptografia correspondente
    if escolha in ["1", "01"]:
        texto_descriptografado = descriptografar_md5(texto_criptografado)
    elif escolha in ["2", "02"]:
        texto_descriptografado = descriptografar_y4x(texto_criptografado)
    elif escolha in ["3", "03"]:
        texto_descriptografado = descriptografar_sha(texto_criptografado)
    elif escolha in ["4", "04"]:
        texto_descriptografado = descriptografar_r7g(texto_criptografado)
    elif escolha in ["5", "05"]:
        texto_descriptografado = descriptografar_flk(texto_criptografado)
    elif escolha in ["6", "06"]:
        texto_descriptografado = descriptografar_h1x(texto_criptografado)
    elif escolha in ["7", "07"]:
        texto_descriptografado = descriptografar_fck(texto_criptografado)
    elif escolha in ["8", "08"]:
        texto_descriptografado = descriptografar_sla(texto_criptografado)
    else:
        print("Opção inválida!")

    # Exibe o resultado da descriptografia
    print("Texto descriptografado:", texto_descriptografado)

if __name__ == "__main__":
    main()
