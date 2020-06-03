import requests, quoteAPI

def main():
    tupl = quoteAPI.getQuoteWithKeyword("bottle")
    print('"' + tupl[0] + '" ' + tupl[1])

if __name__ == "__main__":
    main()
