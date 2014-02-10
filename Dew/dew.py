__author__ = 'token_000'
import sys
sys.path.insert(0, '/usr/local/lib/python3.2/site-packages')
from twilio.rest import TwilioRestClient

# put your own credentials here
id = "AC258ed2b725533f944e2e8aaf60d30cd7"
auth = "e7dcf4042a058b5348387375989a81ed"

client = TwilioRestClient(id, auth)

message = client.messages.create(body="Mtn Dew is for me and you.",
        to="+7087688139",
        from_="+12192303780")
print(message.sid)
