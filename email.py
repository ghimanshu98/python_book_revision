from typing import Protocol
from contact import Contact

class Emailable(Protocol):
    email: str

class MailSender(Emailable):
    def send_mail(self, message: str)-> None:
        print(f"sending mail to {self.email =}")
        # add email logic here

class EmailableContact(Contact, MailSender):
    pass