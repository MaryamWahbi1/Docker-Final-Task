# Docker Final Task
### Explanation of the task

1. Create a Python Web APP (use either Flask or FastAPI libraries) that:
- Presents the Current BitCoin Price
- Stores the price in a Redis Database
- Presents the Average Price for the last 10 minutes
2. Dockerize the applications (Create Dockerfile and docker-compose.yml)

3. Create a Jenkinsfile for CI/CD that creates and pushes the generated Web application Docker image to Docker Hub.

------------


### Step 1: Define the application dependencies
#### 1. Create a directory for the project:
```shell
mkdir HW4
cd HW4
```
#### 2. Create a file called app.py my project directory:
```python
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
```
#### 3. Create another file called requirements.txt in project directory:
```
flask
redis
requests

```

------------


### Step 2: Create a Dockerfile
```
# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

------------


### Step 3: Define services in a Compose file
```
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:5000"
  redis:
    image: "redis:alpine"
```

------------


### Step 4: Build and run your app with Compose
1. Running docker compose up.

[![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/docker_compose_up.PNG?raw=true)](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/docker_compose_up.PNG?raw=true)

2. Enter http://localhost:8000/ in a browser to see the application running

[![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/BitCoin_Price_HTML.PNG?raw=true)](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/BitCoin_Price_HTML.PNG?raw=true)

------------


# dockerhub 
[![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/Dockerhub.PNG?raw=true)](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/Dockerhub.PNG?raw=true)


[![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/docker_pull.PNG?raw=true)](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/docker_pull.PNG?raw=true)


[![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/docker_images.PNG?raw=true)](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/docker_images.PNG?raw=true)

[![](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/curl.PNG?raw=true)](https://github.com/MaryamWahbi1/Docker-Final-Task/blob/master/screenshots/curl.PNG?raw=true)

