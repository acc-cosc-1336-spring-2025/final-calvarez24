#write functions here, don't add input('') statements here!
class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def get_stock_list():
    stocks = []
    stocks.append(Stock("AAPL", "Apple Inc"))
    stocks.append(Stock("CAT", "Caterpillar"))
    stocks.append(Stock("EK", "Eastman Kodak"))
    stocks.append(Stock("GOOG", "Google"))
    stocks.append(Stock("MSFT", "Microsoft"))
    return stocks 

def display_stock_list(stocks):
    for stock in stocks:
        print(f"Company Symbol: {stock.get_symbol()}")
        print(f"Company Name: {stock.get_company_name()}")
        print("-" * 20)
        