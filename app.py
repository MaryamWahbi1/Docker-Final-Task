# Import libraries
import time
import datetime
import redis
from flask import Flask, redirect, url_for, render_template, request, flash
import json
import requests

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

#  get current time
current_time = datetime.datetime.now()
#  get current date
curr_date = current_time.strftime("%d/%m/%Y %H:%M:%S")

# function that return the current BitCoin price
def Current_BitCoin_Price():
    # Defining Binance API URL
    key = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = (requests.get(key))
    # requesting data from url
    data = response.json()
    price = data['bpi']["USD"]['rate']
    return ""+str(curr_date)+" --> "+str(price)+"$"

# function that return the average price for the last 10 minutes
def Price_Avg():
    # Defining Binance API URL
    key = "https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10"
    response = (requests.get(key))
    data = response.json()
    prices =[]   
    #last 10 minutes
    t = 10
    # running loop to print all crypto prices in the last 10 minutes
    for i in range(t):
        price = data['Data']["Data"][i]['close']
        prices.append(price)
             
    price_len = len(prices)
    price_sum = sum(prices)
    #the Average Price for the last 10 minutes
    average = price_sum / price_len 
    #return the average price for the last 10 minutes
    return "Average "+" --> "+str(average)+"$"

@app.route('/')
def hello():
    count = Price_Avg()
    return render_template('index.html',first_text=Current_BitCoin_Price(),second_text=Price_Avg())