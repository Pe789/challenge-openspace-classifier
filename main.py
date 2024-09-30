from utils.openspace import Openspace
from utils.table import Table, Seat
import csv
import random

# putting it all together

colleagues = [] #making a list of new_colleagues
with open('new_colleagues.csv', "r") as my_file:    
    for i in csv.reader(my_file):
       colleagues = colleagues + i
    random.shuffle(colleagues) # shuffling the list of colleagues randomly
print(colleagues)
number_of_colleagues = len(colleagues)
print (number_of_colleagues)



open_space_final = Openspace(6) #6 tables of 4 being created
open_space_final.organize(colleagues) # seating the colleagues at the tables in the open space
open_space_final.display() #displaying the results





