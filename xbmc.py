import httplib
import time
import os

abortRequested = False

def translatePath(profile):
    return profile

def getCondVisibility(platform):
    if platform == 'system.platform.linux':
        return True 
    return False

def executebuiltin(command):
    print command

def executeJSONRPC(request):
    headers = {"Content-type": "application/json", "Accept": "text/plain"}
    # conn = httplib.HTTPConnection("openelec")
    # conn = httplib.HTTPConnection("localhost:8080")
    conn = httplib.HTTPConnection("nuc:8080")
    try:
        conn.request("POST", "/jsonrpc", request, headers)
    except:
        return ""
    response = conn.getresponse()
    print request
    print response
    return response.read()

def sleep(milliseconds):
    time.sleep(milliseconds / 1000.0);

class Player:

    def play(self, media):
        # wol.send_magic_packet('C0:3F:D5:62:4C:55')
        os.system("etherwake 'C0:3F:D5:62:4C:55'")
        # os.system('kodi-send --host=localhost --action="CECActivateSource"')
        request = '{"id":1,"jsonrpc":"2.0","method":"Player.Open","params":{"item":{"file":"' + media + '"}}}'
        response = ""
        while response == "":
            response = executeJSONRPC(request)
