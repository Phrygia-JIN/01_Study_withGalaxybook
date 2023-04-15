# 감리 구분
# 주가가 단기간에 급등, 증권거래소에 의해 「요주의」주식으로 분류된 종목을 감리종목이라 합니다. 
# 감리종목은 최근 6일간 주가상승폭이 가격제한폭(상한가)의 5배를 초과하거나 최근 12일간의 주가 상승폭이 가격제한폭의 8배를 넘어서는 상태가 3일간 지속될 경우 감리종목으로 지정
from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

Cons = kiwoom.GetMasterConstruction("005930")
print(Cons)