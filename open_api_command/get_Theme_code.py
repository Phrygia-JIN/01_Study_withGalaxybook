from pykiwoom.kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

tickers = kiwoom.GetThemeGroupCode('141')
pprint.pprint(tickers)

for ticker in tickers:
    name = kiwoom.GetMasterCodeName(ticker)
    print(ticker, name)