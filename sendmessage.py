__author__ = 'Tramel Jones'
#text messaging app

import requests
#target number
class SendMessage():
    def __init__(self):
        self.sendto= '+17087688139'
        self.from_= '+14086101534'#12192303780
        self.body = "Hello!"

    def send(self):
        payload = {'From':self.from_, 'To':self.sendto, 'Body':self.body}
        r = requests.post('https://api.twilio.com/2010-04-01/Accounts/AC258ed2b725533f944e2e8aaf60d30cd7/Messages', data=payload, auth=('AC258ed2b725533f944e2e8aaf60d30cd7', 'e7dcf4042a058b5348387375989a81ed'))
        #print(r.text)

    def setmessage(self, sendto = None, body= None):
        if sendto is not None:
            self.sendto = sendto
        if body is not None:
            self.body = body
        self.send()
