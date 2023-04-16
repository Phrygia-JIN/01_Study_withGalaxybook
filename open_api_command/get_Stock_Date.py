from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

stock_date = kiwoom.GetMasterListedStockDate("005930")
print(stock_date)
print(type(stock_date))