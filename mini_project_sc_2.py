import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import yfinance as yf

# Date must be in the fromat ("%Y-%m-%d") That is, year-month-day
start_date = '2023-07-01' #1 December 2020
end_date = '2023-09-30'    #2 February 2023
# "start_date" must be an older date than the "end_date"

amazon = yf.download(tickers = "AMZN",
                  start = start_date,
                  end = end_date)
aapl = yf.download(tickers = "AAPL",
                  start = start_date,
                  end = end_date)

amazon.head()
aapl.head()
amazon.reset_index(inplace=True)
aapl.reset_index(inplace=True)
amazon.head()
aapl.head()
aapl['Daily_Return'] = aapl['Adj Close'].pct_change()
amazon['Daily_Return'] = amazon['Adj Close'].pct_change()

plt.figure(figsize=(14,5))
sns.set_style("ticks")

sns.scatterplot(x=aapl.index, y='Daily_Return',data=aapl['Daily_Return'],color='blue')
plt.show()