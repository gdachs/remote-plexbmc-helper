class addon:
    def __init__(self):
        self.__addonInfo__ = {}
        self.__addonInfo__['path'] = '.'
        self.__addonInfo__['version'] = '0.0.1'
        self.__addonInfo__['profile'] = ''
        self.__settings__ = {}
        self.__settings__['debug'] = 'true'
        self.__settings__['gdm_debug'] = '1'
        self.__settings__['use_xbmc_name'] = None
        self.__settings__['c_name'] = 'Mock PLEXBMC Helper'
        self.__settings__['uuid'] = '7ff5d6d0-7a69-11e4-82f8-0800200c9a66'
        self.__settings__['myplex_user'] = ''

    def getAddonInfo(self, key):
        return self.__addonInfo__[key]

    def setSetting(self, key, value):
        self.__settings__[key] = value

    def getSetting(self, key):
        return self.__settings__[key]

def Addon(name = 'plugin.video.plexbmc'):
    return addon()

