#model.py
#deals with app data and api calls
import requests

#API call

url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@{apiVersion}/{date}/{endpoint}"
response = requests.get(url_host)
sample_json = response.json()


def get_currencies():
    currency_strings = []

    #get 3 letter code and currency from currency map
    for code in url_host.keys():
      currency = url_host[code]
      currency_strings.append(code + " - " + currency)  
    return currency_strings

def get_currency_from_code(code):
    return url_host[code]

def get_currency_string(code):
    return code + " - " + get_currency_from_code(code)



endpoint = "" 
query = ""


currencies = get_currencies()
default_from = get_currency_string("usd")
default_to = get_currency_string("eur")


if __name__ == "__main__": 
    get_currencies()
    print(url_host)
