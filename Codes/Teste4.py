import re
import unittest
from flask import Flask

app = Flask(__name__)

class EmailValidator:
    allowed_domains = ['gmail.com', 'hotmail.com', 'bol.com', 'yahoo.com']

    @staticmethod
    def validate(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        domain = email.split('@')[1]
        return domain in EmailValidator.allowed_domains

# Testes unitários
import unittest

class TestEmailValidator(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(EmailValidator.validate('user@gmail.com'))
        self.assertTrue(EmailValidator.validate('another_user@hotmail.com'))
        self.assertTrue(EmailValidator.validate('test@bol.com'))
        self.assertTrue(EmailValidator.validate('example@yahoo.com'))

    def test_invalid_emails(self):
        self.assertFalse(EmailValidator.validate('user@example.com'))
        self.assertFalse(EmailValidator.validate('test@invaliddomain.org'))
        self.assertFalse(EmailValidator.validate('user@gmailcom'))
        self.assertFalse(EmailValidator.validate('user.gmail.com'))

if __name__ == "__main__":
    unittest.main()
