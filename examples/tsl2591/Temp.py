from sense_hat import SenseHat
from time import sleep
from datetime import datetime, timedelta
import csv
import serial

sense = SenseHat()

light_port = "Insere le port sur arduino en ENTIER"

ser = serial.Serial(light_port, 9800, timeout=1)

for k in range(10):
	ser.readline()

start_time = datetime.now()
now_time = datetime.now()
time_ok = True
dicti = []

while(time_ok):
    temp = round(sense.get_temperature(), 2)
    lumi = ser.readline().decode()
    dicti.append({"date":datetime.now(), "temp":temp, "light":lumi})
    
    #Temps de dodo entre chaque prises
    sleep(30)
    now_time = datetime.now()
    
    #Temps d'excution totale
    time_ok = start_time + timedelta(minutes=180) >= now_time

ser.close()

f = open("temps.csv", "w", encoding="utf-8")
    
with f:
    headers=["date", "temp", "light"]
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    
    for dictio in dicti:
        writer.writerow(dictio)
