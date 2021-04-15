# importing the csv library
import csv
  
# opening the csv file by specifying
# the location
# with the variable name as csv_file
with open('output.csv') as csv_file:
  
    # creating an object of csv reader
    # with the delimiter as ,
    csv_reader = csv.reader(csv_file, delimiter = ',')
  
    # list to store the names of columns
    list_of_column_names = []
  
    # loop to iterate thorugh the rows of csv
    for row in csv_reader:
  
        # adding the first row
        list_of_column_names.append(row)
  
        # breaking the loop after the
        # first iteration itself
        break
  
# printing the result
print("List of column names : ",
      list_of_column_names[0])
