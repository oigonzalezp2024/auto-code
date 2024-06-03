
from os import mkdir

class AutoCode:

    def generate(self, nameClass:str, campos:list):
        try:
            mkdir("./project")
            mkdir("./project/core")
            mkdir("./project/core/Interfaces")
            mkdir("./project/core/Abstracts")
            mkdir("./project/core/Entity")
            mkdir("./project/core/Interfaces/Interface"+str(nameClass).capitalize())
            mkdir("./project/core/Abstracts/Abstract"+str(nameClass).capitalize())
            mkdir("./project/core/Entity/"+str(nameClass).capitalize())            
        except:
            try:
                mkdir("./project/core/Interfaces/Interface"+str(nameClass).capitalize())
                mkdir("./project/core/Abstracts/Abstract"+str(nameClass).capitalize())
                mkdir("./project/core/Entity/"+str(nameClass).capitalize())            
            except:
                pass

        self.createInterface(nameClass, campos)
        self.createAbstract(nameClass, campos)
        self.createEntity(nameClass, campos)

    def createInterface(self, nameClass:str, campos:list):
        f = open('./AutoCode/core/Interfaces/Interface.py','r')
        content = f.read()
        f.close()
        
        f = open('./AutoCode/core/Interfaces/InterfaceMyClass/InterfaceMyClass.py','r')
        content2 = f.read()
        f.close()
        
        cont1 = content.replace("MyClass", str(nameClass).capitalize())
        content2 = content2.replace(content, "")
        metodos = ""
        parametrosConstructor = ""
        atributos = ""
        for campo in campos:
            metodos += content2.replace(content, "").replace("Method", "_"+str(campo)).replace(", _"+str(campo), ", "+str(campo))
            parametrosConstructor += str(campo)+":str='', "
            atributos += "    "+str(campo)+" = str()\n"
        cont = cont1 + metodos

        f = open("./project/core/Interfaces/Interface"+str(nameClass).capitalize()+"/Interface"+str(nameClass).capitalize()+".py",'w')
        f.write(cont.replace("def __init__(self, Method:str):", "def __init__(self, "+parametrosConstructor[:-2]+"):").replace("    Method = str()", atributos[:-1]))
        f.close()

    def createAbstract(self, nameClass:str, campos:list):

        f = open('./AutoCode/core/Abstracts/Abstract.py','r')
        content = f.read()
        f.close()
        
        f = open('./AutoCode/core/Abstracts/AbstractMyClass.py','r')
        content2 = f.read()
        f.close()

        cont1 = content.replace("MyClass", str(nameClass).capitalize())
        content2 = content2.replace(content, "")
        metodos = ""
        parametrosConstructor = ""
        atributos = ""
        for campo in campos:
            metodos += content2.replace(content, "").replace("Method", "_"+str(campo)).replace(", _"+str(campo), ", "+str(campo))
            parametrosConstructor += str(campo)+":str='', "
            atributos += "    "+str(campo)+" = str()\n"
        cont = cont1 + metodos

        f = open("./project/core/Abstracts/Abstract"+str(nameClass).capitalize()+"/Abstract"+str(nameClass).capitalize()+".py",'w')
        f.write(cont.replace("def __init__(self, Method:str):", "def __init__(self, "+parametrosConstructor[:-2]+"):").replace("    Method = str()", atributos[:-1]))
        f.close()

    def createEntity(self, nameClass:str, campos:list):

        f = open('./AutoCode/core/Entity/MyClass.py','r')
        content = f.read()
        f.close()
        
        f = open('./AutoCode/core/Entity/EntityMyClass.py','r')
        content2 = f.read()
        f.close()

        cont1 = content.replace("MyClass", str(nameClass).capitalize())
        # variables en el constructor - inicio

        contenidoCostructor = ""
        conts = []
        
        for campo in campos:
            cont = str("        ")+content2.replace(content, "").replace("Method", "_"+str(campo)).replace(", _"+str(campo), ", "+str(campo)).replace("self._", "self.").replace(" = _", " = ").replace("def set_"+str(campo)+"(self, "+str(campo)+":str):", "").replace("    def get_"+str(campo)+"(self)->str:", "").replace("        return self."+str(campo)+"", "").replace("        ", "").replace("    ", "").replace("\n", "")+str("\n")
            contenidoCostructor += cont
            conts.append(cont)
        # variables en el constructor - fin
        cont4 = content2.replace(content, "").replace("Method", "_id_usuario").replace(", _id_usuario", ", id_usuario").replace("self._", "self.").replace(" = _", " = ")
        cont5 = content2.replace(content, "").replace("Method", "_nombre").replace(", _nombre", ", nombre").replace("self._", "self.").replace(" = _", " = ")
        cont = cont1 + contenidoCostructor + cont4 + cont5
        f = open("./project/core/Entity/"+str(nameClass).capitalize()+str("/")+str(nameClass).capitalize()+".py",'w')
        f.write(cont.replace("def __init__(self, Method:str):", "def __init__(self, id_usuario:str='', nombre:str=''):").replace("\n        self.Method = Method", "").replace("    Method = str()", str(conts[0]).replace("        self.","    ").replace(" = id_usuario"," = str()") + str(conts[1]).replace("        self.","    ").replace(" = nombre"," = str()")).replace("\n    def __init__(self,","    def __init__(self,"))
        f.close()

    def createEntity(self, nameClass:str, campos:list):

        f = open('./AutoCode/core/Entity/MyClass.py','r')
        content = f.read()
        f.close()
        
        f = open('./AutoCode/core/Entity/EntityMyClass.py','r')
        content2 = f.read()
        f.close()

        cont1 = content.replace("MyClass", str(nameClass).capitalize())
        content2 = content2.replace(content, "")
        metodos = ""
        parametrosConstructor = ""
        atributos = ""
        contt = ""
        for campo in campos:
            contt += str("        ")+content2.replace(content, "").replace("Method", "_"+str(campo)).replace(", _"+str(campo), ", "+str(campo)).replace("self._", "self.").replace(" = _", " = ").replace("def set_"+str(campo)+"(self, "+str(campo)+":str):", "").replace("    def get_"+str(campo)+"(self)->str:", "").replace("        return self."+str(campo)+"", "").replace("        ", "").replace("    ", "").replace("\n", "")+str("\n")
            metodos += content2.replace(content, "").replace("Method", "_"+str(campo)).replace(", _"+str(campo), ", "+str(campo)).replace("self._", "self.").replace(" = _", " = ")
            parametrosConstructor += str(campo)+":str='', "
            atributos += "    "+str(campo)+" = str()\n"
        cont = cont1 + contt + metodos

        f = open("./project/core/Entity/"+str(nameClass).capitalize()+"/"+str(nameClass).capitalize()+".py",'w')
        f.write(cont.replace("def __init__(self, Method:str):", "def __init__(self, "+parametrosConstructor[:-2]+"):").replace("    Method = str()", atributos[:-1]).replace("\n        self.Method = Method", ""))
        f.close()
