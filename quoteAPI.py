import requests

def getQuoteWithUserInput():
    txt = input("Type something to test this out: ")
    getQuote(txt)
    
def getQuote(txt):
    url = 'https://quotes.rest/quote/search?query=' + txt

    # reads the api key from the txt file
    f = open('/var/www/html/QuoteServer/apikey.txt', 'r')
    api_token = f.readline(24)

    headers = {'content-type': 'application/json',
        'X-TheySaidSo-Api-Secret': format(api_token)}

    author = None
    while (author == None):
        response = requests.get(url, headers=headers)
        #print(response)
        quote=response.json()['contents']['quotes'][0]['quote']
        author=response.json()['contents']['quotes'][0]['author']
    return '"' + quote + '" ' + author
