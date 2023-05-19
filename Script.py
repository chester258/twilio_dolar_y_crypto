
"""
************************************************************************
* Author = @chester258                                                *
* Date = '19/05/2023'                                                  *
* Description = Envio de mensajes Twilio con Python                    *
************************************************************************
"""

import pandas as pd
from tqdm import tqdm
from twilio_conf import *
import requests
from datetime import datetime
from Funciones import *

input_date = get_date()

response_dolar = request_dolar() 

dolar =[get_dolar(response_dolar)]

df_dolar = create_df_dolar(dolar)



response_cripto = request_cripto()

cripto = []

for i in tqdm(range(len(response_cripto)),colour='green'):
    cripto.append(get_cripto(response_cripto,i))


df_cripto = create_df_cripto(cripto)


message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df_dolar,df_cripto)


print('Mensaje Enviado con exito ' + message_id)

