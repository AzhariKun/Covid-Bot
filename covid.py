import requests, json, time, datetime
import telepot
from telepot.loop import MessageLoop
# https://github.com/AzhariKun/Covid-Bot

def covidbot(msg):
  chat_id = msg['chat']['id']
  command = msg['text']
  if command == '/info':
    getapi = requests.get('https://api.kawalcorona.com/indonesia/')
    jumlah_covid = json.loads(getapi.text)
    tokenbot.sendMessage(chat_id, str('Data COVID-19 di Indonesia\n\n  POSITIF: ' + jumlah_covid[0]['positif'] + '\n  SEMBUH: ' + jumlah_covid[0]['sembuh'] + '\n  MENINGGAL: ' + jumlah_covid[0]['meninggal'] + '\n  DIRAWAT: ' + jumlah_covid[0]['dirawat'] + '\n\nTetap jaga kesehatan, dengan mengikuti imbauan dari pemerintah.\n1. Cuci Tangan\n2. Memakai masker\n3. Jaga Jarak atau Physical Distancing.'))
tokenbot = telepot.Bot('Your Token')
print(tokenbot.getMe())
MessageLoop(tokenbot, covidbot).run_as_thread()
while 1:
  time.sleep(10)