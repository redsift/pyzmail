import email.mime.text
import unittest, doctest
import pyzmail
from pyzmail.generate import *

class TestGenerate(unittest.TestCase):

    def setUp(self):
        pass

    def test_format_addresses(self):
        """test format_addresse"""
        self.assertEqual('foo@example.com', str(format_addresses([ 'foo@example.com', ])))
        self.assertEqual('Foo <foo@example.com>', str(format_addresses([ ('Foo', 'foo@example.com'), ])))
        # notice the space around the comma
        self.assertEqual('foo@example.com , bar@example.com', str(format_addresses([ 'foo@example.com', 'bar@example.com'])))
        # notice the space around the comma
        self.assertEqual('Foo <foo@example.com> , Bar <bar@example.com>', str(format_addresses([ ('Foo', 'foo@example.com'), ( 'Bar', 'bar@example.com')])))

    def test_complete_mail(self):
        """test complete_mail"""
        msg=email.mime.text.MIMEText('The text.', 'plain', 'us-ascii')
        payload, mail_from, rcpt_to, msg_id = complete_mail(
            msg,
            ("Me", "me@foo.com"),
            [("Him", "him@bar.com")],
            "Non unicode subject",
            "iso-8859-1",
            cc=["her@bar.com"],
            bcc=["them@bar.com"],
            date=1313558269,
            headers=[("User-Agent", u"pyzmail")],
        )
        self.assertEqual(['him@bar.com', 'her@bar.com', 'them@bar.com'], rcpt_to)

# Add doctest
def load_tests(loader, tests, ignore):
    # this works with python 2.7 and 3.x
    tests.addTests(doctest.DocTestSuite(pyzmail.generate))
    return tests

def additional_tests():
    # Add doctest for python 2.6 and below
    if sys.version_info<(2, 7):
        return doctest.DocTestSuite(pyzmail.generate)
    else:
        return unittest.TestSuite()
