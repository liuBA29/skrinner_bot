import requests
import  asyncio

def get_tickers():
    url = 'https://api.bybit.com/v5/market/tickers'
    params = {'category': 'linear'}
    response = requests.get(url=url, params=params)
    return response.json()['result']['list']

async def monitoring():
    tickers = get_tickers()
    for ticker in tickers:
        print(ticker)
        symbol = ticker['symbol']


if __name__ == '__main__':
    asyncio.run(monitoring())
