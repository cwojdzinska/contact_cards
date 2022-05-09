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
        
    
    def contact1(self):
        return f'Kontaktuję się z {self.name} {self.surname} dzwoniąc na {self.company_cell}'
    
    @property
    def counting_business(self):
        return len(self.name)+len(self.surname)
   
    
name1=BaseContact(name="John", surname="Doe", company="Solaris", role="VP", cell="+49-153926354", email="john@solaris.com")
name2=BusinessContact(name="Jola", surname="Boska", company="Solaris", role="Manager", company_cell="+28-264819911", company_email="jola@solaris.com")

print(name1.counting)
print(name1.contact())

print(name2.counting_business)
print(name2.contact1())
