# contacts.py

class Contact:
    def __init__(self, name, genre, email):
        self.name = name
        self.genre = genre
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, genre, email):
        contact = Contact(name, genre, email)
        self.contacts.append(contact)

    def get_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def update_contact(self, name, genre=None, email=None):
        contact = self.get_contact(name)
        if contact:
            if genre:
                contact.genre = genre
            if email:
                contact.email = email
            return contact
        return None

    def list_contacts(self):
        return [(contact.name, contact.genre, contact.email) for contact in self.contacts]