'''class A:
   def method(self):
      print("A method")

class B(A):
   def another_method(self):
      print("B method")

class C(B):
   def third_method(self):
      print("C method")

c = C()
c.method()
c.another_method()
c.third_method()

import random
class special:
   def __init__(self,cont):
      self.cont = cont
   def __getitem__(self,index):
      return self.cont[index + random.randint(-1,1)]
   def __len__(self):
      return random.randint(0,len(self.cont)*2)

vogue_list = special(["A","B","C","D","E"])
print(len(vogue_list))
print(len(vogue_list))
print(vogue_list[2])
print(vogue_list[2])

a = 42
b = a
c= [a]

del a
b =100
c[0] = -1

class spam:
   __egg =7
   def print_egg(self):
      print(self.__egg)

s= spam()
s.print_egg()
print(s._spam__egg)
print(s.__egg)


class Rectangle:
   def __init__(self,width,height):
      self.width=width
      self.height = height

   def calculate_area(self):
      return self.width*self.height

   @classmethod
   def new_square(cls,side_length):
      return cls(side_length,side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())
'''

# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
       print(str(v) + ' ' + k)
       item_total += v
    print("Total number of items: " + str(item_total))
displayInventory(stuff)

class Parent:
   value1="this is value 1"
   value2="this is value 2"

class Child(Parent):
   pass
parent=Parent()







