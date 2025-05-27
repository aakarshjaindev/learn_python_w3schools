# python polymorphism
'''
the word polymorphism means " namy forms and in progrmamingg ti refers to methods /functions opernatgorwith the same nname than canb neb eexecuted on lmany objects of classes 
'''


# functional polymorphism 
'''
* an example fo a python fucntion tha can be used on different  objsesc is the len() function'''
# sring 
# for strings len() return the numnber of charcaters


x = " hello, world"
print(len(x))

# DICTIONARY 
thisdict = { 
           "brand" : "ford" , 
           "model  ": 'mustang',
           "year ": 1942
           }
    
print(len(thisdict))



# inhertiance class polymorphisms
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.modelp = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()



