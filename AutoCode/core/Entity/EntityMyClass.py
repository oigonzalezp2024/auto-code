
from core.Abstracts.AbstractMyClass.AbstractMyClass import AbstractMyClass

class MyClass(AbstractMyClass):

    Method = str()

    def __init__(self, Method:str):
        self.Method = Method
    
    def setMethod(self, Method:str):
        self.Method = Method

    def getMethod(self)->str:
        return self.Method
