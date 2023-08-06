import os
import requests

BANNER = r"""
$$$$$$$$\  $$$$$$\  $$\   $$\ $$$$$$$$\        $$$$$$\  $$\      $$\  $$$$$$\  
$$  _____|$$  __$$\ $$ | $$  |$$  _____|      $$  __$$\ $$$\    $$$ |$$  __$$\ 
$$ |      $$ /  $$ |$$ |$$  / $$ |            $$ /  \__|$$$$\  $$$$ |$$ /  \__|
$$$$$\    $$$$$$$$ |$$$$$  /  $$$$$\          \$$$$$$\  $$\$$\$$ $$ |\$$$$$$\  
$$  __|   $$  __$$ |$$  $$<   $$  __|          \____$$\ $$ \$$$  $$ | \____$$\ 
$$ |      $$ |  $$ |$$ |\$$\  $$ |            $$\   $$ |$$ |\$  /$$ |$$\   $$ |
$$ |      $$ |  $$ |$$ | \$$\ $$$$$$$$\       \$$$$$$  |$$ | \_/ $$ |\$$$$$$  |
\__|      \__|  \__|\__|  \__|\________|       \______/ \__|     \__| \______/ 
                                                                               
                                                                               
                                                                               
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class SMSAnonimo:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
    
    def enviar_sms(self):
        numero_alvo = input("Qual o número alvo? ")
        mensagem = input("Mensagem para ser enviada?  ")
        
        url = "https://rest.nexmo.com/sms/json"
        payload = {
            "api_key": self.api_key,
            "api_secret": self.api_secret,
            "from": "NEXMO_NUMBER",  # Número fornecido pela Nexmo
            "to": numero_alvo,
            "text": mensagem
        }
        
        try:
            response = requests.post(url, data=payload)
            data = response.json()
            
            if data["messages"][0]["status"] == "0":
                print("SMS enviado com sucesso!")
                print("Message ID:", data["messages"][0]["message-id"])
            else:
                print("Erro ao enviar o SMS:", data["messages"][0]["error-text"])
        except Exception as e:
            print("Erro ao enviar o SMS:", str(e))

clear_screen()
print("\033[1;34m" + BANNER + "\033[0m")

# Substitua as informações abaixo pelas suas credenciais da Nexmo
api_key = input("Sua key nexmo?  ")
api_secret = input("Sua api secret (nexmo)?  ")

sms_anonimo = SMSAnonimo(api_key, api_secret)
sms_anonimo.enviar_sms()
