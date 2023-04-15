import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import pythoncom

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # login = login_ocx()
        # login.login()

        self.kiwoom = Kiwoom()
        self.kiwoom.CommConnect()
        name = self.kiwoom.GetMasterCodeName("005930")
        print(name)

        # tr request
        self.kiwoom.SetInputValue("종목코드", "005930")
        self.kiwoom.CommRqData("opt10001", "opt10001", 0, "0101")

# 로그인
class login_ocx():        
    def login(self):
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.dynamicCall("CommConnect()")
        self.ocx.OnEventConnect.connect(self.OnEventConnect)
    def OnEventConnect(self, err_code):
        print(err_code)

# 메소드
class Kiwoom:
    def __init__(self):
        self.login = False
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self.OnEventConnect)

    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        while not self.login:
            pythoncom.PumpWaitingMessages()

    def GetMasterCodeName(self, code):
        name = self.ocx.dynamicCall("GetMasterCodeName(QString)", code)
        return name
    
    def OnEventConnect(self, err_code):
        self.login = True
    
    def SetInputValue(self, id, value):
        self.ocx.dynamicCall("SetInputValue(Qstring, Qstring)", id, value)

    def CommRqData(self, rqname, trcode, next, screen):
        self.ocx.dynamicCall("CommRqData(Qstring, Qstring, int, Qstring)", rqname, trcode, next, screen)

    def GetCommData(self, trcode, rqname, index, item):
        data = self.ocx.dynamicCall("GetCommData(QString, QString, int, Qstring)", trcode, rqname, index, item)
        return data.strip()


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
