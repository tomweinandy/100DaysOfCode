"""
Day 36: Stock Activity Monitor
"""
import ast
import requests
import datetime as dt
from twilio.rest import Client

# Save variables
STOCK = "AMZN"
COMPANY_NAME = "Amazon"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Read in credential string and save as a dictionary
with open('../../../../Dropbox/100DaysOfCodePRIVATE/Day36Creds.txt') as file:
    creds_str = file.read()
    creds = ast.literal_eval(creds_str)

# Save tokens as variables
STOCK_KEY = creds['ALPHA_VANTAGE_API']
NEWS_KEY = creds['NEWS_API']
TWILIO_KEY = creds['TWILIO_API']
TWILIO_NUMBER = creds['TWILIO_NUMBER']
ACCOUNT_SID = creds['ACCOUNT_SID']
MY_NUMBER = creds['TOMS_NUMBER']

for key, value in creds.items():
    print(key, value)


# Helper function
def triangle_icon(n: float):
    if n > 0:
        return '🔺'
    elif n < 0:
        return '🔻'
    else:
        return 'NC'


####################################################################################
# STEP 1: Identify when a stock changes by 5% or more
# Use https://www.alphavantage.co/documentation/

# Call Alpha Vantage API to get stock data from previous 100 days
stock_url = f'{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_KEY}'
response = requests.get(stock_url)

# Print status, return data
print('Stock response status code:', response.status_code)
response.raise_for_status()
stock_data = response.json()

# Parse data
stocks = stock_data['Time Series (Daily)']
day_list = []
for key, value in stocks.items():
    day_list.append(key)

# Get previous two days' closing price
previous_day = stocks[day_list[0]]
previous2_day = stocks[day_list[1]]

previous_close = float(previous_day['4. close'])
previous2_close = float(previous2_day['4. close'])

# Calculate the absolute percent change
percent_change = 100*(previous2_close - previous_close)/previous2_close

# Determine of the absolute change was more than 5%
big_delta = abs(percent_change) >= 5

####################################################################################
# STEP 2: Fetch top three articles that mention the company
# Use https://newsapi.org/docs/endpoints/everything

# Call Alpha Vantage API to get stock data from previous 100 days
today = dt.datetime.today().strftime('%Y-%m-%d')
news_url = f'{NEWS_ENDPOINT}?q={COMPANY_NAME.lower()}&from={today}&sortBy=publishedAt&apiKey={NEWS_KEY}&language=en'
response = requests.get(news_url)

# Print status, return data
print('News response status code:', response.status_code)
response.raise_for_status()
news_data = response.json()
news = news_data['articles']

# Save select info from top three articles
top_three_articles = ''
for i in range(0, 3):
    article = news[i]
    top_three_articles += f'Title: {article["title"]}\nURL: {article["url"]}\nBrief:{article["description"]}\n\n'
print(top_three_articles)

####################################################################################
# STEP 3: Send a text of top three articles if the stock changes by 5% or more
# Use twilio.com/docs/sms/quickstart/python

# Build text of alert
icon = triangle_icon(percent_change)
pct_change = round(percent_change, 1)
message_body = f'\n{STOCK}: {icon}{pct_change}% {top_three_articles}'

# Send out SMS with top three articles
big_delta = True  # uncomment to test
client = Client(ACCOUNT_SID, TWILIO_KEY)
if big_delta:
    message = client.messages \
                    .create(
                         body=message_body,
                         from_=TWILIO_NUMBER,
                         to=MY_NUMBER
                     )
