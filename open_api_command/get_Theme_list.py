from pykiwoom.kiwoom import *
import pprint # 데이터 보기 좋게 출력

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

group = kiwoom.GetThemeGroupList(1) # dict 형식
pprint.pprint(group)

print(group['화장품'])