class Contact:
    """
    Represents a contact with id, name, company, and phone number.
    Args:
        contact_id (int): Unique identifier for the contact.
        firstname (str): First name of the contact.
        lastname (str): Last name of the contact.
        company (str): Company name.
        phonenumber (str): Phone number.
    """
    def __init__(self, contact_id, firstname, lastname, company, phonenumber):
        self.contact_id = contact_id
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.phonenumber = phonenumber
    def __repr__(self):
        """
        Returns a string representation of the Contact.
        Returns:
            str: String representation.
        """
        return f"Contact({self.contact_id}, {self.firstname}, {self.lastname}, {self.company}, {self.phonenumber})"
    def as_tuple(self):
        """
        Returns the contact as a tuple (contact_id, Contact).
        Returns:
            tuple: (contact_id, Contact)
        """
        return (self.contact_id, self)
    def as_dict(self):
        """
        Returns the contact as a dictionary for CSV writing.
        Returns:
            dict: Contact fields as dictionary.
        """
        return {
            'contact_id': self.contact_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'company': self.company,
            'phonenumber': self.phonenumber
        }
