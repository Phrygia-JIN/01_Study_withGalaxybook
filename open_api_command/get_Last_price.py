from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

last_price = kiwoom.GetMasterLastPrice("005930")
print(int(last_price))
print(type(last_price))