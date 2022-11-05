from typing import List

class Contact:
    """
    This example introduces us to class variables. The all_contacts list, because
    it is part of the class definition, is shared by all instances of this class. This
    means that there is only one Contact.all_contacts list. We can also access it as
    self.all_contacts from within any method on an instance of the Contact class.
    """
    all_contact : List["Contact"] = []  # global list

    def __init__(self, name : str, email : str) -> None:
        self.name = name
        self.email = email
        Contact.all_contact.append(self)  # it is appeneding the newly created object

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}"
            f")"
        )


class Friend(Contact):
    # over riding initialization method of super class
    # def __init__(self, name: str, email: str, phone: str) -> None:
    #     self.name = name  
    #     self.email = email
    #     self.phone = phone
        # duplicate code to set up email and name properties, which can be avoided by below syntax

    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone =phone    
    """
    This example first binds the instance to the parent class using super() and
    calls __init__() on that object, passing in the expected arguments. It then does
    its own initialization, namely, setting the phone attribute, which is unique to the
    Friend class."""






    
# test:

# p1 = Contact("Himanshu", "ghimanshu98@gmail.com")
# p2 = Contact("Sergio", "sergio@yahoo.com")

# print(p1)
# print(p2)
# print(p1.all_contact)
# print(Contact.all_contact)