import requests
import schedule
import time
from requests_html import HTML, HTMLSession

class requestin:
  def __init__(self):
    self.url = 'https://wise.com/gb/currency-converter/gbp-to-inr-rate'

  def reminder(self):
    print('Will be updated in 5 minutes....')
    
  def get_time(self):
    r = requests.get(self.url)
    print(r.headers['Date'])
    
  def get_price(self): 
    session = HTMLSession()
    response = session.get(self.url)
    somthing = response.html.find('span.text-success',first=True).text
    somthing = float(somthing)
    print(round(somthing,2))

  def scheduling(self): 
    schedule.every().day.at("19:55:00").do(self.get_time)
    schedule.every().day.at("19:55:00").do(self.reminder)
    schedule.every().day.at("20:00:00").do(self.get_price)

    while True:
      schedule.run_pending()
      time.sleep(1)

requesting = requestin()
requesting.scheduling()
