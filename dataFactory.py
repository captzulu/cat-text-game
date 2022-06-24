import constants
import importlib
import json
class dataFactory(object):
    def loadData(name):
        json_file = open(constants.DATA_PATH + '/' + name + '.json', encoding='utf-8')
        return json.load(json_file)
    
    def dictFromJson(className):
        jsonFileName = className + 's'
        return dataFactory.loadData(jsonFileName)
    
    def initClass(className, obj):
        module = importlib.import_module('dataObjects.' + className)
        returnClass = getattr(module, className.capitalize())
        return returnClass(**obj)

    def loadClassDict(className):
        dict_loaded = dataFactory.dictFromJson(className)
        classes_dict = {}
        for key, item in dict_loaded.items():
            classes_dict.update([(key,dataFactory.initClass(className, item))])
        return classes_dict