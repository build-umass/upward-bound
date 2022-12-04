
import json
import socket
import re
import os
import threading
import requests


# Host and Port
HOST = '0.0.0.0'
PORT = 1997

PYTHON_PATH = os.getenv('PYTHON_PATH')

"""
This file will be the server which listens for get requests from the client(which is yet to be constructed),
use the query parameters to send the DocuSign Envelope to the correct recipient.

Note: this is some boiler plate for a potential use case and we can interate to include more use cases as they arise.

Other Note: Mutlithreading might not be necessary but it follows sound software practices.
"""

def threaded(c):
	while True:
		"""
		Parse request and handle according to the Docusign API guidelines
		"""
		break


def main():
    print("Server started on port {}".format(PORT))
    # Create Socket and Listen
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(5)
    while True:
        c, addr = s.accept()
        # lock acquired by client
        print("Connected to :", addr[0], ":", addr[1])

        # Start a new thread and return its identifier
        t = threading.Thread(target=threaded, args=(c,))
        t.start()


if __name__ == '__main__':
    main()