from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  
  # gather info about source code elements
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])

  # bad practice to put print in function. Just for testing purposes.
  #print(content)
  #print(type(rate))

  return rate

current_rate = get_currency('EUR','AUD')
print(current_rate)