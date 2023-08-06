import os
import requests
from termcolor import colored

BANNER = r"""
   ____     ______     ______      _____    _____    _____  
  (    )   (_  __ \   (   __ \    / ___/   / ____\  / ____\ 
  / /\ \     ) ) \ \   ) (__) )  ( (__    ( (___   ( (___   
 ( (__) )   ( (   ) ) (    __/    ) __)    \___ \   \___ \  
  )    (     ) )  ) )  ) \ \  _  ( (           ) )      ) ) 
 /  /\  \   / /__/ /  ( ( \ \_))  \ \___   ___/ /   ___/ /  
/__(  )__\ (______/    )_) \__/    \____\ /____/   /____/   
                                                            

"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_endereco(latitude, longitude):
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        endereco = data.get("display_name")
        return endereco
    return None

clear_screen()
print("\033[1;34m" + BANNER + "\033[0m")

# Solicitar as coordenadas do usuário
latitude = float(input("Digite a latitude: "))
longitude = float(input("Digite a longitude: "))

endereco = obter_endereco(latitude, longitude)

if endereco:
    print("Endereço encontrado:")
    print(endereco)
    
    # Salvar o endereço em um arquivo de texto
    with open("adress.txt", "w") as arquivo:
        arquivo.write(endereco)
        print("\n" + colored("Endereço salvo no arquivo 'adress.txt'.", "blue"))
else:
    print("Endereço não encontrado.")
