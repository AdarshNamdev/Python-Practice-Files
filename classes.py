class pwskills1(object):

    mobile = "750-715-7178"
    pie = 3.14
    def __init__(self, name, email, g):
        self.name = name
        self.email = email
        self.g = g

    @classmethod
    def details(cls, name1, email1):

        return cls(name1, email1)

    @staticmethod
    def modify_constants():
        pie = pwskills1.pie
        print(pie)


    def student_details(self):
        print(self.name, self.email, self.mobile)
        print(self.name, self.email, pwskills1.mobile)


pw1 = pwskills1("lalala", 'lala@gmail.com', 9.8)

print(pw1.modify_constants())


print(pw1.g)