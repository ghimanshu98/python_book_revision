from __future__ import annotations
from typing import List


# Extending built in class list

class ContactList(list["Contact"]):  # inheriting nuiltin class "list", of Contact ojects
    
    def search(self, name :str) -> list["Contact"]:
        
        matching_contacts : list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    """
    This example introduces us to class variables. The all_contacts list, because
    it is part of the class definition, is shared by all instances of this class. This
    means that there is only one Contact.all_contacts list. We can also access it as
    self.all_contacts from within any method on an instance of the Contact class.
    """
    all_contacts = ContactList()  # global list

    def __init__(self, name : str, email : str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)  # it is appeneding the newly created object

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"
            f")"
        )



"""
>>> c1 = Contact("John A", "johna@example.net")
>>> c2 = Contact("John B", "johnb@sloop.net")
>>> c3 = Contact("Jenna C", "cutty@sark.io")
>>> [c.name for c in Contact.all_contacts.search('John')]
"""