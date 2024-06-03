
from abc import ABCMeta, abstractmethod

class InterfaceMyClass(metaclass=ABCMeta):

    Method = str()

    @abstractmethod
    def __init__(self, Method:str):
        pass
    
    @abstractmethod
    def setMethod(self, Method:str):
        pass

    @abstractmethod
    def getMethod(self)->str:
        pass