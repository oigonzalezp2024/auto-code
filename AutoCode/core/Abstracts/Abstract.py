
from abc import abstractmethod
from core.Interfaces.InterfaceMyClass.InterfaceMyClass import InterfaceMyClass

class AbstractMyClass(InterfaceMyClass):

    Method = str()
    
    @abstractmethod
    def __init__(self, Method:str):
        pass