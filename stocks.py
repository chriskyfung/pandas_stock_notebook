from datetime import date, timedelta
import json
import pandas as pd
import pandas_datareader as pdr

class stock_profile:
  def __init__(self, fpath=None):
    self.listing = {}
    self.name_dict = {}
    self.dataframes = {}
    if fpath:
      self.loadJsonProfile(fpath)

  def loadJsonProfile(self, fpath):
    with open(fpath) as f:
      jsondata = json.load(f)
    self.listing = dict((k.lower(), v) for k, v in jsondata['listing'].items())
    self.name_dict = dict((k, v.lower()) for k, v in jsondata['name_dict'].items())

  def name2code(self, stock_name):
    try:
      return self.name_dict[stock_name]
    except:
      return None

  def code2name(self, stock_code):
    try:
      return self.listing[stock_code]
    except:
      return ''
  
  def cacheFromYahooData(self, stock_codes, start_date, end_date=None):
    if end_date == None:
      end_date = date.today()
    for s in stock_codes:
      df = pdr.DataReader(s, 'yahoo', start_date, end_date)
      self.dataframes[s] = df.copy()
      stock_name = self.code2name(s)
      print(f'{stock_name}({s}):')
      display(df)
      print('\n')

