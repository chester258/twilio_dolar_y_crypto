import pandas as pd
from tqdm import tqdm
from twilio_conf import *
import requests
from datetime import datetime
from twilio.rest import Client


def get_date():

    input_date = datetime.now()
    input_date = input_date.strftime("%Y-%m-%d")

    return input_date

def request_dolar():
    api_dolar = 'https://api.bluelytics.com.ar/v2/latest'

    try :
        response = requests.get(api_dolar).json()
    except Exception as e:
        print(e)

    return response
    

def get_dolar(response):
    fecha = response['last_update'].split('T')[0]
    dolar_blue_compra = response['blue']['value_buy']
    dolar_blue_venta = response['blue']['value_sell']

    return fecha, dolar_blue_compra, dolar_blue_venta



def create_df_dolar(data):
    col = ['Fecha','Compra','Venta']
    df = pd.DataFrame(data,columns=col)
    df.set_index('Fecha',inplace=True)

    return df




def request_cripto():
    api_cripto = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false&locale=en'

    try :
        response = requests.get(api_cripto).json()
    except Exception as e:
        print(e)

    return response




def get_cripto(response,i):
    nombre = response[i]['name']
    precio = round(response[i]['current_price'],2)
    rank = response[i]['market_cap_rank']


    return nombre,precio,rank


def create_df_cripto(data):
    col = ['Nombre','Precio usd','Ranking']
    df = pd.DataFrame(data,columns=col)

    return df




def send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,dolar,cripto):
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN

    client = Client(account_sid, auth_token)

    mensage = client.messages \
        .create(
            body= '\nHola Admin ! \n\n\n El dolar en Argentina es de:\n\n '+str(dolar) +' \n\n\n Y aca el resumen de las cryptos: \n\n '+str(cripto), 
            from_=PHONE_NUMBER,
            to='+543517624070')
    
    return mensage.sid




