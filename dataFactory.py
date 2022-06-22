import constants
from type import Type
import json
class dataFactory(object):
    def loadData(name):
        json_file = open(constants.DATA_PATH + '/' + name + '.json')
        return json.load(json_file)

    def loadTypes():
        types_loaded = dataFactory.loadData('types')
        types = []
        for type in types_loaded:
            types.append(Type(**type))
        return types