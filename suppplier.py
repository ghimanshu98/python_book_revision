# sub class - inheritance

from contact import Contact

class Supplier(Contact):
    def order(self, order : "Order") -> None:
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )


s1 = Supplier("hardwar_supp", "hardware@xyz.com")
s2 = Supplier("Software_supp", "xyz@abc.com")

# test

print(Contact.all_contact)

s1.order("Pliers")