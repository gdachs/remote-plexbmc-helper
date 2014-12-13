class __window__():

    def __init__(self):
        self.__properties__ = {}
        self.__properties__['plexbmc.nowplaying.server'] = 'microserver:32400'
        self.__properties__['plexbmc.nowplaying.id'] = '1'

    def getProperty(self, key):
        return self.__properties__[key]

    def setProperty(self, key, value):
        self.__properties__[key] = value

def Window(windowId):
    return __window__()
