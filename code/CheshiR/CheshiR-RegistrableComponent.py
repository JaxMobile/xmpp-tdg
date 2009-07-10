#!/usr/bin/env python

import logging
from SimpleBackend import SimpleBackend
from HTTPFrontend import HTTPFrontend
from RegistrableComponent import RegistrableComponent

#logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')

def main() :
	backend = SimpleBackend()
	component = RegistrableComponent(
		jid = "posts.cheshir.lit", password = "mypass",
		server = "cheshir.lit", port = 5060, backend = backend)
	component.start()
	httpFrontend = HTTPFrontend(8080, backend)
	httpFrontend.start()

if __name__ == '__main__' :
	main()
