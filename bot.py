import pywhatkit


#importando as blibiotecas
import pywhatkit
import keyboard
import time
from datetime import datetime

#criando lista de contatos
contatos = ['numero']

#Definir intervalo de envio 
while len(contatos) >=1:
    #envaindo a mensagem
    pywhatkit.sendwhatmsg(contatos[0],"infectado.",datetime.now().hour,datetime.now().minute +2) 
    del contatos[0]#deletando o contato que a msg foi enviada
    time.sleep(10)
    keyboard.press_and_release('ctrl + w')#fechando a aqba do navegador para que não crie inumeras abas