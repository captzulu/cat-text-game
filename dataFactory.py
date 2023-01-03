import constants
import importlib
import json

class dataFactory(object):
    @staticmethod
    def dictFromJson(name : str, className: object) -> dict[str, object]:
        json_file = open(constants.DATA_PATH + '/' + name + "s" + '.json', encoding='utf-8')
        return json.load(json_file, object_hook=lambda d: dataFactory.decoder(d, className))
    
    @staticmethod
    def decoder(object : dict, className):
        if isinstance(list(object.values())[0], className):
            return object
        return className(**object)
    
    @staticmethod
    def getClass(className) -> object:
        module = importlib.import_module('dataObjects.' + className)
        cls = className[0].capitalize() + className[1:]
        return getattr(module, cls)
    
    @staticmethod
    def loadClassDictTest(className : str) -> dict[str, object]:
        return dataFactory.dictFromJson(className + "Test", dataFactory.getClass(className))

    @staticmethod
    def loadClassDict(className : str) -> dict[str, object]:
        return dataFactory.dictFromJson(className, dataFactory.getClass(className))