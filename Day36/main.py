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
with open('../../../Dropbox/100DaysOfPython_PRIVATE/Day36Creds.txt') as file:
    creds_str = file.read()
    creds = ast.literal_eval(creds_str)

# Save tokens as variables
STOCK_KEY = creds['ALPHA_VANTAGE_API']
NEWS_KEY = creds['NEWS_API']
TWILIO_KEY = creds['TWILIO_API']
TWILIO_NUMBER = creds['TWILIO_NUMBER']
ACCOUNT_SID = creds['ACCOUNT_SID']
AUTH_TOKEN = creds['AUTH_TOKEN']
MY_NUMBER = creds['TOMS_NUMBER']

for key, value in creds.items():
    print(key, value)

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
abs_change = abs((previous2_close - previous_close)/previous2_close)*100

####################################################################################
# STEP 2: Fetch top three articles that mention the company
# Use https://newsapi.org/docs/endpoints/everything

# Call Alpha Vantage API to get stock data from previous 100 days
today = dt.datetime.today().strftime('%Y-%m-%d')
news_url = f'{NEWS_ENDPOINT}?q={COMPANY_NAME.lower()}&from={today}&sortBy=publishedAt&apiKey={NEWS_KEY}'
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
    # top_three_articles += f'Title: {article["title"]}\nURL: {article["url"]}\nSnippet:{article["content"]}\n\n'
    top_three_articles += f'Title: {article["title"]}\nURL: {article["url"]}\n\n'

print(top_three_articles)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.


# Send SMS if it will rain
delta_five = True
client = Client(ACCOUNT_SID, AUTH_TOKEN)

if delta_five:
    message = client.messages \
                    .create(
                         body=top_three_articles,
                         from_=TWILIO_NUMBER,
                         to=MY_NUMBER
                     )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

