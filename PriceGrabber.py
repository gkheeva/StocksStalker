__author__ = 'gkheeva'

from yahoo_finance import Share

class PriceGrabber:

    def getStock(self, share):
        stock = Share(share)
        return stock

if __name__ == '__main__':
   priceGrabber = PriceGrabber()
   apple = priceGrabber.getStock("AAPL")
   appleOpenPrice = apple.get_open()

   print(appleOpenPrice)