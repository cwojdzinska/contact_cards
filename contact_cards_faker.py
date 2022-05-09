from faker import Faker 

class Card:
    def __init__(self, name, surname, company, role, cell='', email=''):
        self.name = name
        self.surname = surname
        self.company = company
        self.role = role
        self.cell = cell
        self.email = email
    
    def __str__(self):
        return f'{self.name} {self.surname} {self.company} {self.role} {self.email}'
    
class BaseContact(Card):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def contact(self):
        return f'Kontaktuję się z {self.name} {self.surname} dzwoniąc na {self.cell}'
    
    @property
    def counting(self):
        return len(self.name)+len(self.surname)
  

class BusinessContact(Card):
    def __init__(self, company_cell, company_email,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_cell = company_cell
        self.company_email = company_email
        
    
    def contact(self):
        return f'Kontaktuję biznesowo się z {self.name} {self.surname} dzwoniąc na {self.company_cell}'
    
    @property
    def counting_business(self):
        return len(self.name)+len(self.surname)
   



def create_contacts(card_type, card_count):   
    fake = Faker()
    contacts = []
    
    for i in range(0, card_count):
        name=fake.name().split()[0]
        surname=fake.name().split()[1]
        role=fake.job()
        company=fake.company()
        email=f'{name.lower().replace(".","")}.{surname.lower().replace(".","")}@{fake.email().split("@")[1]}'
        cell=fake.phone_number()
        if card_type==BusinessContact:
            contacts.append(BusinessContact(name=name, surname=surname, company=company, role=role, company_cell=cell, company_email=email))     
        elif card_type==BaseContact:
            contacts.append(BaseContact(name=name, surname=surname, company=company, role=role, cell=cell, email=email))
        else:
            pass

    return contacts

if __name__=="__main__":
    contacts=create_contacts(BusinessContact,10)
    
    for c in contacts:
        print (c)
        print (c.contact())

    contacts=create_contacts(BaseContact,5)

    for c in contacts:
        print (c)
        print (c.contact())


