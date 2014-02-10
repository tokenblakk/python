__author__ = 'Tramel Jones'
#Mtn Dew advertisement text messaging app

import requests
#target number
class Dew2():
    def __init__(self):
        self.sendto= '+17087688139'
        self.from_= '+14086101534'#12192303780

    def dewit(self, sendto = None):
        if sendto is None:
            sendto= self.sendto
        payload = {'From':self.from_, 'To':sendto, 'Body':'Mtn Dew is for me and you.  http://i.imgur.com/2Ezv4RO.jpg'}
        r = requests.post('https://api.twilio.com/2010-04-01/Accounts/AC258ed2b725533f944e2e8aaf60d30cd7/Messages', data=payload, auth=('AC258ed2b725533f944e2e8aaf60d30cd7', 'e7dcf4042a058b5348387375989a81ed'))
        print(r.text)

#Dew = Dew2()
#Dew.dewit()

#pi@raspberrypikachu ~ $ alias textme="python -c 'import Dew2; doodoo=Dew2.Dew2(
#'7087688139')'"