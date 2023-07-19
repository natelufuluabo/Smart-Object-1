from RPiSim import GPIO
import paho.mqtt.client as mqtt
import time
import sys
import signal


def terminer(signum, frame):
    print("Terminer")
    GPIO.output(18, GPIO.LOW)
    GPIO.cleanup()
    sys.exit(0)


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))
    commande = str(message.payload.decode("utf-8"))
    
    if commande == "alarm_on":
        GPIO.output(17, GPIO.HIGH)
    elif commande == "alarm_off":
        GPIO.output(17, GPIO.LOW)
    elif commande == "living_room_on":
        GPIO.output(27, GPIO.HIGH)
    elif commande == "living_room_off":
        GPIO.output(27, GPIO.LOW)
    elif commande == "kitchen_on":
        GPIO.output(22, GPIO.HIGH)
    elif commande == "kitchen_off":
        GPIO.output(22, GPIO.LOW)
       

# Les GPIOS
signal.signal(signal.SIGINT, terminer)
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    # Alarme
    GPIO.setup(17, GPIO.MODE_OUT, initial=GPIO.LOW)
    # Lumière Salon
    GPIO.setup(27, GPIO.MODE_OUT, initial=GPIO.LOW)
    # Lumière Cuisine
    GPIO.setup(22, GPIO.MODE_OUT, initial=GPIO.LOW)
except Exception:
    print("Problème avec les GPIO")

# MQTT

host = "node02.myqtthub.com"
port = 1883
clean_session = True
client_id = "thermo"
username = "natelufuluabo@yahoo.ca"
password = "Kylian2021!!"

client = mqtt.Client(client_id=client_id, clean_session=clean_session)
client.username_pw_set(username, password)
client.connect(host, port)
client.loop_start()
client.subscribe("Nathan/Etats")
client.on_message = on_message

while True:
    time.sleep(0.5)
