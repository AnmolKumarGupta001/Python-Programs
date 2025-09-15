class Employee:
    a=1
  



class manager(Employee):

    a=2


class staff(manager):
    a=3
    
o = manager()
print(o.a)
