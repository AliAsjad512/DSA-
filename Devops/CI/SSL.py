SSL Certificate Expiry Checker - Check SSL certificate expiry dates


import ssl
import socket
import datetime
import argparse
import OpenSSL
import certifi
import json

class SSLChecker:
    def __init__(self, host, port=443):
        self.host = host
        self.port = port

    def get_certificate(self):
        """Retrieve SSL certificate from host"""
        context = ssl.create_default_context()
        with socket.create_connection((self.host, self.port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=self.host) as ssock:
                cert_bin = ssock.getpeercert(binary_form=True)
                cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, cert_bin)
                return cert