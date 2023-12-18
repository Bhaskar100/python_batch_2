import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import yfinance as yf

# Date must be in the fromat ("%Y-%m-%d") That is, year-month-day
start_date = '2022-12-1' #1 December 2020
end_date = '2023-12-12'    #2 February 2023
# "start_date" must be an older date than the "end_date"

amazon = yf.download(tickers = "AMZN",
                  start = start_date,
                  end = end_date)
print(amazon)

aapl = yf.download(tickers = "AAPL",
                  start = start_date,
                  end = end_date)

amazon.head()
aapl.head()
amazon.reset_index(inplace=True)
aapl.reset_index(inplace=True)
amazon.head()
aapl.head()
plt.figure(figsize=(14,5))
sns.set_style("ticks")
sns.lineplot(data=amazon,x="Date",y='Close',color='firebrick')
sns.lineplot(data=aapl,x="Date",y='Close',color='blue')
sns.despine()
plt.title("The Stock Price of Amazon",size='x-large',color='blue')
plt.show()
