import constants
import importlib
import json
class dataFactory(object):
    @staticmethod
    def loadData(name : str) -> dict[str, object]:
        json_file = open(constants.DATA_PATH + '/' + name + '.json', encoding='utf-8')
        return json.load(json_file, parse_int=None)
    
    @staticmethod
    def dictFromJson(className : str) -> dict[str, object]:
        jsonFileName = className + 's'
        return dataFactory.loadData(jsonFileName)
    
    @staticmethod
    def initClass(className : str, obj : object):
        module = importlib.import_module('dataObjects.' + className)
        className = className[0].capitalize() + className[1:]
        returnClass = getattr(module, className)
        return returnClass(**obj)

    @staticmethod
    def loadClassDict(className : str) -> dict[str, object]:
        dict_loaded = dataFactory.dictFromJson(className)
        classes_dict : dict[str, object] = {}
        for key, item in dict_loaded.items():
            classes_dict.update([(key, dataFactory.initClass(className, item))])
        return classes_dict
    
    @staticmethod
    def loadClassDictTest(className : str) -> dict[str, object]:
        dict_loaded = dataFactory.dictFromJson(className + 'Test')
        classes_dict : dict[str, object] = {}
        for key, item in dict_loaded.items():
            classes_dict.update([(key, dataFactory.initClass(className, item))])
        return classes_dict