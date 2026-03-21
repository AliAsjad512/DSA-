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
            

            def check_expiry(self):
        """Check certificate expiry details"""
        cert = self.get_certificate()
        # Get notAfter date
        not_after_str = cert.get_notAfter().decode('ascii')
        # Format: YYYYMMDDHHMMSSZ
        expiry = datetime.datetime.strptime(not_after_str, '%Y%m%d%H%M%S%z')
        now = datetime.datetime.now(datetime.timezone.utc)
        days_left = (expiry - now).days

        # Get subject and issuer
        subject = dict(cert.get_subject().get_components())
        issuer = dict(cert.get_issuer().get_components())

        return {
            'host': self.host,
            'port': self.port,
            'expiry_date': expiry.isoformat(),
            'days_left': days_left,
            'subject': {k.decode(): v.decode() for k, v in subject.items()},
            'issuer': {k.decode(): v.decode() for k, v in issuer.items()},
            'valid': days_left > 0
        }