from contacts.contact import Contact
class ContactsModel:
    def __init__(self):
        pass

    # 정보입력
    @staticmethod
    def set_contact(name, phone, email, addr): # set (등록) / 하나씩등록 contact
        contact = Contact(name, phone, email, addr)
        return contact
    # 1명의 개인정보를 설정 (contact 단수)

    # 정보가져오기
    @staticmethod
    def get_contacts(params): # get (읽기) / 여러개읽기 contacts
        contacts = []
        for i in params:
            contacts.append(i.to_string())
        return ''.join(contacts)
    # 여러명의 개인정보를 가져오는 것

    # 정보삭제
    @staticmethod
    def del_contact(params, name):
        for i, t in enumerate(params):
            if t.name == name:
                del params[i]