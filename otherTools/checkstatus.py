import os
import requests
import time

BANNER = r"""
 $$$$$$\ $$$$$$$$\  $$$$$$\ $$$$$$$$\ $$\   $$\  $$$$$$\  
$$  __$$\\__$$  __|$$  __$$\\__$$  __|$$ |  $$ |$$  __$$\ 
$$ /  \__|  $$ |   $$ /  $$ |  $$ |   $$ |  $$ |$$ /  \__|
\$$$$$$\    $$ |   $$$$$$$$ |  $$ |   $$ |  $$ |\$$$$$$\  
 \____$$\   $$ |   $$  __$$ |  $$ |   $$ |  $$ | \____$$\ 
$$\   $$ |  $$ |   $$ |  $$ |  $$ |   $$ |  $$ |$$\   $$ |
\$$$$$$  |  $$ |   $$ |  $$ |  $$ |   \$$$$$$  |\$$$$$$  |
 \______/   \__|   \__|  \__|  \__|    \______/  \______/ 
                                                          
                                                          
                                                          
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def verificar_estado_site(url):
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("\033[92mO site está ativo.\033[0m")  # Mensagem em verde quando o site está ativo
            else:
                print("\033[91mO site está inativo.", response.status_code, "\033[0m")  # Mensagem em vermelho quando o site está inativo
        except requests.exceptions.RequestException:
            print("Ocorreu um erro ao verificar o estado do site.")

        time.sleep(0.5)

clear_screen()
print("\033[1;34m" + BANNER + "\033[0m")

url = input("Digite a URL do site que deseja verificar o estado: ")
verificar_estado_site(url)
