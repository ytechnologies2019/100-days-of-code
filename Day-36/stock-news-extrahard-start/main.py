from http.client import responses
import requests

STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
API_KEY = ''


STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tsla Inc'
#ABXYNKABSE8J4EZL

## STEP 1: Use https://www.alphavantage.co
stock_parameters = {
    'function' : 'TIME_SERIES_DAILY' ,
    'symbol': STOCK_NAME ,
    'apikey': API_KEY,
}

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response  = requests.get(STOCK_ENDPOINT,stock_parameters)
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']
print(yesterday_closing_price)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

## STEP 3: Find the Positive difference between 1 and 2
different = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
print(different)

# STEP Workout the Percentage
different_percentage = different / float(yesterday_closing_price)
print(different_percentage)


