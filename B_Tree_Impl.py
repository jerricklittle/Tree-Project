# Main File for Application

import random
import string
import csv
from contact import Contact


def random_phone():
    """Generate a random phone number."""
    return ''.join(random.choices(string.digits, k=10))

def random_name():
    """Generate a random name."""
    return ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=6))

def random_company():
    """Generate a random company name."""
    return ''.join(random.choices(string.ascii_uppercase, k=3)) + ' Inc.'

# Read contacts from a CSV file
def read_contacts_from_csv(filename):
    """
    Read contacts from a CSV file and return a list of Contact objects.
    Args:
        filename (str): Path to the CSV file.
    Returns:
        list: List of Contact objects.
    """
    contacts = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            contact = Contact(
                contact_id=int(row['contact_id']),
                firstname=row['firstname'],
                lastname=row['lastname'],
                company=row['company'],
                phonenumber=row['phonenumber']
            )
            contacts.append(contact)
    return contacts

class BTreeNode:
    """
    Node of a B-Tree. Stores keys and child pointers.
    Args:
        t (int): Minimum degree.
        leaf (bool): True if node is a leaf.
    """
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree (defines the range for number of keys)
        self.leaf = leaf  # True if leaf node, false otherwise
        self.keys = []  # List of keys in the node
        self.child = []  # List of child pointers

class BTree:
    """
    B-Tree data structure for storing and managing contacts.
    Args:
        t (int): Minimum degree of the B-Tree.
    """
    def __init__(self, t):
        self.root = BTreeNode(t, True)  # Create the root node
        self.t = t  # Minimum degree

    def search(self, x, k):
        """
        Search for a key in the B-Tree.
        Args:
            x (BTreeNode): Node to start search from.
            k (int): Key to search for (contact_id).
        Returns:
            Contact or None: Contact if found, else None.
        """
        i = 0
        while i < len(x.keys) and k > x.keys[i][0]:
            i += 1
        if i < len(x.keys) and k == x.keys[i][0]:
            return x.keys[i][1]
        elif x.leaf:
            return None
        else:
            return self.search(x.child[i], k)

    def range_query(self, x, k1, k2, result=None):
        """
        Find all contacts with contact_id in [k1, k2].
        Args:
            x (BTreeNode): Node to start from.
            k1 (int): Start of range.
            k2 (int): End of range.
            result (list): Accumulator for results.
        Returns:
            list: List of Contact objects in range.
        """
        if result is None:
            result = []
        i = 0
        while i < len(x.keys) and x.keys[i][0] < k1:
            i += 1
        while i < len(x.keys) and x.keys[i][0] <= k2:
            if not x.leaf:
                self.range_query(x.child[i], k1, k2, result)
            result.append(x.keys[i][1])
            i += 1
        if not x.leaf and i < len(x.child):
            self.range_query(x.child[i], k1, k2, result)
        return result

    def traverse(self, x, result=None):
        """
        Traverse the B-Tree in order and collect all contacts.
        Args:
            x (BTreeNode): Node to start from.
            result (list): Accumulator for results.
        Returns:
            list: List of all Contact objects in order.
        """
        if result is None:
            result = []
        i = 0
        for i in range(len(x.keys)):
            if not x.leaf:
                self.traverse(x.child[i], result)
            result.append(x.keys[i][1])
        if not x.leaf:
            self.traverse(x.child[i+1], result)
        return result

    def insert(self, k):
        """
        Insert a key into the B-Tree.
        Args:
            k (tuple): (contact_id, Contact) tuple to insert.
        Returns:
            None
        """
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(self.t)
            temp.leaf = False
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.root = temp
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        """
        Insert a key into a non-full node.
        Args:
            x (BTreeNode): Node to insert into.
            k (tuple): (contact_id, Contact) tuple to insert.
        Returns:
            None
        """
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        """
        Split a full child node during insertion.
        Args:
            x (BTreeNode): Parent node.
            i (int): Index of child to split.
        Returns:
            None
        """
        t = self.t
        y = x.child[i]
        z = BTreeNode(t, y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t]

    def delete(self, x, k):
        """
        Delete a key from the B-Tree.
        Args:
            x (BTreeNode): Node to start from.
            k (tuple): (contact_id, Contact) tuple to delete.
        Returns:
            None
        """
        t = self.t
        i = 0
        while i < len(x.keys) and k[0] > x.keys[i][0]:
            i += 1
        if x.leaf:
            if i < len(x.keys) and x.keys[i][0] == k[0]:
                x.keys.pop(i)
                return
        else:
            if i < len(x.keys) and x.keys[i][0] == k[0]:
                return self.delete_internal_node(x, k, i)
            if len(x.child[i].keys) < t:
                self.fill(x, i)
            self.delete(x.child[i], k)

    def delete_internal_node(self, x, k, i):
        """
        Delete a key from an internal node.
        Args:
            x (BTreeNode): Node.
            k (tuple): (contact_id, Contact) tuple.
            i (int): Index of key in node.
        Returns:
            None
        """
        t = self.t
        if len(x.child[i].keys) >= t:
            pred_key = self.get_predecessor(x, i)
            x.keys[i] = pred_key
            self.delete(x.child[i], pred_key)
        elif len(x.child[i + 1].keys) >= t:
            succ_key = self.get_successor(x, i)
            x.keys[i] = succ_key
            self.delete(x.child[i + 1], succ_key)
        else:
            self.merge(x, i)
            self.delete(x.child[i], k)

    def get_predecessor(self, x, i):
        """
        Get the predecessor key for a given key in a node.
        Args:
            x (BTreeNode): Node.
            i (int): Index of key.
        Returns:
            tuple: Predecessor key.
        """
        cur = x.child[i]
        while not cur.leaf:
            cur = cur.child[len(cur.child) - 1]
        return cur.keys[len(cur.keys) - 1]

    def get_successor(self, x, i):
        """
        Get the successor key for a given key in a node.
        Args:
            x (BTreeNode): Node.
            i (int): Index of key.
        Returns:
            tuple: Successor key.
        """
        cur = x.child[i + 1]
        while not cur.leaf:
            cur = cur.child[0]
        return cur.keys[0]

    def merge(self, x, i):
        """
        Merge two child nodes of a node.
        Args:
            x (BTreeNode): Parent node.
            i (int): Index of key to merge at.
        Returns:
            None
        """
        t = self.t
        child = x.child[i]
        sibling = x.child[i + 1]
        child.keys.append(x.keys[i])
        child.keys.extend(sibling.keys)
        if not child.leaf:
            child.child.extend(sibling.child)
        x.keys.pop(i)
        x.child.pop(i + 1)
        if len(x.keys) == 0:
            self.root = child

    def fill(self, x, i):
        """
        Ensure a child node has at least t keys.
        Args:
            x (BTreeNode): Parent node.
            i (int): Index of child.
        Returns:
            None
        """
        t = self.t
        if i != 0 and len(x.child[i - 1].keys) >= t:
            self.borrow_from_prev(x, i)
        elif i != len(x.child) - 1 and len(x.child[i + 1].keys) >= t:
            self.borrow_from_next(x, i)
        else:
            if i != len(x.child) - 1:
                self.merge(x, i)
            else:
                self.merge(x, i - 1)

    def borrow_from_prev(self, x, i):
        """
        Borrow a key from the previous sibling.
        Args:
            x (BTreeNode): Parent node.
            i (int): Index of child.
        Returns:
            None
        """
        child = x.child[i]
        sibling = x.child[i - 1]
        child.keys.insert(0, x.keys[i - 1])
        x.keys[i - 1] = sibling.keys.pop()
        if not child.leaf:
            child.child.insert(0, sibling.child.pop())

    def borrow_from_next(self, x, i):
        """
        Borrow a key from the next sibling.
        Args:
            x (BTreeNode): Parent node.
            i (int): Index of child.
        Returns:
            None
        """
        child = x.child[i]
        sibling = x.child[i + 1]
        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)
        if not child.leaf:
            child.child.append(sibling.child.pop(0))

# Build B-tree from contacts dataset
if __name__ == "__main__":
    """Main application to manage contacts using B-Tree.
    Also provides a simple command-line interface for user interaction."""

    contacts = read_contacts_from_csv('contacts_BTree.csv')
    btree = BTree(3)
    for contact in contacts:
        btree.insert(contact.as_tuple())

    def print_menu():
        print("\nContact Manager B-Tree Options:")
        print("1: Show Whole Traversal")
        print("2: Search for a contact by last name")
        print("3: Insert a contact")
        print("4: Delete a contact by last name")
        print("5: Exit")

    def input_contact():
        try:
            contact_id = int(input("Enter contact_id (integer): "))
            firstname = input("Enter first name: ").strip()
            lastname = input("Enter last name: ").strip()
            company = input("Enter company: ").strip()
            phonenumber = input("Enter phone number: ").strip()
            if not (firstname and lastname and company and phonenumber):
                print("All fields are required!")
                return None
            return Contact(contact_id, firstname, lastname, company, phonenumber)
        except Exception as e:
            print(f"Invalid input: {e}")
            return None

    def search_by_lastname(btree, lastname):
        results = []
        for c in btree.traverse(btree.root):
            if c.lastname.lower() == lastname.lower():
                results.append(c)
        return results

    def delete_by_lastname(btree, lastname):
        found = False
        for c in btree.traverse(btree.root):
            if c.lastname.lower() == lastname.lower():
                btree.delete(btree.root, (c.contact_id,))
                found = True
        return found

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            print("\nAll contacts in B-tree (in order):")
            for c in btree.traverse(btree.root):
                print(c)
        elif choice == '2':
            lastname = input("Enter last name to search: ").strip()
            results = search_by_lastname(btree, lastname)
            if results:
                print("Found contacts:")
                for c in results:
                    print(c)
            else:
                print("No contact found with that last name.")
        elif choice == '3':
            contact = input_contact()
            if contact:
                btree.insert(contact.as_tuple())
                print("Contact inserted.")
        elif choice == '4':
            lastname = input("Enter last name to delete: ").strip()
            if delete_by_lastname(btree, lastname):
                print("Contact(s) deleted.")
            else:
                print("No contact found with that last name.")
        elif choice == '5':
            print("Exiting Application.")
            break
        else:
            print("Invalid choice. Try again.")

