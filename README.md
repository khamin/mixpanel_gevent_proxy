# About

[Mixpanel](http://mixpanel.com) [Gevent](http://gevent.org) Proxy is a fast async UDP-based requests forwarder.

# Install

From PyPi:

	$ pip install mixpanel_gevent_proxy

or manually from github repository:

	$ git clone git://github.com/khamin/mixpanel_gevent_proxy.git
	$ cd mixpanel_gevent_proxy
	$ python setup.py install

# How to Run

	$ mixpanel_gevent_proxy

Run in background:

	$ mixpanel_gevent_proxy &

More options:

	$ mixpanel_gevent_proxy --help

# UDP Consumer Example

All you need is to send JSON serialized array [endpoint, json_message] UDP datagram. Example:

```python
import socket
import json

from mixpanel import Mixpanel


class UDPConsumer (object):
	def __init__ (self, ip='127.0.0.1', port=8051):
		self.ip = ip
		self.port = port

	def send (self, endpoint, json_message):
		msg = json.dumps([endpoint, json_message])

		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(msg, (self.ip, self.port))

mp = Mixpanel(
	token='YOUR_TOKEN',
	consumer=UDPConsumer(),
)
```

Have fun!
