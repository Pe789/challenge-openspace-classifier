
from utils.table import Table

class Openspace:
  #This is a Openspace
  def __init__(self, number_of_tables):
    self.number_of_tables = number_of_tables
    self.tables = []
    for i in range(self.number_of_tables):
      self.tables.append(Table())
    
  def organize(self,names):
    for i in names:
      for j in self.tables:
        #print(f"colleague {i} and checking on table {j}")
        #print(j.has_free_spot())
        if j.has_free_spot() == True:
          j.assign_seat(i)
          #print(f"{i} being seated")
          break  
     
  def display(self):
    table_nr = 1
    for i in self.tables:
      seated = []
      for j in i.seats:      
        seated.append (j.occupant)
      print(f"Table {table_nr} has following persons seated :{seated}")
      table_nr = table_nr + 1
       
 