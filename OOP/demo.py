class Student:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print('Accepting data')
        self.name = input('Enter name')
        self.contact = input('Enter your contact number')

    def putdata(self):
        print('Name is: '+self.name, '\nContact is: '+self.contact)


John = Student("", 0)
John.getdata()
John.putdata()
