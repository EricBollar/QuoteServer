import requests
from os import path

def isServer():
    basepath = path.dirname(__file__)
    filepath = format(path.abspath(basepath))+"/../"+"is_server.txt"
    f = open(filepath, "r")
    return (f.readline(1) == "1")

# reads the api key from the txt file
def getKey():
    basepath = path.dirname(__file__)
    filepath = format(path.abspath(basepath))+"/../"+"apikey.txt"
    f = open(filepath, "r")
    return f.readline(24)

def getQuoteWithUserInput():
    txt = input("Type something to test this out: ")
    getQuote(txt)
    
def getQuote(txt):
    url = 'https://quotes.rest/quote/search?query=' + txt

    api_token = getKey()

    headers = {'content-type': 'application/json',
        'X-TheySaidSo-Api-Secret': format(api_token)}

    author = None
    while (author == None):
        response = requests.get(url, headers=headers)
        #print(response)
        quote=response.json()['contents']['quotes'][0]['quote']
        author=response.json()['contents']['quotes'][0]['author']
    return '"' + quote + '" ' + author
