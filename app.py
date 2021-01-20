import requests
from bs4 import BeautifulSoup
import pywhatkit as kit
from datetime import datetime
import time

class Start:
    """Se inicia el proceso"""
    def trigger(self):
        while True:
            get_info = GetInfo()
            get_info.check_status() 
            """Se actualiza el valor quantity al llamar al metodo check_status"""
            if content.quantity != 30: #es la cantidad de coursos al momento de iniciar el script
                whatsapp_message = WhatsappMessage()
                whatsapp_message.send_message()
            else:
                print("La cantidad no cambio")
                time.sleep(3600)

class GetInfo:
    """Se obtiene la información necesaria de la pagina"""
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
    """Obtiene la candidad de cursos y lo devuelve como INT"""
    def content(self,courses):
        self.quantity = int(courses[-11:-8])
        print(str(self.quantity) + " #Debug")
        
class Time:
    """Se encarga del manejo del tiempo"""
    def get_time(self):
        """Obtiene el horario actual"""
        current = datetime.now().strftime("%H:%M:%S")
        self.current_hour = int(current[0:2])
        self.current_minute = int(current[3:5])
        self.transform_time(self.current_hour,self.current_minute)

    def transform_time(self,current_hour,current_minute):
        """
        Se transforma el horario para enviar
        La libreria necesita que el horario de envio sea mayor que el actual 
        ya que toma tiempo abrir WppWeb y enviar
        """
        if current_minute == 59:
            """
            Si el minuto actual es 59 debe volver a 0 y pasar a la siguiente hora
            ya que no hay minuto 60
            """
            self.sending_minute = 0
            self.sending_hour = current_hour + 1
        else:
            """
            Sino se suman 2 minutos al horario actual (si se pone menos tiempo, el 50% de las veces se buggea)
            """
            self.sending_minute = current_minute + 2 
            self.sending_hour = current_hour
       
        
class WhatsappMessage:
    """
    Maneja el Mensaje
    """
    def __init__(self):
        self.number = "+541136646178"

    def send_message(self):
        """
        Se crea el objeto time y se llama a la funcion para obtener el horario final de envio
        """
        time = Time()
        time.get_time()
        kit.sendwhatmsg(self.number,"Cambio la cantidad de cursos https://allcoursefree.com/",time.sending_hour,time.sending_minute )
        print("Mensaje Enviado")   
                
content = Content()


