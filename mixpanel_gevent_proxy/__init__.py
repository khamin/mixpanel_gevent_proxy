# -*- coding: utf-8 -*-

import argparse

from json import loads
from mixpanel import Consumer

from gevent.monkey import patch_all
from gevent.server import DatagramServer

patch_all()


parser = argparse.ArgumentParser(
	description='''Mixpanel Gevent Proxy.
Send me JSON encoded [endpoint, json_message] UDP datagram and I will
forward it using default mixpanel consumer.''',
)

parser.add_argument(
	'-p', '--port',
	default=8051,
	type=int,
	help='UDP port listen to',
)


args = parser.parse_args()


class MixpanelProxy (DatagramServer):
	def handle (self, data, address):
		print('Got %r' % data)
		consumer = Consumer()
		consumer.send(*loads(data))


def main ():
	print('Runnig mixpanel gevent proxy on port %d.' % args.port)
	MixpanelProxy(':%d' % args.port).serve_forever()


if __name__ == '__main__':
	main()
