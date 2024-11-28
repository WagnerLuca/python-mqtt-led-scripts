from paho.mqtt import client as mqtt
import random
import threading
import time

print("Connecting to MQTT Broker..")
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("mqtt.dzg", 1883, 60)
mqttc.loop_start()
print("Connected")


def color_thread():
    while True:
        print("Change color")
        
        r = random.randint(0, 255)  # Starke Rottöne für die Flammen
        g = random.randint(0, 255)  # Warme gelblich-orange Töne
        b = random.randint(0, 255)    # Kaum Blau für die Glut
        # transition_duration = random.randint(1, 2)

        mqttc.publish("zigbee2mqtt/0x18fc260000b66b9f/set", '{"color":{"rgb":"'+str(r)+','+str(g)+','+str(b)+'"}}', 0)
        time.sleep(.5)

def brightness_thread():
    while True:
        # LED ON
        mqttc.publish("zigbee2mqtt/0x18fc260000b66b9f/set", '{"brightness": 0}')
        time.sleep(.4)

        # LED OFF
        mqttc.publish("zigbee2mqtt/0x18fc260000b66b9f/set", '{"brightness": 254}')
        time.sleep(.1)


  
color_thread = threading.Thread(target=color_thread)
brightness_thread = threading.Thread(target=brightness_thread)

color_thread.start()
brightness_thread.start()

# while True:
#     print("Change led:")
#     # Available inputs: 0,1,2
#     topic = "zigbee2mqtt/0x18fc260000b66b9f/set"
    
#     # Available inputs, jeweils: 0-255 (red,green,blue)

#     r = random.randint(200, 255)  # Starke Rottöne für die Flammen
#     g = random.randint(80, 150)  # Warme gelblich-orange Töne
#     b = random.randint(0, 50)    # Kaum Blau für die Glut
#     transition_duration = random.randint(1, 2)
#     # mqttc.publish(topic, "bytearray(color)", 1)
#     mqttc.publish("zigbee2mqtt/0x18fc260000b66b9f/set", '{"color":{"rgb":"'+str(r)+','+str(g)+','+str(b)+'"},"transition":'+str(transition_duration)+'}', 0)
#     time.sleep(transition_duration)