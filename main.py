import requests

def main():
    txt = input("Type something to test this out: ")
    url = 'https://quotes.rest/quote/search?query=' + txt
    api_token = "6uvWDTpksQPjIeRxmCBQWAeF"
    headers = {'content-type': 'application/json',
        'X-TheySaidSo-Api-Secret': format(api_token)}

    response = requests.get(url, headers=headers)
    #print(response)
    quote=response.json()['contents']['quotes'][0]['quote']
    author=response.json()['contents']['quotes'][0]['author']
    print('"' + quote + '" ' + author)

if __name__ == "__main__":
    main()