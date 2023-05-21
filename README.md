# twilio_dolar_y_crypto
Envio diario del precio del dolar en argentina y del top 10 criptomonedas

Es un proyecto de practica, donde basicamente automatizo la llegada de un mensaje diario a mi celular, en este caso del precio del dolar en argentina y el precio de las 
las primeras 10 criptomonedas(un ranking basado en el capital del mercado de cada moneda).

Herramientas:
-Twilio
-Python
-ubuntu
-AWS

-Con twilio compre un numero de celular con el que voy a mandar el mensaje 

-Con python me conecte a la libreria de twilio, me conecte a las distintas APIS (de donde extraigo la informacion del precio del dolar y las criptos), y 
cree el codigo para una ves extraida y trabajada la informacion, mandar el mensaje final, con la informacion requerida, desde el numero de twilio.

-Con AWS creo una instancia de EC2 donde, con ubuntu, automatizo este proceso diariamente.



