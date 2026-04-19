from datetime import date, timedelta
import json
import yfinance as yf
from IPython.display import display

class stock_profile:
  def __init__(self, fpath=None):
    self.listing = {} # A dict for storing the key-value pairs of stock codes and their preferred name
    self.name_dict = {} # A dict for storing the key-value pairs of stock names/aliases and their corresponding code
    self.dataframes = {} # A dict for mapping stock codes and their associated dataframes
    if fpath:
      self.loadJsonProfile(fpath) # Load profile data from the specified JSON file if the arg `fpath` is passed in the initialization
    return

  # Read the codes and names of a basket of stocks from a JSON-formatted file and map them to the `listing` and `name_dict` dictionary objects
  def loadJsonProfile(self, fpath):
    with open(fpath, encoding='utf-8') as f:
      jsondata = json.load(f)
    self.listing = dict((k.lower(), v.split(',',1)[0]) for k, v in jsondata['listing'].items())
    for k, v in self.listing.items():
      names = v.split(',')
      for n in names:
        self.name_dict[n.strip()] = k
    return

  # Find the stock code associated with a given name
  def name2code(self, stock_name):
    try:
      return self.name_dict[stock_name]
    except:
      return None

  # Get the preferred name of a specific stock
  def code2name(self, stock_code):
    try:
      return self.listing[stock_code]
    except:
      return ''
  
  # Cache the historical data from Yahoo Finance for a list of stocks as a dict of Pandas `dataframes`
  def cacheFromYfinance(self, stock_codes, start_date, end_date=None):
    if end_date == None:
      end_date = date.today()
    if isinstance(stock_codes,list):
      tickers = [s.upper() for s in stock_codes]
      df = yf.download(tickers, start=start_date, end=end_date)
      for s in stock_codes:
        # Extract the data for the stock
        stock_df = df.loc[:, (slice(None), s.upper())] # Use s.upper() to match the ticker in the multi-index
        # Remove the stock code from the column index
        stock_df.columns = stock_df.columns.droplevel(1)
        # Store the cleaned dataframe
        self.dataframes[s] = stock_df.copy()
        stock_name = self.code2name(s)
        print(f'{stock_name}({s}):')
        display(self.dataframes[s])
        print('\n')
    else:
      print('ERROR: Wrong type argument: list, stock_codes')
    return

  # Get all tickers from listing
  def getAllStockCodes(self):
    return list(self.listing.keys())
