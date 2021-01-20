import requests
from bs4 import BeautifulSoup
import pywhatkit as kit
from datetime import datetime
import time

class Start:

    def trigger(self):
        while True:
            get_info = GetInfo()
            get_info.check_status()
            if content.quantity != 19: #19 es la cantidad de coursos al momento de iniciar el script
                whatsapp_message = WhatsappMessage()
                whatsapp_message.send_message()
            else:
                print("La cantidad no cambio")
                time.sleep(3600)

class GetInfo:

    def __init__(self):
        self.URL = "https://allcoursefree.com/"
        self.headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
        self.page = requests.get(self.URL, headers = self.headers)
    
    def check_status(self):
        
        soup = BeautifulSoup(self.page.text, 'html.parser')
        title = soup.find('h1', attrs={"class":'site-title'}).get_text()
        courses = soup.find('p', attrs={"class":'woocommerce-result-count'}).get_text()
        content.content(courses)

class Content:

    def content(self,courses):
        self.quantity = int(courses[-11:-8])
        print(str(self.quantity) + " #Debug")
        
class Time:

    def get_time(self):
        current = datetime.now().strftime("%H:%M:%S")
        self.current_hour = int(current[0:2])
        self.current_minute = int(current[3:5])
        self.transform_time(self.current_hour,self.current_minute)

    def transform_time(self,current_hour,current_minute):
        if current_minute == 59:
            sending_minute = 0
            sending_hour = current_hour + 1
        else:
            sending_minute = current_minute + 1 
            sending_hour = current_hour
        return sending_hour,sending_minute   
        
class WhatsappMessage:
    def __init__(self):
        self.number = "+541136646178"

    def send_message(self):
        time = Time()
        sending_hour,sending_minute  = time.get_time()
        kit.sendwhatmsg(self.number,"Cambio la cantidad de cursos https://allcoursefree.com/",sending_hour,sending_minute )
        print("Mensaje Enviado")   
                
content = Content()


