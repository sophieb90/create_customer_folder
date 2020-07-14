
# script to create folders based on customer names
# version 1.0.0
# created on 24 June 2020
# created by Sophie

# import modules
import os
# specify name of file
file = 'customers.py'
# check if text file does not exist
if not os.path.exists(file):
  # if it doesn't exist stop with error message
  print('Error: file ' + file +' does not exist!')
  exit()
# if file exists 
else:
  print('File found: ' + file )
  #  open file
  f = open( file, "r" )
  # create a list
  customers = []
  # read all lines in file
  for line in f:
    name = line.rstrip('\n')
    print( 'adding ' + name + ' to the list' )
    # add line to the list
    customers.append( name )
  print( customers )

# loop though the List
for customer in customers:
#   create path using name
  try:
    os.mkdir(customer)
#   if folder already exists
  except OSError as errorName:
    print(errorName)
