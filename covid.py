import requests, json, time, datetime
import telepot
from telepot.loop import MessageLoop
# https://github.com/AzhariKun/Covid-Bot

def covidbot(msg):
  chat_id = msg['chat']['id']
  command = msg['text']
  if command == '/start':
    tokenbot.sendMessage(chat_id, str('Hai, Terima kasih telah menggunakan layanan kami.\n\nSilahkan pilih, apa yang kamu inginkan. \n 1 - Untuk menampilkan perkembangan data COVID-19 di Dunia. \n 2 - Untuk menampilkan data COVID-19 di Indonesia.'))
  elif command == '1':
    datapositif = requests.get('https://api.kawalcorona.com/positif')
    datasembuh = requests.get('https://api.kawalcorona.com/sembuh')
    datameninggal = requests.get('https://api.kawalcorona.com/meninggal')
    tokenbot.sendMessage(chat_id, str('Data COVID-19 di Dunia\n\n Total Positif: ' + json.loads(datapositif.text)['value'] + '\n Total Sembuh: ' + json.loads(datasembuh.text)['value'] + '\n Total Meninggal: ' + json.loads(datameninggal.text)['value'] + '\n\n Tetap waspada yah! Jaga dirimu dan orang disekitarmu dari virus COVID-19.'))
  elif command == '2':
    getapi = requests.get('https://api.kawalcorona.com/indonesia/')
    jumlah_covid = json.loads(getapi.text)
    tokenbot.sendMessage(chat_id, str('Data COVID-19 di Indonesia\n\n  POSITIF: ' + jumlah_covid[0]['positif'] + '\n  SEMBUH: ' + jumlah_covid[0]['sembuh'] + '\n  MENINGGAL: ' + jumlah_covid[0]['meninggal'] + '\n  DIRAWAT: ' + jumlah_covid[0]['dirawat'] + '\n\nTetap jaga kesehatan, dengan mengikuti himbauan dari pemerintah.\n1. Cuci Tangan\n2. Memakai masker\n3. Jaga Jarak atau Physical Distancing.'))
tokenbot = telepot.Bot('1765494667:AAEZJaoaEJTbsACurdqRNKfrB0tNzlyV3MY')
print(tokenbot.getMe())
MessageLoop(tokenbot, covidbot).run_as_thread()
while 1:
  time.sleep(2)