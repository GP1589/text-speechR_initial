# import serial
# import pyttsx3

# # Configurar el motor de síntesis de voz
# engine = pyttsx3.init()

# # Configurar la comunicación serial
# ser = serial.Serial('COM3', 9600) # Reemplaza COM3 con el puerto serial que estás utilizando

# # Función para enviar texto a Arduino
# def enviar_texto(texto):
#     ser.write(texto.encode('utf-8'))

# # Convertir texto en voz y enviar a Arduino
# texto = "Hola, soy una voz generada por Python"
# engine.say(texto)
# engine.runAndWait()
# enviar_texto(texto)
