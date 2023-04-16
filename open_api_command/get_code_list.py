from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
etf = kiwoom.GetCodeListByMarket('8')

print(len(kospi), kospi)
print(len(kosdaq), kosdaq)
print(len(etf), etf)

"""
코스피 = 0
ELW = 3
뮤추얼펀드 = 4
신주인수권 = 5
리츠 = 6
ETF = 8
하이얼펀드 = 9
코스닥 = 10
K-OTC = 30
코넥스 = 50

"""