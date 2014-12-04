import httplib
import time
from wakeonlan import wol

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
   conn = httplib.HTTPConnection("openelec")
   conn.request("POST", "/jsonrpc", request, headers)
   response = conn.getresponse()
   print request
   print response.status, response.reason
   return response.read()

def sleep(milliseconds):
    time.sleep (milliseconds / 1000.0);

class Player:

   def play(self, media):
       #wol.send_magic_packet('C0:3F:D5:62:4C:55')
       request = '{"id":1,"jsonrpc":"2.0","method":"Player.Open","params":{"item":{"file":"' + media + '"}}}'
       executeJSONRPC(request)
