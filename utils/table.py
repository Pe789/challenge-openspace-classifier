class Seat:
  #This is a seat
  def __init__(self):
    self.free = True
    self.occupant = ""
  def set_occupant(self,name):
    #allows the program to assign someone a seat if it's free
    self.free = False
    self.occupant = name
  def remove_occupant(self):
    #remove someone from a seat and return the name of the person occupying the seat before
    self.free = True
    self.occupant = ""

class Table:
  #This is a Table
  def __init__(self):
    self.capacity = 4
    self.seats = []
    for i in range(self.capacity):
      self.seats.append(Seat())

  def has_free_spot(self):
    for i in self.seats:
      if i.free == True:
        return True
        break  
  def assign_seat(self, name):
    #places someone at the table
    for i in self.seats:
      if i.free == True:
        i.set_occupant(name)
        #print(f"{i} is being seated")
        break   
  def left_capacity(self):
    count = 0
    for i in self.seats:
      #print(i.free)
      if i.free == True:
        count = count + 1
    return count  