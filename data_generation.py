import csv
import random
from faker import Faker
from contact import Contact

fake = Faker()

def random_phone():
    """
    Generate a random 10-digit phone number as a string.
    Returns:
        str: Random phone number.
    """
    return ''.join(random.choices('0123456789', k=10))

def random_company():
    """
    Generate a realistic company name using Faker.
    Returns:
        str: Random company name.
    """
    return fake.company()

def generate_contacts(n):
    """
    Generate a list of random Contact objects.
    Args:
        n (int): Number of contacts to generate.
    Returns:
        list: List of Contact objects.
    """
    contacts = []
    for i in range(n):
        contact = Contact(
            contact_id=i,
            firstname=fake.first_name(),
            lastname=fake.last_name(),
            company=random_company(),
            phonenumber=random_phone()
        )
        contacts.append(contact)
    return contacts

def write_contacts_to_csv(contacts, filename):
    """
    Write a list of Contact objects to a CSV file.
    Args:
        contacts (list): List of Contact objects.
        filename (str): Output CSV filename.
    Returns:
        None
    """
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['contact_id', 'firstname', 'lastname', 'company', 'phonenumber']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact.as_dict())

if __name__ == "__main__":
    """Generate a CSV file with random contacts for B-Tree application.
    Edit the line below to change number of contacts generated."""
    contacts = generate_contacts(20)
    write_contacts_to_csv(contacts, 'contacts_BTree.csv')
    print("contacts_BTree.csv generated with 20 realistic contacts.")
