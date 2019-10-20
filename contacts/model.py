from contacts.contact import Contact
class ContactsModel:
    def __init__(self):
        pass

    @staticmethod
    def set_contact(name, phone, email, addr): #set (등록) / 하나씩등록 contact
        contact = Contact(name, phone, email, addr)
        return contact

    @staticmethod
    def get_contacts(params): #get (읽기) / 여러개읽기 contacts
        contacts = []
        for i in params:\
            contacts.append(i.to_string())
        return ''.join(contacts)

    @staticmethod
    def del_contact(params,name):
        for i, t in enumerate(params):
            if t.name == name:
                del params[i]