from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

stock_state = kiwoom.GetMasterStockState("005930")
print(stock_state)