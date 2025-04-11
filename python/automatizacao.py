import webbrowser 
from datetime import datetime
from time import sleep
import os


horario_desejado = "18:55"
url = "https://classroom.google.com/c/NzM5NDQ3OTIwMTc4?pli=1"
url2 = "https://mail.yahoo.com/d/search/keyword=escola%2520da%2520nuvem?.lang=pt-BR&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAHf3AMjCpB51lrJrDTRQZsBpTytI6uOoK3dcMAoYuS67cEejJdt6-DTRw3cdEk3tgYjnllOxGEk3sPwb--tqIwayaUgrqNs9pgELeEswFWF51Eh5lwLAo4qfi0AGnEnNV83i4MEcMm1FvPOe90Gt5_lTMd1qJ6vNdfQHaIam63fP"
bloco_de_notas = "gedit"

while True:
    agora = datetime.now().strftime("%H:%M")
    if agora == horario_desejado:
        webbrowser.open(url)
        webbrowser.open(url2)

        os.system(bloco_de_notas)
        sleep(60)
    sleep(2)    

    
