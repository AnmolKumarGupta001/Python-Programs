class Programmer:
    company= "Microsoft"
    def __init__(self, name , salary, pincode):
     self.name= name
     self.salary= salary
     self.pincode= pincode


p = Programmer("Anmol", 100000, 273008)
print(p.name,p.salary, p.company, p.pincode)
r = Programmer("Harry", 120000, 273522)
print(r.name,r.salary, r.company, r.pincode)