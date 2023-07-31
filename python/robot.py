class robot:
   def __init__(self , n , c ,w):
      self.name = n
      self.colour = c
      self.weight = w
      
   def bodysize(self):
      if self.name == "Robot 1":
         print('I am', self.name)
         print(self.name, "'s colour is", self.colour)
         print(self.name, "'s weight is ", self.weight)
      elif self.name == "Robot 2":
         print('I am', self.name)
         print(self.name, "'s colour is", self.colour)
         print(self.name, "'s weight is", self.weight)
      else:
         print('Database not found')


r1 = robot("Robot 1", 'red', 30)
r1.bodysize()

r2 = robot("Robot 2", 'blue', 60)
r2.bodysize()
