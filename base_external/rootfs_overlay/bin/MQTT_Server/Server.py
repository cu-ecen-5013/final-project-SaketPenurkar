# Reference - https://github.com/eclipse/paho.mqtt.python

import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.client as mqtt
import datetime

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test")

datetime_object = datetime.datetime.now() 

def on_message(client, userdata, msg):
  a=msg.payload.decode()
  print("Payload is: %s" %(a))
  data_identifier = a[0]
  print("Data Identifier is: %s" %(data_identifier))
  if data_identifier == "T":
      try:
          data_to_write = a[1:]
          print("Data to write is %s" %(data_to_write))
          file_handler = open('/usr/htdocs/temperature.txt', 'a')
          file_handler.write(data_to_write)
          file_handler.write("\n")
          file_handler.close()
          #print(datetime_object)
          #print("Current Temperature is - - ->: %s" %a)
      except Exception as e:
          print(e)
  elif data_identifier == "H":
      try:
          data_to_write = a[1:]
          print("Data to write is %s" %(data_to_write))
          file_handler = open('/usr/htdocs/humidity.txt', 'a')
          print("Writing to file")
          file_handler.write(data_to_write)
          file_handler.write("\n")
          print("Closing file")
          file_handler.close()
          #print(datetime_object)
          #print("Current Humidity is - - ->: %s" %a)
      except Exception as e:
          print(e)
  else:
      print("T not found")

 
client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
