
from core.Abstracts.AbstractMyClass.AbstractMyClass import AbstractMyClass

class MyClass(AbstractMyClass):

    Method = str()

    def __init__(self, Method:str):
        self.Method = Method
